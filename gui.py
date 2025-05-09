import os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QPixmap
from television import Television  # Ensure this import is correct

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 350)
        MainWindow.setMaximumSize(QtCore.QSize(350, 350))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.channel = QtWidgets.QLabel(parent=self.centralwidget)
        self.channel.setGeometry(QtCore.QRect(50, 240, 50, 21))
        self.channel.setObjectName("channel")
        self.channel_up = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel_up.setGeometry(QtCore.QRect(20, 210, 81, 21))
        self.channel_up.setObjectName("channel_up")
        self.channel_down = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel_down.setGeometry(QtCore.QRect(20, 270, 81, 21))
        self.channel_down.setObjectName("channel_down")
        self.volume_down = QtWidgets.QPushButton(parent=self.centralwidget)
        self.volume_down.setGeometry(QtCore.QRect(250, 270, 81, 21))
        self.volume_down.setObjectName("volume_down")
        self.volume_up = QtWidgets.QPushButton(parent=self.centralwidget)
        self.volume_up.setGeometry(QtCore.QRect(250, 210, 81, 21))
        self.volume_up.setObjectName("volume_up")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 240, 31, 16))
        self.label.setObjectName("label")
        self.toggle_power = QtWidgets.QPushButton(parent=self.centralwidget)
        self.toggle_power.setGeometry(QtCore.QRect(120, 180, 111, 21))
        self.toggle_power.setObjectName("toggle_power")
        self.toggle_mute = QtWidgets.QPushButton(parent=self.centralwidget)
        self.toggle_mute.setGeometry(QtCore.QRect(130, 220, 91, 21))
        self.toggle_mute.setObjectName("toggle_mute")
        self.horizontalSlider = QtWidgets.QSlider(parent=self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(90, 140, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.channel_image_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.channel_image_label.setGeometry(QtCore.QRect(40, 20, 261, 91))
        self.channel_image_label.setText("")
        self.channel_image_label.setObjectName("channel_image_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.channel.setText(_translate("MainWindow", "CH"))
        self.channel_up.setText(_translate("MainWindow", "+"))
        self.channel_down.setText(_translate("MainWindow", "-"))
        self.volume_down.setText(_translate("MainWindow", "-"))
        self.volume_up.setText(_translate("MainWindow", "+"))
        self.label.setText(_translate("MainWindow", "VOL"))
        self.toggle_power.setText(_translate("MainWindow", "Power"))
        self.toggle_mute.setText(_translate("MainWindow", "Mute"))

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tv = Television()

        # Connect buttons to their respective handlers
        self.toggle_power.clicked.connect(self.toggle_power_handler)
        self.toggle_mute.clicked.connect(self.toggle_mute_handler)
        self.channel_up.clicked.connect(self.channel_up_handler)
        self.channel_down.clicked.connect(self.channel_down_handler)
        self.volume_up.clicked.connect(self.volume_up_handler)
        self.volume_down.clicked.connect(self.volume_down_handler)

        # Initialize the volume slider range
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(self.tv.MAX_VOLUME)

        # Update the display initially
        self.update_display()

    def update_display(self):
        """
        Updates the display based on the television's current state.
        """
        # Update channel number
        self.channel.setText(f"CH {self.tv.get_channel()}")

        # Update volume slider
        if self.tv.get_power() and not self.tv.get_muted():
            self.horizontalSlider.setValue(self.tv.get_volume())
        else:
            self.horizontalSlider.setValue(0)

        # Update channel image
        image_path = f"channel_images/channel{self.tv.get_channel()}.jpg"
        if os.path.exists(image_path):
            # Load the image
            pixmap = QPixmap(image_path)

            # Scale the image to fit the QLabel size while maintaining aspect ratio
            scaled_pixmap = pixmap.scaled(self.channel_image_label.size(), QtCore.Qt.AspectRatioMode.KeepAspectRatio)

            # Set the scaled pixmap to the QLabel
            self.channel_image_label.setPixmap(scaled_pixmap)
        else:
            # If the image doesn't exist, clear the QLabel
            self.channel_image_label.clear()

    def toggle_power_handler(self):
        """
        Toggle the power status of the television.
        """
        self.tv.power()
        self.update_display()

    def toggle_mute_handler(self):
        """
        Toggle mute status of the television.
        """
        self.tv.mute()
        self.update_display()

    def channel_up_handler(self):
        """
        Increase the channel by 1.
        """
        self.tv.channel_up()
        self.update_display()

    def channel_down_handler(self):
        """
        Decrease the channel by 1.
        """
        self.tv.channel_down()
        self.update_display()

    def volume_up_handler(self):
        """
        Increase the volume by 1.
        """
        self.tv.volume_up()
        self.update_display()

    def volume_down_handler(self):
        """
        Decrease the volume by 1.
        """
        self.tv.volume_down()
        self.update_display()

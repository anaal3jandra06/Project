class Television:
    """
    A class to simulate the basic functionalities of a television.
    """

    MIN_VOLUME = 0
    MAX_VOLUME = 10
    MIN_CHANNEL = 0
    MAX_CHANNEL = 10

    def __init__(self):
        """
        Initialize the Television with power off, muted off,
        volume at minimum, and channel at minimum.
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        """
        Toggle the power status of the television.
        """
        self.__status = not self.__status

    def mute(self):
        """
        Toggle the mute status if the television is powered on.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        """
        Increase the channel by 1, or wrap around to minimum channel
        if currently at maximum channel, if the television is powered on.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        """
        Decrease the channel by 1 , or wrap around to maximum channel
        if currently at minimum channel, if the television is powered on.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        """
        Increase the volume by 1 up to the maximum volume.
        If muted, unmute first. Only works if the television is powered on.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """
        Decrease the volume by 1 down to the minimum volume.
        If muted, unmute first. Only works if the television is powered on.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    # Getter Methods (added to fix the error)
    def get_power(self):
        return self.__status

    def get_muted(self):
        return self.__muted

    def get_volume(self):
        return self.__volume

    def get_channel(self):
        return self.__channel

    def __str__(self):
        """
        Return a string showing the power status, current channel,
        and volume (showing minimum volume if muted).
        """
        if self.__muted:
            volume_display = Television.MIN_VOLUME
        else:
            volume_display = self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume_display}"

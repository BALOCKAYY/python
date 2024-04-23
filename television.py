class Television():
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        This function sets the original power of the TV as off, the mute button as off for when the TV is powered on,
        the volume of the TV to MIN_VOLUME = 0, and the channel of the TV to MIN_CHANNEL = 3.
        """        
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self):
        """
        This function sets the power of the TV to "on" if it is off, and 
        "off" if it is on.
        """        
        self.__status: bool = not self.__status

    def mute(self):
        """
        This function sets the TV to muted if it is turned on if the TV was not muted before,
        and sets the TV to unmuted if the TV was powered on and muted.
        """        
        global volume
        volume = self.__volume
        if self.__status:
            self.__muted: bool = not self.__muted
            self.__volume: int = 0


    def channel_up(self):
        """
        This function turns the channel up by adding one to channel if the TV is on, and if the channel is at the MAX_CHANNEL
        which means channel has a value of 3, it will change it to the MIN_CHANNEL if you try to change the channel up.
        """        
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel: int = Television.MIN_CHANNEL
            else:
                self.__channel: int = self.__channel + 1
                

    def channel_down(self):
        """
        This function turns the channel down by subtracting one to channel if the TV is on, and if the channel is at the MIN_CHANNEL
        which means the channel has a value of 0, then it will change it to the MAX_CHANNEL if you try to change the channel down.
        """        
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel: int = Television.MAX_CHANNEL
            else:
                self.__channel: int = self.__channel - 1


    def volume_up(self):
        """
        This function will turn the TV volume up if the TV is powered on, and if the TV is muted it will grab the volume value
        that the TV was at before it was muted and turn it up by adding one to the original volume. If the TV is not muted the 
        volume will go up 1 normally. If the TV is at the MAX_VOLUME which means the volume has a value of 2, nothing will happen
        and the TV will stay at MAX_VOLUME.
        """        
        if self.__status:
            if self.__muted:
                self.__volume: int = volume
                self.__muted: bool = False
                if self.__volume == Television.MAX_VOLUME:
                    self.__volume: int = Television.MAX_VOLUME
                else:
                    self.__volume: int = self.__volume + 1
            else:
                if self.__volume == Television.MAX_VOLUME:
                    self.__volume: int = Television.MAX_VOLUME
                else:
                    self.__volume: int = self.__volume + 1

    
    def volume_down(self):
        """
        This function will turn the TV volume down if the TV is powered on, and if the TV is muted it will grab the volume value
        that the TV was at before it was muted and turn it down by subtracting one from the original volume. If the TV is not
        muted the volume will go down by 1 normally. If the TV is at the MIN_VOLUME which means the volume has a value of 0, 
        nothing will happen and the TV will stay at MIN_VOLUME.
        """
        if self.__status:
            if self.__muted:
                self.__volume: int = volume
                self.__muted: bool =  False
                if self.__volume == Television.MIN_VOLUME:
                    self.__volume: int = Television.MIN_VOLUME
                else:
                    self.__volume: int = self.__volume - 1
            else:
                if self.__volume == Television.MIN_VOLUME:
                    self.__volume: int = Television.MIN_VOLUME
                else:
                    self.__volume: int = self.__volume - 1
        

    def __str__(self):
        """
        This function takes the values of status (Power ON/OFF), channel (Channel number), and volume (Volume of TV) at their
        current values and packs them into a string that displays each back to the user in a clean format.
        """        
        status: bool = self.__status
        channel: int = self.__channel
        volume_level: int = self.__volume
        return f"Power = {status}, Channel = {channel}, Volume = {volume_level}"

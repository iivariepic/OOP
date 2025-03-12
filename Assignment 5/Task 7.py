class WirelessDevice:
    def __init__(self, maxBattery:float):
        self.__maxBattery:float = maxBattery
        self.__remainingBattery:float = maxBattery
        self.__is_on:bool = True

    def use_battery(self, used_battery:float):
        self.__remainingBattery -= used_battery
        if self.__remainingBattery <= 0:
            self.__remainingBattery = 0
            self.turn_off()

    def charge(self, amount:float):
        self.__remainingBattery += amount
        if self.__remainingBattery > self.__maxBattery:
            self.__remainingBattery = self.__maxBattery

    def turn_off(self):
        self.__is_on = False

    def turn_on(self):
        if self.__remainingBattery > 0:
            self.__is_on = True

class TvRemote(WirelessDevice):
    def charge(self):
        # Switching to a new battery means fully charging always
        self.__remainingBattery = self.__maxBattery

    def use(self):
        # insert random logic here
        pass
        self.use_battery(0.1)

    def turn_off(self):
        raise ValueError('TV Remote cannot be turned off')

class MobilePhone(WirelessDevice):
    def use(self):
        # insert random logic here
        pass
        self.use_battery(0.01)
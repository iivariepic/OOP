from drill import Drill

class CordlessDrill(Drill):
    def __init__(self, manufacturer, model, rpm, max_battery):
        super().__init__(manufacturer, model, rpm, connector_size=10)
        self.__max_battery = max_battery
        self.__battery = max_battery

    def use_battery(self, used_battery):
        # Returns if there is battery remaining
        self.__battery -= used_battery
        if self.__battery <= 0:
            self.__battery = 0
            return False

        return True

    def charge_battery(self, charged_battery):
        # Returns if battery is not at max
        self.__battery += charged_battery
        if self.__battery >= self.__max_battery:
            self.__battery = self.__max_battery
            return False

        return True

    def has_battery(self):
        return self.__battery > 0
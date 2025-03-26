from tool import Tool
from drilling_tool import DrillingTool

class Drill(Tool):
    def __init__(self, manufacturer, model, connector_size:int):
        super().__init__(manufacturer, model)
        self.connector_size = connector_size # Is in mm
        self.__attached_bit = None

    def change_bit(self, new_bit):
        self.__attached_bit.detach()
        self.__attached_bit = new_bit

    def remove_bit(self):
        self.__attached_bit.detach()
        self.__attached_bit = None

    @property
    def attached_bit(self):
        return self.__attached_bit
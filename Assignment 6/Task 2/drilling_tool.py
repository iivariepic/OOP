from tool import Tool
from drill import Drill

class DrillingTool(Tool):
    def __init__(self, manufacturer, model, diameter):
        super().__init__(manufacturer, model)
        self.__diameter = diameter # This is in mm
        self.__attached_to = None

    def detach(self):
        self.__attached_to = None

    def __attach(self, drill:Drill):
        self.__attached_to = drill

    def try_attaching(self, drill:Drill):
        if drill.connector_size >= self.__diameter:
            if drill.attached_bit is None:
                drill.change_bit(self)
                self.__attach(drill)
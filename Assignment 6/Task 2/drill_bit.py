from drilling_tool import DrillingTool
from cordless_drill import CordlessDrill

class DrillBit(DrillingTool):
    def __init__(self, manufacturer, model, diameter, max_rpm):
        super().__init__(manufacturer, model, diameter, max_rpm)

    def use(self):
        drill = self.attached_to

        if drill is not None:
            if drill is CordlessDrill:
                if drill.has_battery():
                    print("Using!")
                    drill.use_battery(1)

            else:
                print("Using!")
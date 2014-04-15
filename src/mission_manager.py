#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from src.missions import *

class MissionManager:

    def __init__(self):
        # TODO these missions are hard coded; should read from file or something?
        self.get_hardcoded_missions()
        self.current_mission = self.missions[0]

    def get_hardcoded_missions(self):
        mission1 = Mission1()
        mission2 = Mission2()
        self.missions = [mission1, mission2]

    def info(self):
        return str(self.current_mission)

    def update(self, controller):
        if self.current_mission.complete(controller):
            self.missions.pop(0)
            if not self.missions:
                return True
            else:
                self.current_mission = self.missions[0]
        return False

#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from src.missions import *

class MissionManager:

    def __init__(self, controller):
        # TODO these missions are hard coded; should read from file or something?
        self.controller = controller
        self.get_hardcoded_missions()
        self.current_mission = self.missions[0]
        

    def get_hardcoded_missions(self):
        mission1 = Mission1(self.controller)
        mission2 = Mission2(self.controller)
        self.missions = [mission1, mission2]

    def info(self):
        return str(self.current_mission)

    def startup(self):
        print("\tWelcome to Bashyland!\n")
        print("\n\t" + self.current_mission.title + ":")
        print("\t" + self.current_mission.intro)
        print("\t" + self.current_mission.description + "\n")

    def update(self):
        if self.current_mission.complete():
            print("\n\t" + self.current_mission.completion_message)
            self.missions.pop(0)
            if not self.missions:
                return True
            else:
                self.current_mission = self.missions[0]
                print("\n\t" + self.current_mission.title + ":")
                print("\t" + self.current_mission.intro)
                print("\t" + self.current_mission.description + "\n")
        return False

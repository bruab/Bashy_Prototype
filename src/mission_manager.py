#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from src.mission import Mission

class MissionManager:

    def __init__(self):
        mission1 = Mission()
        mission1dict = {"history": [], "filesystem": [["pwd", "/home/brian"]]}
        mission1.goals = mission1dict
        mission2 = Mission()
        mission2dict = {"history": [["get_last", "pwd"]], "filesystem": []}
        mission2.goals = mission2dict
        self.missions = [mission1, mission2]

    def next(self):
        if self.missions:
            return self.missions.pop(0)
        else:
            return None


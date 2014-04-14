#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from src.mission import Mission

class MissionManager:

    def __init__(self):
        mission = Mission()
        missiondict = {"history": [], "filesystem": [["pwd", "/home/brian"]]}
        mission.goals = missiondict
        self.missions = [mission]


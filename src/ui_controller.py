#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from src.filesystem import FileSystem
from src.history import History
from src.mission import Mission

class UIController:

    def __init__(self):
        self.filesystem = FileSystem()
        self.history = History()
        self.mission = Mission()
        missiondict = {"history": [], "filesystem": [["pwd", "/home/brian"]]}
        self.mission.goals = missiondict

    def complete(self):
        return self.mission.complete(self.history, self.filesystem)

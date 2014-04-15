#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from src.history import History
from src.filesystem import FileSystem


class BashyController():

    def __init__(self):
        self.history = History()
        self.filesystem = FileSystem()

    def pwd(self):
        return self.filesystem.pwd()

    def cd(self, path):
        self.filesystem.cd(path)

    def get_last_n_commands(self, number):
        return self.history.get_last_n_commands(number)

    def add_history_line(self, line):
        self.history.add_line(line)

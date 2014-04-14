#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4


class History:

    def __init__(self, commands=None):
        if not commands:
            commands = []
        self.commands = commands

    def get_last(self):
        if self.commands:
            return self.commands[-1]

    def add_line(self, line):
        self.commands.append(line)

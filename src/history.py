#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

def format_list(items):
    if not items:
        return ""
    elif len(items) == 1:
        return items[0] + "\n"
    else:
        result = ""
        for item in items[:-1]:
            result += item + "\n"
        result += items[-1]
        return result

class History:

    def __init__(self, commands=None):
        if not commands:
            commands = []
        self.commands = commands

    def get_last_n_commands(self, number):
        if len(self.commands) < number:
            return self.commands
        else:
            return self.commands[-number:]

    def get_last_n_formatted(self, number):
        if len(self.commands) < number:
            return format_list(self.commands)
        else:
            return format_list(self.commands[-number:])

    def add_line(self, line):
        self.commands.append(line)

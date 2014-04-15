#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4


class Mission:

    def __init__(self):
        self.title = ""
        self.description = ""
        self.little_hint = ""
        self.big_hint = ""

    def __str__(self):
        return self.description

    def complete(self, controller):
        return True

class Mission1(Mission):
    def __init__(self):
        self.title = "Mission 1"
        self.description = "Find out where you are with the 'pwd' command."
        self.little_hint = "Use the command in the description ..."
        self.big_hint = "Type 'pwd' and press enter."

    def complete(self, controller):
        last_command = controller.get_last_n_commands(1)[0]
        if last_command == "pwd":
            return True
        else:
            return False

class Mission2(Mission):
    def __init__(self):
        self.title = "Mission 2"
        self.description = "Navigate to /home/brian/foo"
        self.little_hint = "Use the command 'cd' plus the directory you want to go to."
        self.big_hint = "Type 'cd /home/brian/foo'"

    def complete(self, controller):
        if controller.pwd() == "/home/brian/foo":
            return True
        else:
            return False


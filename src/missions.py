#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4


class Mission:

    def __init__(self, controller):
        self.title = ""
        self.intro = ""
        self.description = ""
        self.little_hint = ""
        self.big_hint = ""
        self.completion_message = "You did it!"
        self.controller = controller

    def __str__(self):
        return self.description

    def complete(self):
        return True

class Mission1(Mission):
    def __init__(self, controller):
        Mission.__init__(self, controller)
        self.title = "Mission 1"
        self.intro = "First let's learn about this new place."
        self.description = "Find out where you are with the 'pwd' command."
        self.little_hint = "Use the command in the description ..."
        self.big_hint = "Type 'pwd' and press enter."
        self.completion_message = "Nice! The 'pwd' command will always tell you your current location."

    def complete(self):
        last_command = self.controller.get_last_n_commands(1)[0]
        if last_command == "pwd":
            return True
        else:
            return False

class Mission2(Mission):
    def __init__(self, controller):
        Mission.__init__(self, controller)
        self.title = "Mission 2"
        self.intro = "Now it's time to move around a little bit."
        self.description = "Navigate to /home/" + self.controller.username + "/foo using the 'cd' command."
        self.little_hint = "Use the command 'cd' plus the directory you want to go to."
        self.big_hint = "Type 'cd /home/brian/foo'"
        self.completion_message = "Very good! Now you know how to move around."

    def complete(self):
        if self.controller.pwd() == "/home/" + self.controller.username + "/foo":
            return True
        else:
            return False

class Mission3(Mission):
    def __init__(self, controller):
        Mission.__init__(self, controller)
        self.title = "Mission 3"
        self.intro = "This 'foo' directory is boring. Let's go back."
        self.description = "Navigate back to /home/" + self.controller.username + "/foo " +\
                           "by using two periods ('..') and the 'cd' command."
        self.little_hint = "Use the command 'cd' plus '..' to go to the parent directory."
        self.big_hint = "Type 'cd ..'"
        self.home = "/home/" + self.controller.username

    def complete(self):
        last_command = self.controller.get_last_n_commands(1)[0]
        current_dir = self.controller.pwd()
        if last_command == "cd .." and current_dir == self.home: 
            return True
        else:
            return False

class Mission4(Mission):
    def __init__(self, controller):
        Mission.__init__(self, controller)
        self.title = "Mission 4"
        self.intro = "Let's keep exploring."
        self.description = "Use 'cd ..' and 'pwd' to reach the highest directory you can get to."
        self.little_hint = "Type 'cd ..' to go up one directory, then 'pwd' to see what directory you're in."
        self.big_hint = "Type 'cd ..' then 'pwd' over and over :)"
        self.completion_message = "Nice! The topmost directory is just called '/'. You can also call it 'root'.\n"

    def complete(self):
        last_command = self.controller.get_last_n_commands(1)[0]
        current_dir = self.controller.pwd()
        if last_command == "pwd" and current_dir == "/":
            return True
        else:
            return False


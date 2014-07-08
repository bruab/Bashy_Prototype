#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from src.mission_manager import MissionManager
from src.bashy_controller import BashyController
from art.ascii_art import *
import cmd


class BashyCmd(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.controller = BashyController()
        self.mission_manager = MissionManager(self.controller)
        self.prompt = "Bashy> "
        print(bashy_logo)
        self.mission_manager.startup()

    def precmd(self, line):
        self.controller.add_history_line(line)
        return cmd.Cmd.precmd(self, line)

    def postcmd(self, stop, line):
        if self.mission_manager.update():
            print("\tYou win.")
            return True
        else:
            return stop

    def do_exit(self, line):
        return True

    def do_info(self, line):
        print(self.mission_manager.info())

    def do_pwd(self, line):
        print(self.controller.pwd())

    def do_cd(self, line):
        self.controller.cd(line)

    def do_history(self, line):
        print(self.controller.get_last_n_commands(20))


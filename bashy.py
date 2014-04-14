#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import cmd
from src.ui_controller import UIController


class BashyCmd(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "Bashy> "
        self.controller = UIController() 

    def do_exit(self):
        return True

    def do_complete(self, line):
        print(self.controller.complete())

########################################################################

if __name__ == '__main__':
    BashyCmd().cmdloop("Welcome to Bashy!")

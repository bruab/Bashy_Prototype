#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import cmd


class BashyCmd(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "Bashy> "

    def do_exit(self, line):
        return True


########################################################################

if __name__ == '__main__':
    BashyCmd().cmdloop("Welcome to Bashy!")

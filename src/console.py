#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from src.mission_manager import MissionManager
from src.history import History
from src.filesystem import FileSystem
import cmd


class BashyCmd(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.history = History()
        self.filesystem = FileSystem()
        self.mission_manager = MissionManager()
        self.current_mission = self.mission_manager.next_mission()
        self.prompt = "Bashy> "

    def precmd(self, line):
        self.history.add_line(line)
        return cmd.Cmd.precmd(self, line)

    def postcmd(self, stop, line):
        if self.current_mission.complete(self.history, self.filesystem):
            self.current_mission = self.mission_manager.next_mission()
            if not self.current_mission:
                print("Congratulations, you win.")
                return True


    def do_exit(self, line):
        return True

    def do_info(self, line):
        print(self.current_mission)

    def do_pwd(self, line):
        print(self.filesystem.pwd())

    def do_cd(self, line):
        self.filesystem.cd(line)

    def do_history(self, line):
        self.history.get_last_n(20)

########################################################################

if __name__ == '__main__':
    BashyCmd().cmdloop("Welcome to Bashy!")

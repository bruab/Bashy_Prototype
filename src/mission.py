#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4


class Mission:

    def __init__(self, goals=None):
        if not goals:
            goals = {}
        self.goals = goals

    def __str__(self):
        return(str(self.goals))

    def complete(self, history, filesystem):
        for command in self.goals["history"]:
            method = getattr(history, command[0])
            expected_result = command[1]
            if method() != expected_result:
                return False
        for command in self.goals["filesystem"]:
            method = getattr(filesystem, command[0])
            expected_result = command[1]
            if method() != expected_result:
                return False
        return True


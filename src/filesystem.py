#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4


class FileSystem:

    def __init__(self):
        self.current_directory = "/home/brian"

    def pwd(self):
        return self.current_directory

    def cd(self, path):
        self.current_directory = path

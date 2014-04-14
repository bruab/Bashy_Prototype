#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from src.filesystem import FileSystem

class UIController:

    def __init__(self):
        self.filesystem = FileSystem()


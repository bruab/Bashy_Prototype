#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4


class File:

    def __init__(self, name="", parent=None, owner="", group="",
            permissions="", directory=False, data=None):
        self.name = name
        self.parent = parent
        self.owner = owner
        self.group = group
        self.permissions = permissions
        self.directory = directory
        self.data = data

    def get_absolute_path(self):
        at_root = False
        current_dir = self
        dirs = [self.name]
        while not at_root:
            if current_dir.parent:
                current_dir = current_dir.parent
                dirs.append(current_dir.name)
            else:
                at_root = True
        path = "/".join(dirs[::-1])
        return path[1:]  # Remove double slash at beginning



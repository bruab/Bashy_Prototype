#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from collections import namedtuple

File = namedtuple('File', 'owner group permissions directory data')

class FileSystem:


    def __init__(self):
        # TODO build the whole tree :)
        self.current_directory = "/home/brian" # This is just a string!
        self.files = self.initialize_filesystem()

    def pwd(self):
        return self.current_directory

    def cd(self, path):
        # TODO actually use self.files! This is just a string.
        self.current_directory = path

    def initialize_filesystem(self):
        # TODO naming scheme for File tuples
        Bin = File('root', 'root', '755', True, {})
        foo = File('brian', 'users', '755', True, {})
        sample_text = File('brian', 'users', '755', False, "This is some sample text")
        brian = File('brian', 'users', '755', True, {'foo': foo, 'sample.txt': sample_text})
        Home = File('root', 'root', '755', True, {'brian': brian})
        self.root = File('root', 'root', '755', True, {'home': Home, 'bin': Bin})

    def exists(self, path):
        directories = path.split("/")
        parent = self.root
        for subdirectory in directories[1:]:
            if not subdirectory in parent.data.keys():
                return False
            parent = parent.data[subdirectory]
        return True


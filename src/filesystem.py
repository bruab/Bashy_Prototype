#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import sys
from src.files import File

class FileSystem:


    def __init__(self, name):
        self.initialize_filesystem(name)

    def pwd(self):
        return self.current_directory.get_absolute_path()

    def cd(self, path):
        if path == "..":
            if self.current_directory.parent:
                self.current_directory = self.current_directory.parent
        elif path == ".":
            return
        elif path == "/":
            self.current_directory = self.root
        elif path.startswith("/"):
            # Absolute path
            dirs = path.strip().split("/")[1:]
            current_dir = self.root
            for dirname in dirs:
                if dirname not in current_dir.data:
                    sys.stderr.write("Invalid path: " + path + "\n")
                    return
                else:
                    current_dir = current_dir.data[dirname]
            self.current_directory = current_dir
        else:
            # Relative path
            dirs = path.strip().split("/")
            current_dir = self.current_directory
            for dirname in dirs:
                if dirname not in current_dir.data:
                    sys.stderr.write("Invalid path: " + path + "\n")
                    return
                else:
                    current_dir = current_dir.data[dirname]
            self.current_directory = current_dir



    def initialize_filesystem(self, name):
        # TODO naming scheme for File tuples
        # TODO tests depend on this particular filesystem, and so does game.
        # all this should live in a text file or something ...
        Bin = File('bin', None, 'root', 'root', '755', True, {})
        foo = File('foo', None, name, 'users', '755', True, {})
        sample_text = File('sample.txt', None, name, 'users', '755', False, "This is some sample text")
        user_home = File(name, None, name, 'users', '755', True, {'foo': foo, 'sample.txt': sample_text})
        Home = File('home', None, 'root', 'root', '755', True, {name: user_home})
        self.root = File('/', None, 'root', 'root', '755', True, {'home': Home, 'bin': Bin})
        Home.parent = self.root
        user_home.parent = Home
        Bin.parent = self.root
        foo.parent = user_home
        sample_text.parent = user_home
        self.current_directory = user_home 

    def exists(self, path):
        directories = path.split("/")
        parent = self.root
        for subdirectory in directories[1:]:
            if not subdirectory in parent.data:
                return False
            parent = parent.data[subdirectory]
        return True


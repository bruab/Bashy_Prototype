#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from src.files import File

class FileSystem:


    def __init__(self):
        self.initialize_filesystem()

    def pwd(self):
        return self.current_directory.get_absolute_path()

    def cd(self, path):
        if path.startswith("/"):
            # Absolute path
            dirs = path.strip().split("/")[1:]
            current_dir = self.root
            for dirname in dirs:
                if dirname not in current_dir.data:
                    sys.stderr.write("Invalid path: " + path)
                    return
                else:
                    current_dir = current_dir.data[dirname]
            self.current_directory = current_dir
        elif path == "..":
            self.current_directory = self.current_directory.parent

    def initialize_filesystem(self):
        # TODO naming scheme for File tuples
        Bin = File('bin', None, 'root', 'root', '755', True, {})
        foo = File('foo', None, 'brian', 'users', '755', True, {})
        sample_text = File('sample.txt', None, 'brian', 'users', '755', False, "This is some sample text")
        brian = File('brian', None, 'brian', 'users', '755', True, {'foo': foo, 'sample.txt': sample_text})
        Home = File('home', None, 'root', 'root', '755', True, {'brian': brian})
        self.root = File('/', None, 'root', 'root', '755', True, {'home': Home, 'bin': Bin})
        Home.parent = self.root
        brian.parent = Home
        Bin.parent = self.root
        foo.parent = brian
        sample_text.parent = brian
        self.current_directory = brian

    def exists(self, path):
        directories = path.split("/")
        parent = self.root
        for subdirectory in directories[1:]:
            if not subdirectory in parent.data:
                return False
            parent = parent.data[subdirectory]
        return True


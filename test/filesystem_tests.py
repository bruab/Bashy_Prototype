#!/usr/bin/env python

import  unittest
from src.filesystem import FileSystem

class TestFileSystem(unittest.TestCase):

    def setUp(self):
        self.filesystem = FileSystem()

    def test_pwd(self):
        self.assertEquals("/home/brian", self.filesystem.pwd())

    def test_cd(self):
        self.assertEquals("/home/brian", self.filesystem.current_directory)
        self.filesystem.cd("/home")
        self.assertEquals("/home", self.filesystem.current_directory)

        


##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFileSystem))
    return suite

if __name__ == '__main__':
    unittest.main()

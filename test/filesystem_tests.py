#!/usr/bin/env python

import  unittest
from src.filesystem import FileSystem

class TestFileSystem(unittest.TestCase):

    def setUp(self):
        self.filesystem = FileSystem()

    def test_pwd(self):
        self.assertEquals("/home/brian", self.filesystem.pwd())
        pass

    def test_cd(self):
        self.assertEquals("brian", self.filesystem.current_directory.name)
        self.assertEquals("/home/brian", self.filesystem.current_directory.get_absolute_path())
        self.filesystem.cd("/home")
        self.assertEquals("home", self.filesystem.current_directory.name)

    def test_cd_to_parent(self):
        #self.assertEquals("/home/brian", self.filesystem.current_directory)
        self.filesystem.cd("..")
        #self.assertEquals("/home", self.filesystem.current_directory)

    def test_exists(self):
        test_path = "/home/brian"
        self.assertTrue(self.filesystem.exists(test_path))

    def test_exists_file(self):
        test_path = "/home/brian/sample.txt"
        self.assertTrue(self.filesystem.exists(test_path))
        


##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFileSystem))
    return suite

if __name__ == '__main__':
    unittest.main()

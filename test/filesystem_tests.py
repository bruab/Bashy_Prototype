#!/usr/bin/env python

import  unittest
from src.filesystem import FileSystem

class TestFileSystem(unittest.TestCase):

    def setUp(self):
        self.ctrlr = FileSystem()


##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFileSystem))
    return suite

if __name__ == '__main__':
    unittest.main()

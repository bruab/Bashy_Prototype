#!/usr/bin/env python

import  unittest
from src.files import File

class TestFile(unittest.TestCase):

    def setUp(self):
        self.parentfile = File(name="/", parent=None)
        self.childfile = File(name="home", parent=self.parentfile)
        self.grandchildfile = File(name="brian", parent=self.childfile)

    def test_get_absolute_path(self):
        self.assertEqual("/home", self.childfile.get_absolute_path())
        self.assertEqual("/home/brian", self.grandchildfile.get_absolute_path())



##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFile))
    return suite

if __name__ == '__main__':
    unittest.main()

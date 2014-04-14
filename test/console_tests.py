#!/usr/bin/env python

import  unittest
from src.console import BashyCmd

class TestConsole(unittest.TestCase):

    def setUp(self):
        self.cmd = BashyCmd()


##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestConsole))
    return suite

if __name__ == '__main__':
    unittest.main()

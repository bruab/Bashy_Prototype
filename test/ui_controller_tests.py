#!/usr/bin/env python

import  unittest
from src.ui_controller import UIController

class TestUIController(unittest.TestCase):

    def setUp(self):
        self.ctrlr = UIController()

    def test_constructor(self):
        self.assertTrue(self.ctrlr.filesystem)


##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestUIController))
    return suite

if __name__ == '__main__':
    unittest.main()

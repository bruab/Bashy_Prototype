#!/usr/bin/env python

import  unittest
from mock import Mock
from src.ui_controller import UIController

class TestUIController(unittest.TestCase):

    def setUp(self):
        self.ctrlr = UIController()

    def test_constructor(self):
        self.assertTrue(self.ctrlr.filesystem)
        self.assertTrue(self.ctrlr.history)

    def test_complete(self):
        self.ctrlr.mission = Mock()
        self.ctrlr.complete()
        self.ctrlr.mission.complete.assert_called_with(self.ctrlr.history, self.ctrlr.filesystem)


##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestUIController))
    return suite

if __name__ == '__main__':
    unittest.main()

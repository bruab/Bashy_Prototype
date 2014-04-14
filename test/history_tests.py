#!/usr/bin/env python

import  unittest
from src.history import History

class TestHistory(unittest.TestCase):

    def setUp(self):
        self.history = History()

    def test_get_last(self):
        self.history.commands = ["pwd", "foo"]
        self.assertEquals("foo", self.history.get_last())


##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestHistory))
    return suite

if __name__ == '__main__':
    unittest.main()

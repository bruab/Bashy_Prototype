#!/usr/bin/env python

import  unittest
from src.history import History

class TestHistory(unittest.TestCase):

    def setUp(self):
        self.history = History()

    def test_get_last(self):
        self.history.commands = ["pwd", "foo"]
        self.assertEquals("foo", self.history.get_last())

    def test_get_last_if_history_empty(self):
        # Shouldn't throw exception
        actual = self.history.get_last()
        self.assertFalse(actual)

    def test_add_line(self):
        self.assertEquals(0, len(self.history.commands))
        self.history.add_line("foo line")
        self.assertEquals(1, len(self.history.commands))


##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestHistory))
    return suite

if __name__ == '__main__':
    unittest.main()

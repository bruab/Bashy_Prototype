#!/usr/bin/env python

import  unittest
from src.history import History

class TestHistory(unittest.TestCase):

    def setUp(self):
        self.history = History()

    def test_get_last_n_commands(self):
        self.history.commands = ["foo1", "foo2", "foo3"]
        expected = ["foo2", "foo3"]
        self.assertEquals(expected, self.history.get_last_n_commands(2))

    def test_get_last_n_formatted(self):
        self.history.commands = ["foo1", "foo2", "foo3"]
        expected = "foo1\nfoo2\nfoo3"
        self.assertEquals(self.history.get_last_n_formatted(3), expected)

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

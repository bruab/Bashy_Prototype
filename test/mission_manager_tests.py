#!/usr/bin/env python

import  unittest
from src.mission_manager import MissionManager

class TestMissionManager(unittest.TestCase):

    def setUp(self):
        self.mgr = MissionManager()

    def test_constructor(self):
        self.assertTrue(self.mgr.missions)

    def test_next_mission(self):
        # TODO for now mission manager is hardcoded to contain two tests ...
        self.assertTrue(self.mgr.next_mission())
        self.assertTrue(self.mgr.next_mission())
        self.assertFalse(self.mgr.next_mission())


##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMissionManager))
    return suite

if __name__ == '__main__':
    unittest.main()

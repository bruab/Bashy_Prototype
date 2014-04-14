#!/usr/bin/env python

import  unittest
from mock import Mock
from src.mission import Mission

class TestMission(unittest.TestCase):

    def setUp(self):
        self.mission = Mission()

    def setup_mission_goals(self):
        missiondict = {"history": [], "filesystem": [["pwd", "/home/brian"]]}
        self.mission.goals = missiondict

    def test_complete(self):
        self.setup_mission_goals()
        mockhistory = Mock()
        mockfilesystem = Mock()
        mockfilesystem.pwd.return_value = "/home/brian"
        self.assertTrue(self.mission.complete(mockhistory, mockfilesystem))

    def test_str(self):
        self.setup_mission_goals()
        expected = "{'filesystem': [['pwd', '/home/brian']], 'history': []}"
        self.assertEquals(str(self.mission), expected)


##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMission))
    return suite

if __name__ == '__main__':
    unittest.main()

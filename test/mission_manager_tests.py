#!/usr/bin/env python

import  unittest
from mock import Mock
from src.mission_manager import MissionManager

class TestMissionManager(unittest.TestCase):

    def setUp(self):
        self.mgr = MissionManager()

    def test_constructor(self):
        self.assertTrue(self.mgr.missions)
        self.assertTrue(self.mgr.current_mission)

    def test_info(self):
        self.assertEquals("Find out where you are with the 'pwd' command.", self.mgr.info())

    def test_update(self):
        mock_ctrlr = Mock()
        mock_mission = Mock()
        mock_mission.complete.return_value = False
        self.mgr.current_mission = mock_mission
        self.assertFalse(self.mgr.update(mock_ctrlr))
        mock_mission.complete.assert_called_with(mock_ctrlr)

    def test_update_true(self):
        mock_ctrlr = Mock()
        mock_mission = Mock()
        mock_mission.complete.return_value = True
        mock_mission.completion_message = ""
        self.mgr.missions = [mock_mission]
        self.mgr.current_mission = mock_mission
        self.assertTrue(self.mgr.update(mock_ctrlr))


##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMissionManager))
    return suite

if __name__ == '__main__':
    unittest.main()

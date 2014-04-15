#!/usr/bin/env python

import  unittest
from mock import Mock
from src.missions import * 

class TestMission(unittest.TestCase):

    def setUp(self):
        self.mission = Mission()

    def test_mission_1(self):
        mission1 = Mission1()
        mock_ctrlr = Mock()
        mock_ctrlr.get_last_n_commands.return_value = ["rm -rf /"]
        self.assertFalse(mission1.complete(mock_ctrlr))
        mock_ctrlr.get_last_n_commands.return_value = ["pwd"]
        self.assertTrue(mission1.complete(mock_ctrlr))
        mock_ctrlr.get_last_n_commands.assert_called_with(1)

    def test_mission_2(self):
        mission2 = Mission2()
        mock_ctrlr = Mock()
        mock_ctrlr.pwd.return_value = "/home/brian"
        self.assertFalse(mission2.complete(mock_ctrlr))
        mock_ctrlr.pwd.return_value = "/home/brian/foo"
        self.assertTrue(mission2.complete(mock_ctrlr))


##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMission))
    return suite

if __name__ == '__main__':
    unittest.main()

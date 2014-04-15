#!/usr/bin/env python

# import all the lovely files
import unittest
import test.console_tests
import test.filesystem_tests
import test.mission_tests
import test.mission_manager_tests
import test.history_tests
import test.bashy_controller_tests

# get suites from test modules
suite1 = test.console_tests.suite()
suite2 = test.filesystem_tests.suite()
suite3 = test.mission_tests.suite()
suite4 = test.mission_manager_tests.suite()
suite5 = test.history_tests.suite()
suite6 = test.bashy_controller_tests.suite()

# collect suites in a TestSuite object
suite = unittest.TestSuite()
suite.addTest(suite1)
suite.addTest(suite2)
suite.addTest(suite3)
suite.addTest(suite4)
suite.addTest(suite5)
suite.addTest(suite6)

# run suite
unittest.TextTestRunner(verbosity=2).run(suite)

#!/usr/bin/env python

# import all the lovely files
import unittest
import test.ui_controller_tests

# get suites from test modules
suite1 = test.ui_controller_tests.suite()

# collect suites in a TestSuite object
suite = unittest.TestSuite()
suite.addTest(suite1)

# run suite
unittest.TextTestRunner(verbosity=2).run(suite)

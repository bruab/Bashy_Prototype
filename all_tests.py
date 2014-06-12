#!/usr/bin/env python

# import all the lovely files
import unittest
import test.console_tests
import test.filesystem_tests
import test.mission_tests
import test.mission_manager_tests
import test.history_tests
import test.bashy_controller_tests
import test.files_tests

# get suites from test modules
allsuites = [
test.console_tests.suite(),
test.filesystem_tests.suite(),
test.mission_tests.suite(),
test.mission_manager_tests.suite(),
test.history_tests.suite(),
test.bashy_controller_tests.suite(),
test.files_tests.suite()
]

# collect suites in a TestSuite object
suite = unittest.TestSuite()
for testsuite in allsuites:
    suite.addTest(testsuite)

# run suite
unittest.TextTestRunner(verbosity=2).run(suite)

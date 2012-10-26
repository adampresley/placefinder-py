import unittest, sys

sys.path.insert(0, "../")
sys.path.insert(0, "../tests")

import tests.placefindertests as placefindertests

suites = [
	placefindertests.suite()
]

completeSuite = unittest.TestSuite()

for suite in suites:
	completeSuite.addTest(suite)

#
# Run all tests
#
unittest.TextTestRunner(verbosity = 2, failfast = True).run(completeSuite)

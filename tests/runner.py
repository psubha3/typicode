import unittest

from test_verify_get_users import GetUsersMethods
from test_verify_post_of_given_user import UserPostMethods

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

suite.addTests(loader.loadTestsFromTestCase(GetUsersMethods))
suite.addTest(loader.loadTestsFromTestCase(UserPostMethods))


runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)


import unittest
from HtmlTestRunner import HTMLtestRunner

from test_verify_get_users import GetUsersMethods
from test_verify_post_of_given_user import UserPostMethods

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

suite.addTests(loader.loadTestsFromTestCase(GetUsersMethods))
suite.addTest(loader.loadTestsFromTestCase(UserPostMethods))


runner = unittest.TextTestRunner(verbosity=3)
outfile = file('Report.html', 'w')
runner = HTMLTestRunner(stream=outfile,
                            verbosity=2,
                            title='Typicode api Report',
                            description='This is test result of typicode api')
result = runner.run(suite)


import unittest
import jsonpath

from create_base_session import SessionWithUrlBase
from helper import get_response_for_given_path


class GetUsersMethods(unittest.TestCase):

    session = None

    @classmethod
    def setUp(cls):
        """
        Creates the session for https://jsonplaceholder.typicode.com
        Assign a value to username
        """
        base_session = SessionWithUrlBase('https://jsonplaceholder.typicode.com')
        cls.session = base_session
        cls.get_users_api = "/users"
        cls.search_username = 'Samantha'
        cls.username_path = '$..username'
        cls.userid_path = '$..id'

    def test_01_verify_get_user(self):
        """
        1. makes a GET users api call
        1. Validates if the response code returned is 200
        2. Validates if the response received is not an empty list.
        """
        print("Verify get users api")
        response = self.session.typicode_get_api(self.get_users_api)
        self.assertEqual(response.status_code, 200, "Received status code " + str(response.status_code) +
                         " instead of 200")
        self.assertNotEqual(len(response.json()), 0, "No users available")

    def test_02_get_api_with_user_username(self):
        """
        1. Calls get api with username query
        2. Validates if response code returned is 200
        3. Validates if response received is not an empty list
        4. Validates if the path is present in the given response
        5. Validates if the path value is same as our search value
        """
        print("Verify get users api with username")
        response = self.session.typicode_get_api_with_query(self.get_users_api, 'username=' + self.search_username)
        self.assertEqual(response.status_code, 200, "Received status code " + str(response.status_code) +
                         " instead of 200")
        self.assertNotEqual(len(response.json()), 0, "No response received")
        username_response = get_response_for_given_path(response.json(), self.username_path)
        self.assertNotEquals(username_response, False, "Searched string is not present")
        self.assertItemsEqual(username_response, [self.search_username],
                              "Username " + self.search_username + "is not present in the response")

    def test_03_retrieve_and_store_userid_of_specific_user(self):
        print("Store the user id received from the get user api response")
        response = self.session.typicode_get_api_with_query(self.get_users_api, 'username=' + self.search_username)
        self.assertEqual(response.status_code, 200, "Received status code " + str(response.status_code) +
                         " instead of 200")
        self.assertNotEqual(len(response.json()), 0, "No response received")
        username_response = get_response_for_given_path(response.json(), self.username_path)
        self.assertNotEquals(username_response, False, "Searched string is not present")
        self.assertItemsEqual(username_response, [self.search_username],
                              "Username " + self.search_username + "is not present in the response")
        userid_response = get_response_for_given_path(response.json(), self.userid_path)
        self.assertNotEquals(userid_response, False, "Searched string is not present")

    @classmethod
    def tearDown(cls):
        cls.session.close_typicode_session()


if __name__ == '__main__':
    unittest.main()


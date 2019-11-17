import unittest

from create_base_session import SessionWithUrlBase
from helper import get_response_for_given_path, check_given_value_present_in_list


class GetUsersMethods(unittest.TestCase):

    session = None

    @classmethod
    def setUp(cls):
        """
        Creates the session for https://jsonplaceholder.typicode.com
        Assign a value to username, json query path to extract values.
        """
        base_session = SessionWithUrlBase('https://jsonplaceholder.typicode.com')
        cls.session = base_session
        cls.get_users_api = "/users"
        cls.search_username = 'Samantha'
        cls.search_username_key = '$..username'

    def test_01_verify_if_given_user_is_present(self):
        """
        1. Makes a GET users api call
        2. Validates if the response code returned is 200
        3. Validates if the response received is not an empty list
        4. Validates if the username key is present in response
        5. Check if the given user is present in response
        """
        print("Verify if given user is present")
        response = self.session.typicode_get_api(self.get_users_api)

        # Validates if response code is 200
        self.assertEqual(response.status_code, 200, "Received status code " + str(response.status_code) +
                         " instead of 200")

        # Validates if response is not empty
        self.assertNotEqual(len(response.json()), 0, "User response is empty")

        # Validates if the username key is present in response
        username_response = get_response_for_given_path(response.json(), self.search_username_key)
        self.assertNotEquals(username_response, False, "Searched string is not present")

        # Validates if the given username is present in response
        user_present = check_given_value_present_in_list(username_response, self.search_username)
        self.assertTrue(user_present, "Username " + self.search_username + "is not present in the response")

    def test_02_get_api_with_user_username(self):
        """
        1. Calls get api with username query
        2. Validates if response code returned is 200
        3. Validates if response received is not an empty list
        4. Validates if the username key is present in response
        5. Check if the given user is present in response
        """
        print("Verify get users api with username query")
        response = self.session.typicode_get_api_with_query(self.get_users_api, 'username=' + self.search_username)
        # Validates if response code is 200
        self.assertEqual(response.status_code, 200, "Received status code " + str(response.status_code) +
                         " instead of 200")

        # Validates if response is not empty
        self.assertNotEqual(len(response.json()), 0, "User response is empty")

        # Validates if the username key is present in response
        username_response = get_response_for_given_path(response.json(), self.search_username_key)
        self.assertNotEquals(username_response, False, "Searched string is not present")

        # Validates if the given username is present in response
        user_present = check_given_value_present_in_list(username_response, self.search_username)
        self.assertTrue(user_present, "Username " + self.search_username + "is not present in the response")

    @classmethod
    def tearDown(cls):
        cls.session.close_typicode_session()


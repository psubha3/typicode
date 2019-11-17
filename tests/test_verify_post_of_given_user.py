import unittest

from create_base_session import SessionWithUrlBase
from helper import get_response_for_given_path, check_given_value_present_in_list, \
    get_first_user_id_from_users_response, \
    get_all_post_ids_of_given_userid


class UserPostMethods(unittest.TestCase):
    session = None

    def setUp(self):
        """
        Creates the session for https://jsonplaceholder.typicode.com
        Makes a get users api call
        Validates if response is 200
        Validates if response is not empty
        Validates if the username key is present
        Get the userid of the give user and stores in a variable
        """
        base_session = SessionWithUrlBase('https://jsonplaceholder.typicode.com')
        self.session = base_session
        self.get_users_api = "/users"
        self.get_post_api = "/posts"
        self.search_username = 'Samantha'
        self.search_username_key = '$..username'
        self.search_userid_key = '$..id'
        self.search_post_userId = '$..userId'
        self.search_post_id = '$..id'
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
        self.assertTrue(user_present, "Username " + self.search_username + " is not present in the response")

        # Gets the user-id of the given user
        userid = get_first_user_id_from_users_response(response.json(), self.search_username_key,
                                                       self.search_userid_key, self.search_username)
        self.assertNotEquals(userid, 0, "Value is not present in list")
        self.userid = userid

    def test_01_get_postid_of_given_user(self):
        """
        1. Makes a GET api call to get the posts made by users
        2. Validates if the response code returned is 200
        3. Validates if the response received is not an empty list
        4. Validates if the postid key is present in response
        5. Check if the  is present in response
        """
        print("Get ids of post made by a specific user")
        post_response = self.session.typicode_get_api(self.get_post_api)

        # Validates if response code is 200
        self.assertEqual(post_response.status_code, 200, "Received status code " + str(post_response.status_code) +
                         " instead of 200")

        # Validates if response is not empty
        self.assertNotEqual(len(post_response.json()), 0, "User response is empty")

        # Validates if the userid key is present in response
        userid_response = get_response_for_given_path(post_response.json(), self.search_post_userId)
        self.assertNotEquals(userid_response, False, "Searched id is not present")

        # Validates if the given userid is present in response
        print("Check if given userId is present in list")
        user_present = check_given_value_present_in_list(userid_response, self.userid)
        self.assertTrue(user_present, "User ID " + str(self.userid) + " is not present in the response")

        specific_user_post_ids = get_all_post_ids_of_given_userid(post_response.json(), self.search_post_userId,
                                                                  self.search_post_id, self.userid)
        print("User " + self.search_username + " have made post with the given list of Ids" + str(
            specific_user_post_ids))

    def tearDown(self):
        self.session.close_typicode_session()




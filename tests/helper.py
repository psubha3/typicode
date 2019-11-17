import jsonpath


def get_response_for_given_path(json_response, path):
    """
    Extracts the json response matching the given path.
    :param json_response: json response of any api request
    :param path: path to search for in given response
    :return: returns the list of matching response. If not present return False
    """
    match_response = jsonpath.jsonpath(json_response, path)
    return match_response


def check_given_value_present_in_list(listitem, search_string):
    """
    Search the given value is present in the list.
    :param listitem: list of values
    :param search_string: item to search from the list
    :return: True if the value is present else False
    """
    if listitem.count(search_string):
        print(str(search_string) + " is present in the list")
        return True
    else:
        print(str(search_string) + " is not present in the list")
        return False


def get_first_user_id_from_users_response(json_response, user_name_key_path, userid_key_path, search_username):
    """
    Extracts the jsonresponse with username key path, gets the index of it to get the userid of the corresponding user.
    :param json_response: json response of any api response
    :param user_name_key_path: $..username - used to get the value matching the path
    :param userid_key_path: $..id - Used to get the values matching the given path
    :param search_username: username to search in the response and get its id
    :return:
    """
    print("Get Users response: " + str(json_response))
    username_list = get_response_for_given_path(json_response, user_name_key_path)
    print("Username List :" + str(username_list))
    userid_list = get_response_for_given_path(json_response, userid_key_path)
    print("User Id List:" + str(userid_list))
    try:
        username_index = username_list.index(search_username)
        print(search_username + " is present in index " + str(username_index))
        userid = userid_list[username_index]
        print("Userid of " + search_username + " is " + str(userid))
        return userid
    except ValueError:
        return 0


def get_all_post_ids_of_given_userid(json_response, user_id_key_path, postid_key_path, search_userid):
    """
    Gets list based on the user_id path and postid path.
    Filters the user id that matches the given string and gets all of its index
    Use this index to fetch the corresponding value from the postid.
    ll the postid matching the given user id.
    :param json_response: json response received from get post api
    :param user_id_key_path: $..userid - used to get the list of values matching the given query
    :param postid_key_path: $..id - used to get the list of values matching the given query
    :param search_userid: user id to search from the json response
    :return: list of post made by the given user
    """
    try:
        print("Json response: " + str(json_response))
        userid_list = get_response_for_given_path(json_response, user_id_key_path)
        print("Received list from" + user_id_key_path + " key search: " + str(userid_list))
        post_id_list = get_response_for_given_path(json_response, postid_key_path)
        print("Received list from" + postid_key_path + " key search: " + str(post_id_list))
        indexes = [i for i, x in enumerate(userid_list) if x == search_userid]
        specific_user_post_ids = []
        for i in range(len(indexes)):
            specific_user_post_ids.append(post_id_list[indexes[i]])
        return specific_user_post_ids
    except Exception as exception:
        print("Error occurred in processing the list " + str(exception.message))
        return []


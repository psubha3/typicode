import jsonpath


def get_response_for_given_path(json_response, path):
    match_response = jsonpath.jsonpath(json_response, path)
    return match_response


def check_given_value_present_in_list(listitem, search_string):
    if listitem.count(search_string):
        print(search_string + " is present in the list")
        return True
    else:
        print(search_string + " is not present in the list")
        return False

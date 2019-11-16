import jsonpath


def get_response_for_given_path(json_response, path):
    match_response = jsonpath.jsonpath(json_response, path)
    return match_response


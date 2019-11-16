import requests
from requests.exceptions import Timeout


class SessionWithUrlBase(object):
    def __init__(self, base_url):
        self.session = requests.Session()
        self.base_url = base_url

    def typicode_get_api(self, rest_service_name):
        try:
            return self.session.get(self.base_url + rest_service_name)
        except Timeout:
            print('The request timed out')

    def typicode_get_api_with_query(self, rest_service_name, query):
        try:
            return self.session.get(self.base_url + rest_service_name + "?" + query)
        except Timeout:
            print('The request timed out')

    def close_typicode_session(self):
        self.session.close()


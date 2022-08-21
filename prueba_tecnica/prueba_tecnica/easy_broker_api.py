import requests

class EasyBrokerAPIManager:
    auth_token = str
    def __init__(self, auth_token):
        self.auth_token = auth_token

    def get_properties(self, url):
        try:
            response = requests.get(url, headers = {"X-Authorization": self.auth_token, "accept":"application/json"})
            return response.json()
        except Exception as error:
            return str(error)

    def post_contact_requests(self, url, json_data):
        try:
            response = requests.post(url, headers = {"X-Authorization": self.auth_token, "accept":"application/json"}, json=json_data)
            return response
        except Exception as error:
            return str(error)
           

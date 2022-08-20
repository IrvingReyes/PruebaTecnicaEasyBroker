import requests

class EasyBrokerAPIReader:
    
    def __init__(self, auth_token):
        self.auth_token = auth_token

    def get_properties(self, url):
        try:
            response = requests.get(url, headers = {"X-Authorization": self.auth_token, "accept":"application/json"})
            return response.json()
        except Exception as error:
            return str(error)

           

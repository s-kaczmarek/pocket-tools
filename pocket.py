import requests
import json 

class Pocket:

    API_ENDPOINT_GET = "https://getpocket.com/v3/get"
    API_ENDPOINT_ADD = "https://getpocket.com/v3/add"
    HEADERS = {'Content-Type' : 'application/json; charset=UTF-8','X-Accept': 'application/json'}
    REQUEST = {'consumer_key':'', 'access_token':''}


    # if response.status_code == 200:
    #     # Print to console
    #     jprint(response.json())

    def __init__(self, consumer_key, access_token):
        # self.consumer_key = consumer_key
        # self.access_token = access_token

        self.REQUEST['consumer_key'] = consumer_key
        self.REQUEST['access_token'] = access_token

    def beautify_json(self, obj):
        pretty_json = json.dumps(obj, sort_keys=True, indent=4)
        return pretty_json

    def retrieve_all_data(self, pretty_factor):

        self.REQUEST.update({"detailType":"complete"})
        response = requests.get(self.API_ENDPOINT_GET, self.REQUEST)

        if pretty_factor == "true":
            return self.beautify_json(response.json())
        else:
            return response.json()


import sys
import requests
from requests.auth import HTTPBasicAuth
from secret import wufoo_key


def get_wufoo_data() -> dict:
    # Api call to wufoo using secret key to retrieve form responses
    url = "https://chendro.wufoo.com/api/v3/forms/zk890sm1gnzlxu/entries/json"
    # comment to test workflow
    response = requests.get(url, auth=HTTPBasicAuth(wufoo_key, 'pass'))
    print(response.text)

    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
        sys.exit(-1)
    jsonresponse = response.json()
    return jsonresponse['Entries']


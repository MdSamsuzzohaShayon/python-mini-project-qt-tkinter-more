import requests


"""
print("Fetching API")
req_api = requests.get("http://httpbin.org")
res_json = requests.get("http://httpbin.org/json")
print("Making get request to api: ",req_api)
print("Getting response json: ", res_json.json())
"""



def json_api(url):
    res_json = requests.get(url)
    if res_json.status_code == 200:
        return res_json.json()
    else:
        return 'There was an error'
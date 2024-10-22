import requests


import environ
env = environ.Env()
# reading .env file
environ.Env.read_env()
subscription_key = env("subscription_key")
assert subscription_key


def bingsearch(search_term):
    search_url = "https://api.bing.microsoft.com/v7.0/search"
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {"q": search_term, "textDecorations": True, "textFormat": "HTML"}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    return search_results

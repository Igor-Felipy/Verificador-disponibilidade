import requests

def verify(url):
    url = url

    status = requests.get(url).status_code()

    return status
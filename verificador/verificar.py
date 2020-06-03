import requests

def verify(url):
    url = url
    status = requests.get(url)
    return status.status_code


def get_response(status):
    status = status
    while True:
        if status == 100:
            print('The server want more time of connection')
        elif status == 101:
            print('The server want switch a protocol')
        elif status == 102:
            print('The server is processing the information')
        elif status == 103:
            print('The server want to pre-charge resources')
        elif status == 200:
            print('Everything is OK')
        elif status == 201:
            print('Everything is OK and a resource was succesfully create')
        elif status == 200:
            print('')
        elif status == 202:
            print('The request was received but not ')
        elif status == 404:
            print('')
        elif status == 400:
            print('')


def url_clean():
    url = url
    
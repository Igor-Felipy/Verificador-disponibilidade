import requests

def verify(url):
    url = url
    status = requests.get(url)
    return status.status_code


def get_response(status):
    status = status
    while True:
        if status == 100:
            print('Continue')
        elif status == 101:
            print('Switching Protocol')
        elif status == 102:
            print('Processing (WebDAV)')
        elif status == 103:
            print('Early hints')
        elif status == 200:
            print('OK')
        elif status == 201:
            print('Created')
        elif status == 202:
            print('Accepted')
        elif status == 203:
            print('Non-Authoritative Information')
        elif status == 204:
            print('No Content')
        elif status == 205:
            print('Reset Content')
        elif status == 206:
            print('Partitial content')
        elif status == 207:
            print('Multi-Status (WebDAV)')
        elif status == 208:
            print('Multi-Status (WebDAV)')
        elif status == 226:
            print('IM Used (HTTP Delta encoding)')
        elif status == 300:
            print('Mutiple Choice')
        elif status == 301:
            print('Moved Permanently')
        elif status == 302:
            print('Found')
        elif status == 303:
            print('See Other')
        elif status == 304:
            print('Not Modified')
        elif status == 305:
            print('Use Proxy')
        elif status == 306:
            print('Unused')
        elif status == 307:
            print('Temporary Redirect')
        elif status == 308:
            print('Permanent Redirect')
        elif status == 400:
            print('Bad request')
        elif status == 401:
            print('Unauthorized')
        elif status == 402:
            print('Payment Required')
        elif status == 403:
            print('Forbidden')
        elif status == 404:
            print('Not Found')
        elif status == 405:
            print('Method Not Allowed')
        elif status == 406:
            print('Not Acceptable')
        elif status == 407:
            print('Proxy Authentication')
        elif status == 408:
            print('Request Timeout')
        elif status == 409:
            print('Conflict')
        elif status == 410:
            print('Gone')
        elif status == 411:
            print('Length Required')
        elif status == 412:
            print('Precondition Failed')
        elif status == 413:
            print('Payload Too Large')
        elif status == 414:
            print('URI Too Long')
        elif status == 415:
            print('Unsupported Media Type')
        elif status == 416:
            print('')


def url_clean():
    url = url
    
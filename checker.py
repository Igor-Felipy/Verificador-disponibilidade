def main(menu):
    print('\n')
    if menu.upper() == 'U':
        unique_verification()
    elif menu.upper() == 'C':
        continuos_verification()
    elif menu.upper() == 'S':
        check_save()
    elif menu.upper() == 'H':
        help_user()
    else:
        print('Invalid Argument')


def verify(url):
    url = url_clean(url)
    status = requests.get(url).status_code
    return get_response(status)


def url_clean(url):
    try:
        url = url
        if 'http://' in url or 'https://' in url:
            nurl = url
            return nurl
        else:
            nurl = str('http://' + url)
            return nurl
    except:
        print('error')


def get_response(status):
    status = status
    return str('The server say: ' + status_code[status] + f'\t Response type: {status}' + '\tDate: ' + str(datetime.datetime.now()))
    

def unique_verification():
    try:
        url = url_clean(input('Which site to check? '))
        print(verify(url))
        print('\n\n')
    except:
        print('Error')

def continuos_verification():
    url = url_clean(input('Which site to check? '))
    time = int(input('How often? (seconds)'))
    while True:
        try:
            print(verify(url))
        except:
            print('Error')
            break
        sleep(time)

def check_save():
    url = verify.url_clean(input('Which site to check? '))
    time = int(input('How often? (seconds)'))
    arch = str(input('What do you want to name the file? ') + '.txt')
    while True:
        to_write = str(verify.verify(url) + '\n')
        try:
            w = open(arch, 'a')
            w.write(to_write)
        except:
            print('Error')
            break
        print(to_write)
        sleep(time)

def help_user():
    print('Consult the documentation in https://github.com/Igor-Felipy/Verificador-disponibilidade')

status_code = {
    100:'Continue',
    101:'Switching Protocol',
    102:'Processing (WebDAV)',
    103:'Early hints',
    200:'OK',
    201:'Created',
    202:'Accepted',
    203:'Non-Authoritative Information',
    204:'No Content',
    205:'Reset Content',
    206:'Partitial content',
    207:'Multi-Status (WebDAV)',
    208:'Multi-Status (WebDAV)',
    226:'IM Used (HTTP Delta encoding)',
    300:'Mutiple Choice',
    301:'Moved Permanently',
    302:'Found',
    303:'See Other',
    304:'Not Modified',
    305:'Use Proxy',
    306:'Unused',
    307:'Temporary Redirect',
    308:'Permanent Redirect',
    400:'Bad request',
    401:'Unauthorized',
    402:'Payment Required',
    403:'Forbidden',
    404:'Not Found',
    405:'Method Not Allowed',
    406:'Not Acceptable',
    407:'Proxy Authentication',
    408:'Request Timeout',
    409:'Conflict',
    410:'Gone',
    411:'Length Required',
    412:'Precondition Failed',
    413:'Payload Too Large',
    414:'URI Too Long',
    415:'Unsupported Media Type',
    416:'Requested Range Not Satisfiable',
    417:'Expectation Failed',
    418:'I\'m a teapot',
    421:'Misdirected Request',
    422:'Unprocessable Entity',
    423:'Locked (WebDAV)',
    424:'Failed Dependency',
    425:'Too Early',
    426:'Upgrade Required',
    428:'Precondition Required',
    429:'Too Many Requests',
    431:'Request Header Fields Too Large',
    451:'Unavailable For Legal Reasons',
    500:'Internal Server Error',
    501:'Not Implemented',
    502:'Bad Gateway',
    503:'Service Unavailable',
    504:'Gateway Timeout',
    505:'HTTP Version Not Supported',
    506:'Variant Also Negotiates',
    507:'Insufficient Storage',
    508:'Loop Detected (WebDAV)',
    510:'Not Detected (WebDAV)',
    511:'Network Authentication Required',
    'source':'https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status'
}


if __name__=="__main__":
    import requests
    import datetime
    from time import sleep
    
    import argparse
    parser = argparse.ArgumentParser('Connection Checker')
    parser.add_argument('--check',type=str, default='u', help="Unique verification [U] \nContinuous verification [C] \nCheck and save to file [S]")
    args = parser.parse_args()
    main(args.check)

import requests

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



def verify(url):
    url = url
    status = requests.get(url).status_code
    get_response(status)


def url_clean(url):
    url = url
    if 'http://' in url or 'https://' in url:
        nurl = url
        return nurl
    elif 'www' in url:
        nurl = str('https://' + url)
        return nurl
    else:
        nurl = str('https://www.' + url)
        return nurl


def get_response(status):
    status = status
    print('The server say: ' + status_code[status])
    
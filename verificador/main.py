import verify

try:
    url = verify.url_clean(input('qual site verificar? '))
    verify.verify(url)
except:
    print('Error')

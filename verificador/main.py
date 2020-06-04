import verificar

try:
    url = verificar.url_clean(input('qual site verificar? '))
    verificar.verify(url)
except:
    print('Error')
    
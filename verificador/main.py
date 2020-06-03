import verificar

url = input('qual site verificar? ')

response = verificar.verify(url)
if response == 200:
    print('Site no ar')
elif response == 404:
    print('Site não encontrado! ')
elif response == 400:
    ('Site não funcionando!')
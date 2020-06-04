import verificar

url = input('qual site verificar? ')



response = verificar.verify(url)

verificar.get_response(response)
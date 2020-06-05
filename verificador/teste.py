import verify
url = 'google.com'

print(verify.verify(url))
with open('google.txt','a+') as archive:
    for i in archive:
        archive.write(verify.verify(url))
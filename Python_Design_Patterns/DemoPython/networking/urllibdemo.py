import urllib.request

try:
    url = urllib.request.urlopen('https://www.python.org/')
    content=url.read()
    url.close()
except urllib.error.HTTPError:
    print('Web page not found')
    exit()

f=open('python.html','wb')
f.write(content)
f.close()
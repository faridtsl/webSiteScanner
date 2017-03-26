import requests

proxies = {"http": None,
           "https": None}

def get_robots_txt(url):
    print('Robot.txt ...')
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    req= requests.get(url+'/robots.txt', proxies=proxies) #Getting the HTML content of the webpage
    encoding=req.encoding
    if encoding==None:
        encoding="utf-8"
    req=req.content.decode(encoding)
    data = ""
    for line in req:
        data = data + line
    return data

import urllib2
import io

def get_robots_txt(url):
    print('Robot.txt ...')
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    req = urllib2.urlopen(path+'robots.txt')
    data = ""
    for line in req:
        data = data + line
    return data

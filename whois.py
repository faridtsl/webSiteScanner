import os


def get_whois(url):
    print('Whois ...')
    command = 'whois ' + url
    process = os.popen(command)
    return str(process.read())

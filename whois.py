import os


def get_whois(url):
    print('Whois ...')
    command = 'whois ' + url
    process = os.popen(command)
    result = ''
    for line in process:
        result = result + line
    return result
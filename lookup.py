import os

def get_lookup(url):
    print('lookup ...')
    command = 'nslookup -type=a ' + url
    command1 = 'nslookup -type=mx ' + url
    command2 = 'nslookup -type=soa ' + url
    process = os.popen(command)
    result = ''
    for line in process:
        result = result + line

    process = os.popen(command1)
    for line in process:
        result = result + line

    process = os.popen(command2)
    for line in process:
        result = result + line

    return result

def get_enum(url):
    print('dnsenum ...')
    command = 'dnsenum ' + url
    process = os.popen(command)
    result = ''
    for line in process:
        result = result + line

    return result

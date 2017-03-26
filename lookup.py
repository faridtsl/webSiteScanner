import os

def get_lookup(url):
    print('lookup ...')
    command = 'nslookup -type=a ' + url
    command1 = 'nslookup -type=mx ' + url
    command2 = 'nslookup -type=soa ' + url
    process = os.popen(command)
    result = ''
    result +=str(process.read())
    process = os.popen(command1)
    result += str(process.read())
    process = os.popen(command2)
    result += str(process.read())
    return result

def get_enum(url):
    print('dnsenum ...')
    command = 'dnsenum ' + url
    process = os.popen(command)
    result = str(process.read())
    if result == "":
        result="Error while getting DNSENUM results"
    return result

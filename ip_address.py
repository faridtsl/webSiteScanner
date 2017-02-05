import os

def get_ip_address(url):
    print('host ...')
    command = "host "+ url
    process = os.popen(command)
    result = str(process.read())
    marker = result.find("has address") + 12
    endmark = result.find('\n')
    first = result[marker:endmark].splitlines()[0]
    second = result[endmark:]
    if second != None :
        marker = second.find("handled by") + 11
        endmark = second[marker:].find('\n')
        second = second[marker:marker+endmark-1]
    res =  first,second
    return  res

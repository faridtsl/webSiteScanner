import os

def get_ip_address(url):
    print('host ...')
    command = 'host '+str(url)
    process = os.popen(command)
    result = str(process.read())
    try:
        ip = result.split("has address ")[1]
        return ip
    except:
        return ""


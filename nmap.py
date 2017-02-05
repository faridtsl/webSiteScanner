import os

def get_nmap(options , ip):
    print('nmap ...')
    command = "nmap " + options + " " + ip
    process = os.popen(command)
    result = ''
    for line in process:
        result = result + line
    return result

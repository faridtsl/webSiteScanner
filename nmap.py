import os

def get_nmap(options , ip):
    print('nmap ...')
    command = "nmap " + options + " " + ip
    process = os.popen(command)
    return str(process.read())
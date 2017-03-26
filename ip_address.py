import os

def get_ip_address(url):
    print('host ...')
    command = 'host '+str(url)
    process = os.popen(command)
    result = str(process.read())
    mail = "Error while getting mail address"
    try:
        splitted=result.split('\n')
        ip = splitted[0].split("has address ")[1]
        for e in splitted:
            if 'is handled by ' in e:
                mail=e.split('is handled by ')[1] #.split(' ')[1]
                break
            mail = "Error while getting mail address"

    except:
        ip= "Error while getting ip address"
    return (ip,mail)


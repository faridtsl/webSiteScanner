import re

def get_domain_name(url):
    print('Top level domain ...')
    tld = re.sub(r'((http|https):\/\/)?www\.([^\.]*\.)*([^\/]*)(\/)?.*', r'\4', url, re.IGNORECASE)
    return tld
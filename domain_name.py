import tld

def get_domain_name(url):
    print('Top level domain ...')
    return tld.get_tld(url)

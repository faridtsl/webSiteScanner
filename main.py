from general import *
from domain_name import *
from ip_address import  *
from nmap import *
from robots_txt import *
from whois import *
from lookup import *


ROOT_DIR = "~/reconnaissance"
create_dir(ROOT_DIR)

def gather_info(name, url):
    domain = get_domain_name('http://'+url)
    ip_adr = get_ip_address(domain)
    nmap = get_nmap('-F',ip_adr[0])
    rbt_txt = get_robots_txt('http://'+url)
    whois = get_whois(domain)
    lookup = get_lookup(url)
    enm = get_enum(url)
    create_report(name,url,ip_adr,domain,nmap,rbt_txt,whois,lookup,enm)

def create_report(name,url,ip_adr,domain,nmap,rbt_txt,whois,lkp,enm):
    print('Creating report ...')
    prjct_dir = ROOT_DIR + '/' + name
    create_dir(prjct_dir)
    write_file(prjct_dir + '/full_url.txt', url)
    ip = ip_adr[0]
    mail = ip_adr[1]
    dt = 'IP : ' + ip + '\n Mail : '+ mail
    write_file(prjct_dir + '/ip.txt', dt)
    write_file(prjct_dir + '/domain.txt', domain)
    write_file(prjct_dir + '/nmap.txt', nmap)
    write_file(prjct_dir + '/rbt.txt', rbt_txt)
    write_file(prjct_dir + '/whois.txt', whois)
    write_file(prjct_dir + '/lookup.txt', lkp)
    write_file(prjct_dir + '/dnsenum.txt', enm)

site = raw_input('Site you want to scan : ')
name = raw_input('Folder name : ')
gather_info(str(name),str(site))
#gather_info('test','www.scorify.me')

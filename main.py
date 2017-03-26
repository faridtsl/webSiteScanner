from general import *
from domain_name import *
from ip_address import  *
from nmap import *
from robots_txt import *
from whois import *
from lookup import *


ROOT_DIR = "./reconnaissance"
create_dir(ROOT_DIR)

def gather_info(name, url):
    if(url[:4]!="http"):
        url="http://"+url
    domain = get_domain_name(url)
    (ip_adr,mail_adr) = get_ip_address(domain)
    nmap = get_nmap('-F',ip_adr)
    rbt_txt = get_robots_txt(url)
    whois = get_whois(domain)
    lookup = get_lookup(url)
    enm = get_enum(url)
    create_report(name,url,ip_adr,mail_adr,domain,nmap,rbt_txt,whois,lookup,enm)

def create_report(name,url,ip_adr,mail_adr,domain,nmap,rbt_txt,whois,lkp,enm):
    print('Creating report ...')
    prjct_dir = ROOT_DIR + '/' + name
    create_dir(prjct_dir)
    write_file(prjct_dir+"/Report.txt","Rapport sur le site   : "+url)
    write_file(prjct_dir+"/Report.txt","\n=======================\n\n")
    write_file(prjct_dir+"/Report.txt","\n\t- Domain Name       : "+domain)
    write_file(prjct_dir + "/Report.txt","\n\t=====================\n\n")
    write_file(prjct_dir+"/Report.txt","\n\t- Ip Address        : " + ip_adr)
    write_file(prjct_dir+"/Report.txt","\n\t- Mail Address      : " + mail_adr)
    write_file(prjct_dir + "/Report.txt","\n\t======================\n\n")
    write_file(prjct_dir+"/Report.txt","\n\t- NMAP Results      : ")
    write_file(prjct_dir + "/Report.txt", "\n\t======================\n\n")
    write_file(prjct_dir + "/Report.txt", reindent(nmap,"\t\t"))
    write_file(prjct_dir+"/Report.txt","\n\t- Robot text result : ")
    write_file(prjct_dir + "/Report.txt", "\n\t======================\n\n")
    write_file(prjct_dir + "/Report.txt",reindent(rbt_txt,"\t\t"))
    write_file(prjct_dir+"/Report.txt","\n\t- WHOIS result      : ")
    write_file(prjct_dir + "/Report.txt", "\n\t======================\n\n")
    write_file(prjct_dir + "/Report.txt", reindent(whois,"\t\t"))
    write_file(prjct_dir+"/Report.txt","\n\t- Lookup result     : ")
    write_file(prjct_dir + "/Report.txt", "\n\t======================\n\n")
    write_file(prjct_dir + "/Report.txt", reindent(lkp,"\t\t"))
    write_file(prjct_dir+"/Report.txt","\n\t- DNSENUM result    : ")
    write_file(prjct_dir + "/Report.txt", "\n\t======================\n\n")
    write_file(prjct_dir + "/Report.txt",reindent(enm,"\t\t"))


site = input('Site you want to scan : ')
name = input('Folder name : ')
gather_info(str(name),str(site))


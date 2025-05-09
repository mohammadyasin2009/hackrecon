import requests
from bs4 import BeautifulSoup
import socket
from urllib.parse import urlparse
import re
import whois
import argparse
#requests baray gereftan etelaat ya api site hast.
#beautifulsoup baray gereftan html site hast ke maemolan ba requests miad.

print("                                       ❤ salam,be barname shadow_crack khosh amadid ❤                                   ")
print("")
while True:
        def get_links(url):
            if (url.startswith('https://') or url.startswith('http://')):
                site = requests.get(url)
                soup = BeautifulSoup(site.text, 'html.parser')
                linkha = []
                for link in soup.find_all('a'):
                    href = link.get('href')
                    if href:
                        linkha.append(href)
                    
                link2 = []
                for link in linkha: 
                    if link.startswith('http') or link.startswith('https'):
                        try:
                            response2 = requests.get(link)
                            soup2 = BeautifulSoup(response2.text, 'html.parser')
                            for link_tag in soup2.find_all('a'):
                                href2 = link_tag.get('href')
                                if href2:
                                    link2.append(href2)
                        except:
                            continue
                return linkha + link2
            else:
                print("                                                $&&&&&&&&&&&&&&&&&&&&&&&&&&&$")
                print("                                                ❌adress vorody sahih nist❌")
                print("                                                $&&&&&&&&&&&&&&&&&&&&&&&&&&&$")
                print("")
        print("                                               ################################")
        url = input("                                               link vorody ra vared konid:")
        print("                                               ################################")
        print("")
        print("                                         ===========================================")
        print("                                         dar hal peyda kardan etelaat site hastim 🔍")
        print("                                         ===========================================")
        print("                                                                                             ")
        linkha = get_links(url)

        if (url.startswith('https://') or url.startswith('http://')):
            #get all links baray site
            links = get_links(url)
            for link in links:
                output = f"| {link} | "
                
                try:

                    # get titles ha
                    site = requests.get(link)
                    soup = BeautifulSoup(site.text, 'html.parser')
                    title = soup.find("title")
                    if title:
                        output += f"| {title} | "
                    else:
                        output += f"| ❌ no title ❌|"
                    



                    #eror ha
                    if(site.status_code == 200):
                        output += f"| {site.status_code} succes |"
                    elif site.status_code == 301:
                        output += f"| {site.status_code} natije: Moved Permanently |"
                    elif site.status_code == 302:
                        output += f"| {site.status_code} Found (Temporary Redirect) |"
                    elif site.status_code == 400:
                        output += f"| {site.status_code} natije: Bad Request |"
                    elif site.status_code == 401:
                        output += f"| {site.status_code} natije: Unauthorized |"
                    elif site.status_code == 403:
                        output += f"| {site.status_code} natije: Forbidden |"
                    elif site.status_code == 404:
                        output += f"| {site.status_code} natije: Not Found |"
                    elif site.status_code == 500: 
                        output += f"| {site.status_code} natije: Internal Server Error |"
                    else:
                        output += f"| ❌ eror koly ❌ |"



                    #subdomain ha
                    domain = urlparse(link).netloc
                    output += f"| Domain ha: {domain} | "
                    


                    # get open ports and ip ha
                    try:
                        ip = socket.gethostbyname(domain)
                        output += f"| IP site: {ip} | "
                        
                        ports = [21, 22, 23, 25, 53, 80, 110, 119, 123, 143, 161, 194, 443, 445, 993, 995]
                        open_ports = []
                        for port in ports:
                            #af_inet yaeni az ipv4 estefade kon
                            #sock_stream yaeni az tcp site ke etesal motmaen va mehvar hast estefade kon
                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            #connect_ex saeyesh ro mikone be ip port mored nazar vasl beshe
                            result = s.connect_ex((ip, port))
                            if result == 0:
                                strport = str(port)
                                open_ports.append(strport)
                        output += f"| Open Ports: {open_ports} | "
                    except:
                        output += f"| ❌ ip peyda nashod! ❌ |"
                    



                    # get emails and phone numbers ha
                    emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', site.text)
                    mobiles = re.findall(r'(?:\+98|0|98)?9[0-9]{9}\b', site.text)
                    output += f"| Emails: {emails} | Mobiles: {mobiles} |"



                    # get whois ha etelaat
                    try:
                        whoiss = str(site)
                        mmd = urlparse(whoiss).netloc
                        endd = whois.whois(mmd)
                        tabdil = str(endd)
                        whoiss = tabdil.replace('\n', '')
                        output += f"| etelaat koly site: {whoiss} |"
                    except:
                        output += f"| ❌ etelaaty yaft nashod! ❌ |"



                except:
                    output += f"| Error |"
                print("")



                p = argparse.ArgumentParser(output)
                p.add_argument('--recon')
                print("")
                print("===========================================================================================================================")
                print(f" {p}")
                print("==========================================================================================================================")
                print("")

                #enconding='utf-8' yaeni inke khata hara nadide begire mesl vojod horof farsi
                with open ('b.txt' ,'a' , encoding='utf-8') as file:
                    file.write(output + '\n')
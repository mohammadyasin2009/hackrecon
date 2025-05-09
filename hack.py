import requests
from bs4 import BeautifulSoup
import socket
from urllib.parse import urlparse
import re
import whois
import argparse

while True:
        def get_links(url):
            if (url.startswith('https://') or url.startswith('http://')):
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                all_links = []
                for link in soup.find_all('a'):
                    href = link.get('href')
                    if href:
                        all_links.append(href)
                    second_level_links = []
                for link in all_links:
                    if link.startswith('http') or link.startswith('https'):
                        try:
                            response2 = requests.get(link)
                            soup2 = BeautifulSoup(response2.text, 'html.parser')
                            for link2 in soup2.find_all('a'):
                                href2 = link2.get('href')
                                if href2:
                                    second_level_links.append(href2)
                        except:
                            continue
                return all_links + second_level_links
            else:
                print("❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌")
                print("lotfan adress ra dorost vared konid:")
                print("❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌")
        print("")
        print("...............................................")
        url = input("link vorody ra vared konid: ")
        print("...............................................")
        print("")
        all_links = get_links(url)

        if (url.startswith('https://') or url.startswith('http://')):
            #get all links baray site
            links = get_links(url)
            for link in links:
                print(link)
                output = f"| {link} | "
                
                try:

                    # get titles ha
                    response = requests.get(link)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    title = soup.find("title")
                    if title:
                        output += f"| {title} | "
                    else:
                        output += f"| no title |"
                    



                    #eror ha
                    if(response.status_code == 200):
                        output += f"| {response.status_code} succes |"
                    elif response.status_code == 301:
                        output += f"| {response.status_code} natije: Moved Permanently |"
                    elif response.status_code == 302:
                        output += f"| {response.status_code} Found (Temporary Redirect) |"
                    elif response.status_code == 400:
                        output += f"| {response.status_code} natije: Bad Request |"
                    elif response.status_code == 401:
                        output += f"| {response.status_code} natije: Unauthorized |"
                    elif response.status_code == 403:
                        output += f"| {response.status_code} natije: Forbidden |"
                    elif response.status_code == 404:
                        output += f"| {response.status_code} natije: Not Found |"
                    elif response.status_code == 500: 
                        output += f"| {response.status_code} natije: Internal Server Error |"
                    else:
                        output += f"| eror koly |"



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
                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            result = s.connect_ex((ip, port))
                            if result == 0:
                                open_ports.append(str(port))
                        output += f"| Open Ports: {open_ports} | "
                    except Exception as e:
                        output += f"| ip peyda nashod! {e} |"
                    



                    # get emails and phone numbers ha
                    emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', response.text)
                    mobiles = re.findall(r'(?:\+98|0|98)?9[0-9]{9}\b', response.text)
                    output += f"| Emails: {emails} | Mobiles: {mobiles} |"



                    # get whois ha etelaat
                    whoiss = str(response)
                    mmd = urlparse(whoiss).netloc
                    endd = whois.whois(mmd)
                    tabdil = str(endd)
                    whoiss = tabdil.replace('\n', '')
                    output += f"| etelaat koly site: {whoiss} |"




                except:
                    output += f"| Error |"
                print("")



                p = argparse.ArgumentParser(output)
                p.add_argument('--recon')
                print("")
                print(f" {p}")
                print("")
                # with open ('b.txt' ,'w') as file:
                #     file.write(str(output))
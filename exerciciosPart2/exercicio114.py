import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
    print('pudim está acessivel')
except:
    print('error')
finally:
    print('obrigado.')
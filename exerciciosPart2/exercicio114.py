<<<<<<< HEAD
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
    print('pudim está acessivel')
except:
    print('error')
finally:
=======
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
    print('pudim está acessivel')
except:
    print('error')
finally:
>>>>>>> 2971a5e28b248edd4b836abe9eabe7b067b9aa8f
    print('obrigado.')
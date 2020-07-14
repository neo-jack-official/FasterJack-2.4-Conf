#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#By Neo-Jack
#Thanks to: @Fr33W0lf_

import os
from os import system, name
import sys

host = None
def random_lib():
    try:
        import random
        pass
    except ImportError:
        os.system('python -m pip install random')
        import random
    try:
        import random
        pass
    except ImportError:
        os.system('sudo pip install random')
        import random
    try:
        import random
        pass
    except ImportError:
        os.system('pip install random')
        import random
def sys_lib():
    try:
        import sys
        pass
    except ImportError:
        os.system('python -m pip install sys')
        import sys
    try:
        import sys
        pass
    except ImportError:
        os.system('sudo pip install sys')
        import sys
    try:
        import sys
        pass
    except ImportError:
        os.system('pip install sys')
        import sys
def socket_lib():
    try:
        import socket
        pass
    except ImportError:
        os.system('python -m pip install socket')
        import socket
    try:
        import socket
        pass
    except ImportError:
        os.system('sudo pip install socket')
        import socket
    try:
        import socket
        pass
    except ImportError:
        os.system('pip install socket')
        import socket
def socks_lib():
    try:
        import socks
        pass
    except ImportError:
        os.system('python -m pip install socks')
        import socks
    try:
        import socks
        pass
    except ImportError:
        os.system('sudo pip install socks')
        import socks
    try:
        import socks
        pass
    except ImportError:
        os.system('pip install socks')
        import socks
def requests_lib():
    try:
        import requests
        pass
    except ImportError:
        os.system('python -m pip install requests')
        import requests
    try:
        import requests
        pass
    except ImportError:
        os.system('sudo pip install requests')
        import requests
    try:
        import requests
        pass
    except ImportError:
        os.system('pip install requests')
        import requests
def threading_lib():
    try:
        import threading
        pass
    except ImportError:
        os.system('python -m pip install threading')
        import threading
    try:
        import threading
        pass
    except ImportError:
        os.system('sudo pip install threading')
        import threading
    try:
        import urllib.request
        pass
    except ImportError:
        os.system('pip install threading')
        import threading
def urllib_lib():
    try:
        import urllib.request
        pass
    except ImportError:
        os.system('python -m pip install urllib.request')
        import urllib.request
    try:
        import urllib.request
        pass
    except ImportError:
        os.system('sudo pip install urllib.request')
        import urllib.request
    try:
        import urllib.request
        pass
    except ImportError:
        os.system('pip install urllib.request')
        import urllib.request
def time_lib():
    try:
        import time
        pass
    except ImportError:
        os.system('python -m pip install time')
        import time
    try:
        import time
        pass
    except ImportError:
        os.system('sudo pip install time')
        import time
    try:
        import time
        pass
    except ImportError:
        os.system('pip install time')
        import time
def optparse_lib():
    try:
        from optparse import Queue
        pass
    except ImportError:
        os.system('python -m pip install optparse')
        from optparse import OptionParser
    try:
        from optparse import OptionParser
        pass
    except ImportError:
        os.system('sudo pip install optparse')
        from optparse import OptionParser
    try:
        from optparse import OptionParser
        pass
    except ImportError:
        os.system('pip install optparse')
        from optparse import OptionParser
def queue_lib():
    try:
        from queue import Queue
        pass
    except ImportError:
        os.system('python -m pip install queue')
        from queue import Queue
    try:
        from queue import Queue
        pass
    except ImportError:
        os.system('sudo pip install queue')
        from queue import Queue
    try:
        from queue import Queue
        pass
    except ImportError:
        os.system('pip install queue')
        from queue import Queue
def colorama_lib():
    try:
        from colorama import Fore, Back, Style
        pass
    except ImportError:
        os.system('python -m pip install colorama')
        from colorama import Fore, Back, Style
    try:
        from colorama import Fore, Back, Style
        pass
    except ImportError:
        os.system('sudo pip install colorama')
        from colorama import Fore, Back, Style
    try:
        from colorama import Fore, Back, Style
        pass
    except ImportError:
        os.system('pip install colorama')
        from colorama import Fore, Back, Style
def pip_inst():
    try:
        print("Trying to Install PIP required for modules\n")
        #Debian, Ubuntu
        os.system("sudo apt-get install python-pip")
    except ImportError:
        print("Trying to Install PIP required for modules\n")
        #Windows, etc
        os.system("python get-pip.py")
    try:
        print("Trying to Install PIP required for modules\n")
        #Fedora
        os.system("sudo dnf install python-pip")
    except ImportError:
        print("Trying to Install PIP required for modules\n")
        #openSUSE
        os.system("sudo zypper install python-pip")
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
def lis0111010001100001():
    global lis_011000010110001001100011, lis_011000100110100101101110, w , cl, com, org, n, blo    
    lis_011000010110001001100011 = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",".",":","/","_","-"]
    lis_011000100110100101101110 = ["00100000","01100001","01100010","01100011","01100100","01100101","01100110","01100111",
    "01101000","01101001","01101010","01101011","01101100","01101101","01101110","01101111","01110000",
    "01110001","01110010","01110011","01110100","01110101","01110110","01110111","01111000","01111001",
    "01111010","00101110","00111010","00101111","01011111","00101101"]
    if lis_011000010110001001100011 and lis_011000100110100101101110:
        lis_011000100110100101101110 = lis_011000010110001001100011
        n = lis_011000100110100101101110
    w = n[23] + n[23] + n[23] + n[27] 
    cl = n[27] + n[3] + n[12] 
    com = n[27] + n[3] + n[15] + n[13]
    org = n[27] + n[15] + n[18] + n[7]
    blo = n[27] + n[2] + n[12] + n[15] + n[7] + n[19] + n[16] + n[15] + n[20] + com 
def we01100010():
    lis0111010001100001()
    global w01100101bs
    w01100101bs = []    
    w01100101bs.append(w + n[5] + n[12] + n[16] + n[21] + n[5] + n[2] + n[12] + n[15] + n[9] + n[14] + n[6] + n[15] + n[18] + n[13] + n[1] + com)
    w01100101bs.append(n[5] + n[12] + n[16] + n[21] + n[5] + n[2] + n[12] + n[15] + n[9] + n[14] + n[6] + n[15] + n[18] + n[13] + n[1] + com)    
    w01100101bs.append(w + n[12] + n[1] + n[22] + n[15] + n[26] + n[4] + n[5] + n[12] + n[15] + n[19] + n[17] + n[21] + n[5] + n[19] + n[15] + n[2] + n[18] + n[1] + n[14] + cl)
    w01100101bs.append(n[12] + n[1] + n[22] + n[15] + n[26] + n[4] + n[5] + n[12] + n[15] + n[19] + n[17] + n[21] + n[5] + n[19] + n[15] + n[2] + n[18] + n[1] + n[14] + cl)    
    w01100101bs.append(w + n[18] + n[5] + n[4] + n[4] + n[9] + n[7] + n[9] + n[20] + n[1] + n[12] + cl)
    w01100101bs.append(n[18] + n[5] + n[4] + n[4] + n[9] + n[7] + n[9] + n[20] + n[1] + n[12] + cl)    
    w01100101bs.append(w + n[5] + n[12] + n[21] + n[14] + n[9] + n[22] + n[5] + n[18] + n[19] + n[1] + n[12] + cl)
    w01100101bs.append(n[5] + n[12] + n[21] + n[14] + n[9] + n[22] + n[5] + n[18] + n[19] + n[1] + n[12] + cl)    
    w01100101bs.append(w + n[18] + n[1] + n[4] + n[9] + n[15] + n[27] + n[21] + n[3] + n[8] + n[9] + n[12] + n[5] + cl)
    w01100101bs.append(n[18] + n[1] + n[4] + n[9] + n[15] + n[27] + n[21] + n[3] + n[8] + n[9] + n[12] + n[5] + cl)    
    w01100101bs.append(w + n[16] + n[9] + n[5] + n[14] + n[19] + n[1] + n[3] + n[8] + n[9] + n[12] + n[5] + com)
    w01100101bs.append(n[16] + n[9] + n[5] + n[14] + n[19] + n[1] + n[3] + n[8] + n[9] + n[12] + n[5] + com)    
    w01100101bs.append(w + n[9] + n[14] + n[20] + n[5] + n[18] + n[6] + n[5] + n[18] + n[5] + n[14] + n[3] + n[9] + n[1] + cl)
    w01100101bs.append(n[9] + n[14] + n[20] + n[5] + n[18] + n[6] + n[5] + n[18] + n[5] + n[14] + n[3] + n[9] + n[1] + cl)    
    w01100101bs.append(w + n[18] + n[5] + n[7] + n[9] + n[15] + n[14] + n[1] + n[12] + n[9] + n[19] + n[20] + n[1] +cl)
    w01100101bs.append(n[18] + n[5] + n[7] + n[9] + n[15] + n[14] + n[1] + n[12] + n[9] + n[19] + n[20] + n[1] +cl)    
    w01100101bs.append(w + n[12] + n[1] + n[22] + n[15] + n[26] + n[4] + n[5] + n[13] + n[1] + n[9] + n[16] + n[21] + cl)
    w01100101bs.append(n[12] + n[1] + n[22] + n[15] + n[26] + n[4] + n[5] + n[13] + n[1] + n[9] + n[16] + n[21] + cl)    
    w01100101bs.append(w + n[18] + n[5] + n[19] + n[21] + n[13] + n[5] + n[14] + cl)
    w01100101bs.append(n[18] + n[5] + n[19] + n[21] + n[13] + n[5] + n[14] + cl)    
    w01100101bs.append(w + n[12] + n[1] + n[22] + n[15] + n[26] + n[4] + n[5] + n[16] + n[21] + n[3] + n[15] + n[14] + cl) 
    w01100101bs.append(n[12] + n[1] + n[22] + n[15] + n[26] + n[4] + n[5] + n[16] + n[21] + n[3] + n[15] + n[14] + cl)        
    w01100101bs.append(w + n[3] + n[8] + n[9] + n[12] + n[5] + n[15] + n[11] + n[21] + n[12] + n[20] + n[15] + cl)
    w01100101bs.append(n[3] + n[8] + n[9] + n[12] + n[5] + n[15] + n[11] + n[21] + n[12] + n[20] + n[15] + cl)        
    w01100101bs.append(w + n[12] + n[1] + n[9] + n[26] + n[17] + n[21] + n[9] + n[5] + n[18] + n[4] + n[1] + n[4] + n[9] + n[1] + n[18] + n[9] + n[15] + cl)
    w01100101bs.append(n[12] + n[1] + n[9] + n[26] + n[17] + n[21] + n[9] + n[5] + n[18] + n[4] + n[1] + n[4] + n[9] + n[1] + n[18] + n[9] + n[15] + cl)            
    w01100101bs.append(w + n[3] + n[9] + n[16] + n[5] + n[18] + n[3] + n[8] + n[9] + n[12] + n[5] + cl)
    w01100101bs.append(n[3] + n[9] + n[16] + n[5] + n[18] + n[3] + n[8] + n[9] + n[12] + n[5] + cl)    
    w01100101bs.append(w + n[18] + n[5] + n[22] + n[9] + n[19] + n[20] + n[1] + n[4] + n[5] + n[6] + n[18] + n[5] + n[14] + n[20] + n[5] + cl)
    w01100101bs.append(n[18] + n[5] + n[22] + n[9] + n[19] + n[20] + n[1] + n[4] + n[5] + n[6] + n[18] + n[5] + n[14] + n[20] + n[5] + cl)            
    w01100101bs.append(w + n[3] + n[18] + n[15] + n[14] + n[9] + n[3] + n[1] + n[4] + n[9] + n[7] + n[9] + n[20] + n[1] + n[12] + cl)
    w01100101bs.append(n[3] + n[18] + n[15] + n[14] + n[9] + n[3] + n[1] + n[4] + n[9] + n[7] + n[9] + n[20] + n[1] + n[12] + cl)           
    w01100101bs.append(w + n[6] + n[15] + n[18] + n[20] + n[9] + n[14] + n[13] + n[1] + n[16] + n[15] + n[3] + n[8] + n[15] + cl)
    w01100101bs.append(n[6] + n[15] + n[18] + n[20] + n[9] + n[14] + n[13] + n[1] + n[16] + n[15] + n[3] + n[8] + n[15] + cl)    
    w01100101bs.append(n[5] + n[12] + n[19] + n[9] + n[7] + n[12] + n[15] + cl)   
    w01100101bs.append(w + n[5] + n[12] + n[19] + n[9] + n[7] + n[12] + n[15] + cl)        
    w01100101bs.append(n[3] + n[15] + n[14] + n[22] + n[5] + n[18] + n[7] + n[5] + n[14] + n[3] + n[9] + n[1] + n[13] + n[5] + n[4] + n[9] + n[15] + n[19] + cl)    
    w01100101bs.append(w + n[3] + n[15] + n[14] + n[22] + n[5] + n[18] + n[7] + n[5] + n[14] + n[3] + n[9] + n[1] + n[13] + n[5] + n[4] + n[9] + n[15] + n[19] + cl)            
    w01100101bs.append(w + n[16] + n[18] + n[9] + n[13] + n[5] + n[18] + n[1] + n[12] + n[9] + n[14] + n[5] + n[1] + n[16] + n[18] + n[5] + n[14] + n[19] + n[1] + cl)    
    w01100101bs.append(n[16] + n[18] + n[9] + n[13] + n[5] + n[18] + n[1] + n[12] + n[9] + n[14] + n[5] + n[1] + n[16] + n[18] + n[5] + n[14] + n[19] + n[1] + cl)    
    w01100101bs.append(n[16] + n[9] + n[5] + n[14] + n[19] + n[1] + n[16] + n[18] + n[5] + n[14] + n[19] + n[1] + org)    
    w01100101bs.append(w + n[16] + n[9] + n[5] + n[14] + n[19] + n[1] + n[16] + n[18] + n[5] + n[14] + n[19] + n[1] + org)    
    w01100101bs.append(n[16] + n[18] + n[5] + n[14] + n[19] + n[1] + n[15] + n[16] + n[1] + n[12] + cl)    
    w01100101bs.append(w + n[16] + n[18] + n[5] + n[14] + n[19] + n[1] + n[15] + n[16] + n[1] + n[12] + cl)    
    w01100101bs.append(n[16] + n[18] + n[5] + n[14] + n[19] + n[1] + n[15] + n[16] + n[1] + n[12] + blo)    
    w01100101bs.append(w + n[18] + n[1] + n[4] + n[9] + n[15] + n[22] + n[9] + n[12] + n[12] + n[1] + n[6] + n[18] + n[1] + n[14] + n[3] + n[9] + n[1] + cl)    
    w01100101bs.append(n[18] + n[1] + n[4] + n[9] + n[15] + n[22] + n[9] + n[12] + n[12] + n[1] + n[6] + n[18] + n[1] + n[14] + n[3] + n[9] + n[1] + cl)    
    w01100101bs.append(n[18] + n[1] + n[4] + n[9] + n[15] + n[22] + n[9] + n[12] + n[12] + n[1] + n[6] + n[18] + n[1] + n[14] + n[3] + n[9] + n[1] + blo)    
    return(w01100101bs)
def pro():
    if host in w01100101bs:        
        print("\n" + n[0] + n[6] + n[21] + n[3] + n[11] + n[0] + n[15] + n[6] + n[6] + n[0] + host + n[0] + n[1] + n[18] + n[5] + n[0] + n[16] + n[18] + n[15] + n[20] + n[5] + n[3] + n[20] + n[5] + n[4] + n[27] + "\n")
        sys.exit(0)
    else:
        pass




#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#By Neo-Jack

import os
from os import system, name

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
#---------
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
#---------
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
#---------
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
#---------
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
#---------
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
#---------
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
#---------
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
#---------
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
#---------
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
    
#---------
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
#---------
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
#---------





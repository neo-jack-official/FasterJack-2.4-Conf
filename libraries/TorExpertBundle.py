#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#By Neo-Jack

import os
from os import system, name

def tor_inst():
    try:
        print("Trying to Install TOR-Network\n")
        #Debian, Ubuntu
        os.system("sudo apt-get install tor")
    except ImportError:
        print("Trying to Install TOR-Network\n")
        #etc
        os.system("apt-get install tor") #checar
    try:
        print("Trying to Install TOR-Network\n")
        #Fedora
        os.system("sudo dnf install tor")
    except ImportError:
        print("Trying to Install TOR-Network\n")
        #openSUSE
        os.system("sudo zypper install tor")

def torsocks_inst():
    try:
        print("Trying to Install TOR-Socks\n")
        #Debian, Ubuntu
        os.system("sudo apt-get install torsocks")
    except ImportError:
        print("Trying to Install TOR-Sock\n")
        #etc
        os.system("apt-get install torsocks") #checar
    try:
        print("Trying to Install TOR-Socks\n")
        #Fedora
        os.system("sudo dnf install torsocks")
    except ImportError:
        print("Trying to Install TOR-Socks\n")
        #openSUSE
        os.system("sudo zypper install torsocks")
        
def torgeoipdb_inst():
    try:
        print("Trying to Install TOR-Geoipdb\n")
        #Debian, Ubuntu
        os.system("sudo apt-get install tor-geoipdb")
    except ImportError:
        print("Trying to Install TOR-Geoipdb\n")
        #etc
        os.system("apt-get install tor-geoipdb") #checar
    try:
        print("Trying to Install TOR-Geoipdb\n")
        #Fedora
        os.system("sudo dnf install tor-geoipdb")
    except ImportError:
        print("Trying to Install TOR-Geoipdb\n")
        #openSUSE
        os.system("sudo zypper install tor-geoipdb")

def tor_run():
    try:
        print("Trying to Start TOR-Network\n")
        #Debian, Ubuntu
        os.system("sudo /etc/init.d/tor restart")
    except ImportError:
        print("Trying to Start TOR-Network\n")
        #etc
        os.system("/etc/init.d/tor restart") #checar
        
def apt_transport_https():
    try:
        print("Trying to Install apt-transport-https\n")
        #Debian, Ubuntu
        os.system("sudo apt install apt-transport-https")
    except ImportError:
        print("Trying to Install apt-transport-https\n")
        #etc
        os.system("apt install apt-transport-https") #checar
    try:
        print("Trying to Install apt-transport-https\n")
        #Fedora
        os.system("sudo dnf install apt-transport-https")
    except ImportError:
        print("Trying to Install apt-transport-https\n")
        #openSUSE
        os.system("sudo zypper install apt-transport-https")
        

        


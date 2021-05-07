#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#By Neo-Jack

#if say "Under Python 3" works on: Windos, LINUX: Debian, Ubuntu Fedora, OpenSUSE
#if say "Under LINUX" works on: Debian, Ubuntu Fedora, OpenSUSE
#If you running FasterJack as .EXE. check_tor_conf = "no"

# --- CONFIGURATION ---
language_conf = "es"        #Select Language: Options --> [default], [es], [en], [pt]
check_pip_config = "no"     #Check PIP to Install?: Options --> [yes] or [no]. only activate under Python 3
check_libraries_conf = "no" #Check libraries at Startup?: Options --> [yes] or [no]. only activate under python 3
check_tor_conf = "no"      #Check Tor Expert Bundle to Install?: Options --> [yes] or [no]. only activate under LINUX
#Default variables
port_conf = "443"            #Select default Port: Options --> [80] or [443]
clientes_conf = "135"        #Select default number of customers, recommended between [30 - 135]
Tor_conf = "on"            #Select default Tor-Network: Options --> [on] or [off]

#Malicious Package
package_conf = "normal"    #Malicious package, directly influences your internet consumption : Options --> [basic] or [normal] or [strong]

#Extra Notifications        (Off mode make work faster the Ddos)
conectando_conf = "off"     #Select if you want to see connected notification: Options --> [on] or [off]
reconectando_conf = "off"   #Select if you want to see re-connected notification: Options --> [on] or [off]
asignando_nuevo_conf = "off" #Select if you want to see notification of Assigning new Agent: Options --> [on] or [off]
agente_asignado_conf = "off" #Select if you want to see notification of Assigned Agent: Options --> [on] or [off]
forzar_agente_conf = "off"   #Select if you want to see notification of Force new Agent: Options --> [on] or [off]
package_send_it_conf = "off" #Select if you want to see package delivery notification: Options --> [on] or [off]
nueva_ip_asignada = "off"    #select if you want to see notification of new assigned ip: Options --> [on] or [off]
verif_host_conf = "off"      #select if you want to see host verification notification x each client: Options --> [on] or [off]

##From now on, Do not touch, if you do not know what you are doing.
# --- Ip-Checker ---
ipcheck_url1_conf = 'http://icanhazip.com'   # Service Ip-Checker 01 --> Do not modify, unless they fail.                check 06/may/2021
ipcheck_url2_conf = 'http://bot.whatismyipaddress.com'  # Service Ip-Checker 02 --> Do not modify, unless they fail.     check 06/may/2021 
ipcheck_url3_conf = 'https://ifconfig.me/ip' # Service Ip-Checker 03 --> Do not modify, unless they fail.                check 06/may/2021
ipcheck_url4_conf = 'https://ipinfo.io/ip'   # Service Ip-Checker 03 --> Do not modify, unless they fail.                check 06/may/2021
ipcheck_url5_conf = 'https://ipecho.net/plain'   # Service Ip-Checker 03 --> Do not modify, unless they fail.            check 06/may/2021
ipcheck_url6_conf = 'http://ident.me/'       # Service Ip-Checker 03 --> Do not modify, unless they fail.                check 06/may/2021
ipcheck_url7_conf = 'http://checkip.amazonaws.com/' # Service Ip-Checker 03 --> Do not modify, unless they fail.         check 06/may/2021
# --- Bots ---
bot_url1_conf = "https://html5.validator.nu/?doc="               # Service Bot 01 --> Do not modify, unless they fail. 
bot_url2_conf = "https://validator.w3.org/nu/?doc="              # Service Bot 02 --> Do not modify, unless they fail.
bot_url3_conf = "https://datayze.com/site-validator.php?domain=" # Service Bot 03 --> Do not modify, unless they fail.
bot_url4_conf = "https://validator.ampproject.org/#url="         # Service Bot 04 --> Do not modify, unless they fail.
bot_url5_conf = "https://validator.w3.org/check?uri="    # Service Bot 05 --> Do not modify, unless they fail.
# --- Others ---
headers_conf = "headers.txt"                 #Package Headers
#---------------------------------

# --- Gallery of Ip-Checkers -- if you need remplace it: ---
# http://smart-ip.net/myip           Down     check 06/may/2021
# http://bot.whatismyipaddress.com/  USED     check 06/may/2021
# http://whatismyip.akamai.com/      UP       check 06/may/2021
# http://ip.tyk.nu/                  UP       check 06/may/2021
# https://ipof.in/txt                UP       check 06/may/2021
# http://tnx.nl/ip                   DOWN     check 06/may/2021
# http://l2.io/ip                    UP       check 06/may/2021
# http://wgetip.com/                 UP       check 06/may/2021
# http://eth0.me/                    UP       check 06/may/2021
#http://icanhazptr.com               Problem  check 06/may/2021

# --- Gallery of Web validator
# http://www.feedvalidator.org/check.cgi?url=       DOWN  check 06/may/2021 
# https://www.scam-detector.com/validator/          DOWN  check 06/may/2021
# https://validator.nu/?doc=                        UP    check 06/may/2021


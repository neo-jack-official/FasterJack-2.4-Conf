# FasterJack-2.3-Conf
New Version of FasterJack 2.3 configurable

 FasterJack for Python 3 (fasterjack.py)
# It is a Denial Tool for Web-Servers by Neo-Jack JUN / 2020

## News

version 2.2
It incorporates:
1) New codeless working method like Windows version (Start with: python3 fasterjack.py)
2) New display
3) Configurable menu (config.py)
4) Multilanguage (English, Spanish, Portuges)
5) Library Installer and Verifier
6) Tor service verifier and installer (Tor Expert Bundle for LINUX)
7) Improved compatibility with Windows and Linux: Debian, Ubuntu, Fedora, openSUSE.
8) External library to edit language at ease "language / leng_default.py"
9) Direct association of ports to HTTP or HTTPS

## What is FasterJack?

In practice it is a denial or stress testing tool for websites.
The complexity of the program is based on the interaction with its internal sub-programs.
This allows better control of each aspect of the operation, with notifications of the processes in the selected language.
Incorporates within its functions:
Greater and more efficient Navigation Agents that are automatically assigned on each connection and re-connection of the client.
Allowing for higher efficiency, and lower detection rate. Which requires less clients to the minute of using the program.
In a range of 30 to 115 clients.
The package to send is basically a simple message that gives instructions to the server, partially editable in header.txt.

Verifier Bots, which are executed at the beginning to validate the website and / or port, reducing failures or using the program in phantom mode. Ghost mode is when you think you are using the program on a server but it was never that way.
It also contains an option to access the Socket5 or TOR connection, for your security. with IP verifier, to avoid phantom use of protection.

Implements the new socket.socket connection system (socket.AF_INET, socket.SOCK_STREAM) that has shown greater efficiency for the TCP connection.

Bot Methods are also incorporated, which allows using the program in GET, POST or RANDOM by default.
As usual in this type of applications, it uses a minimum of bandwidth, which is very useful to avoid exhausting our Internet capacity.

## How FasterJack Works
FasterJack sends a packet (header) for each client, with false information but that the server can recognize as valid but incomplete, when generating a connection.
Therefore, the Server will be waiting for the rest of the header, which will never arrive.
Servers are generally configured by default to wait approximately 120 seconds per client sending the package.
This causes each client to exhaust the logical resources of the server, until it is saturated and fails.


## What version of Python do you use?
Python 3.6

## How do I know which Python version I have?
* `python -V | python3 -V`


## How do I use it?

If `fasterjack.py` and its dependencies are on Desktop:
1) Open terminal, Type `cd Desktop`
2) Run under Python 3.6:
* `python3 fasterjack.py`




## Configuration options

In the "config.py" menu:
1) Language Selection
2) Verify and install PIP
3) Verify and install dependencies
4) Verify and install Tor service and https
5) Modify default values: Port
6) Modify default values: Clients
7) Modify default values: Activate or not TOR
8) Access to modification of Server Ip-Checker 1 and 2
9) Access to modify part of the package to be delivered

In the app:
1) Choose a Mandatory Website or IP
2) Select port [80 or 443] default: 80
3) Select if you want to Enable default Tor Network: Disabled
4) Select optimal number of clients [30-135] defect 60
5) Select Method between Get or Post defect: Random

## How do I know if I have Tor Network installed?
Open Terminal:
* `tor --version`




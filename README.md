# Client-to-Server-to-Client
Send data/messages from client to a server and then to a separate client in python :)

# Tutorial
HOW TO RUN TUTORIAL REAL QUICK!

Both the server and client script can then be run from the Command prompt (in Windows)
OR from bash Terminal (Linux users)

BEFORE USE go into each file you want to use, both server and client
CHANGE the IP "0.0.0.0" to the IP of the network you are using eg.
On the server files:

"""
def run_server():
    server_ip = "0.0.0.0"  # server hostname or IP address
"""

On the client files:

"""
def run_client(uname):
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "0.0.0.0"  # replace with the server's IP address
"""


ON WINDOWS set the file pull location by copying the the file location
In the terminal write out "cd " and after cd the files location.
(NOTE the server and client do not NEED to be in the same file to work


Set up a terminal tab and write out "python " and then the file name of the server you want to use
RECOMENDED SERVERS:
"server.py"
OR
"serverV3.py"

(NOTE any client should work with "server.py" or with "serverV3.py")


Set up another terminal tab and write out "python " and then the file name of the client you want to use
RECOMENDED CLIENTS:
"client.py"
OR
"clientV3.py"


If it is working after the first message from the client side the message
"
  New user receiving data (Test)
  TO LOAD MESSAGES OUTPUT *.* (Fullstop)
  LIMIT is 100 users
  SERVER 3 ONLY WORKDS WITH CLIENT V3
  by zach :)
"

FINAL NOTES:
	-Recomend using "V3.py" files as it should be the most updated version
	-"V2.py" is NOT reccomended to be used as the client side can suffer from errors 
	-To leave on client side send the message "close" and the server should respond, due to errors or other messages being sent through the message may need to be send multiple times 
	-In TEST folder there are just lines I didnt properly use in the main code, will NOT work if run i think 
	-THIS WAS MY FIRST THINGY so if it dont work IT AINT MY FAULT :(

 # RECOMEND TO USE
 Server and client side I reccomend using
RECOMENDED SERVERS:
"serverV3.py"

RECOMENDED CLIENTS:
"clientV3.py"

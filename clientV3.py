import socket
import sys
import select
import time

uname = input("ENTER USERNAME")

def run_client(uname):
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "0.0.0.0"  # replace with the server's IP address
    server_port = 8000  # replace with the server's port number
    # establish connection with server
    client.connect((server_ip, server_port))


    print("Receiving Data")
    response = client.recv(1024)
    response = response.decode("utf-8")
    time.sleep(0.5)
    print(response)
    
    try:
        while True:

            """
            print("Sending data")
            msg = sys.stdin.readline() 
            client.send(msg.encode("utf-8")[:1024])
            sys.stdout.write("<You>") 
            sys.stdout.write(msg) 
            sys.stdout.flush()
            """
            
            msg = input("Enter message: ")
            message_to_send = "<" + uname + "> " + msg
            client.send(message_to_send.encode("utf-8")[:1024])
            
            x = 0
            print("Receiving Data")
            for x in range(1):
                response = client.recv(1024)
                response = response.decode("utf-8")
                time.sleep(0.5)
            if response.lower() == "closed":
                break
            print(response)
                
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # close client socket (connection to the server)
        client.close()
        print("Connection to server closed")

run_client(uname)


#time.sleep(0.5)
"""
for interv in range(10):
    response = client.recv(1024)
    response = response.decode("utf-8")
    if response.lower() == "closed":
        break
    time.sleep(0.5)
                        
    print(response)
    interv = 9

            if interv == 'recv':
                print("Receiving Data")
                response = client.recv(1024)
                response = response.decode("utf-8")
            
                time.sleep(0.5)
                print(response)
                interv = 'send'
    

                
            if interv == 'send':
                print("Sending data")      
                msg = sys.stdin.readline() 
                client.send(msg.encode("utf-8")[:1024])
                sys.stdout.write("<You>") 
                sys.stdout.write(msg) 
                sys.stdout.flush()
                time.sleep(5)

                interv = 'recv'

"""

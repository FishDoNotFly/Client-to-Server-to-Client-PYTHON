import socket
import sys
import select
import time


interv = 0

def run_client():
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "192.168.68.115"  # replace with the server's IP address
    server_port = 8000  # replace with the server's port number
    # establish connection with server
    client.connect((server_ip, server_port))
    
    try:
        while True:
            if interv == 0:
                print("Receiving Data")
                
                time.sleep(0.5)
                for interv in range(10):
                    response = client.recv(1024)
                    response = response.decode("utf-8")
                    if response.lower() == "closed":
                        break
                    time.sleep(0.5)
                    
                print(response)
                interv = 9
                
            elif interv == 9:
                print("Sending data")
                
                for interv in range(2):
                    
                    msg = sys.stdin.readline() 
                    client.send(msg.encode("utf-8")[:1024])
                    sys.stdout.write("<You>") 
                    sys.stdout.write(msg) 
                    sys.stdout.flush()
                    time.sleep(3)
                    
                interv = 0
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # close client socket (connection to the server)
        client.close()
        print("Connection to server closed")

run_client()

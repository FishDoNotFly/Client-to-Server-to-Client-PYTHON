import socket
import sys
import select
import time
interv = 0

def run_client():
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "0.0.0.0"  # replace with the server's IP address
    server_port = 8000  # replace with the server's port number
    # establish connection with server
    client.connect((server_ip, server_port))

    try:
        while True:
            """
            # maintains a list of possible input streams 
            sockets_list = [sys.stdin, client] 
 
            read_sockets = sockets_list,[],[]
            for interv in range(10):
                interv + 1

            """
            
            for socks in read_sockets: 
                if socks == client:
                    
                    response = client.recv(1024)
                    response = response.decode("utf-8")
                    print(response)
                    if response.lower() == "closed":
                        break

                else:
                    msg = sys.stdin.readline() 
                    client.send(msg.encode("utf-8")[:1024])
                    sys.stdout.write("<You>") 
                    sys.stdout.write(msg) 
                    sys.stdout.flush()

        """
        while True:
            # get input message from user and send it to the server
            msg = input("Enter message: ")
            client.send(msg.encode("utf-8")[:1024])

            # receive message from the server
            response = client.recv(1024)
            response = response.decode("utf-8")
            

            # if server sent us "closed" in the payload, we break out of
            # the loop and close our socket
            if response.lower() == "closed":
                break

            #print(f"Received: {response}")
            print(response)
        """
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # close client socket (connection to the server)
        client.close()
        print("Connection to server closed")


run_client()


"""
while True: 
 
    # maintains a list of possible input streams 
    sockets_list = [sys.stdin, server] 
 
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 
 
    for socks in read_sockets: 
        if socks == server:
            message = socks.recv(2048) 
            print (message)         
            response = client.recv(1024)
            response = response.decode("utf-8")
            if response.lower() == "closed":
                break
            print(response)
       
        else: 
            msg = sys.stdin.readline() 
            client.send(msg.encode("utf-8")[:1024])
            sys.stdout.write("<You>") 
            sys.stdout.write(msg) 
            sys.stdout.flush()

"""

"""
                    message = socks.recv(2048) 
                    print (message)
                    
                    response = client.recv(1024)
                    response = response.decode("utf-8")
                    
                    if response.lower() == "closed":
                        break
                    else:
                        print(response)
                    
                
"""












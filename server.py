import socket
import threading


list_of_clients=[] #setting up list of clients

def handle_client(client_socket, addr):
    try:
        while True:
            # receive adnd print client messages
            request = client_socket.recv(1024).decode("utf-8")
            if request.lower() == "close":
                client_socket.send("closed".encode("utf-8"))   #close client side
                break
            
            print(f"Received: {request}")
            
            # convert and send accept response to the client
            """
            response = "accepted"
            client_socket.send(response.encode("utf-8"))
            """
            ##new additions
            
            message = request #so new code works
            
            print("<" + addr[0] + "> " + message)   #prints server side
            #message_to_send = "<" + addr[0] + "> " + message  #preparing message_to_send and broardcast to othr clients
            #message_to_send = "<" + addr[0] + "> " + message
            message_to_send = "<Client> " + message
            broadcast(message_to_send,client_socket) #conn =! to client_socket so changed
            #calls the function broadcast

            
    except Exception as e:
        print(f"Error when hanlding client: {e}") #error just in case ;)
    finally:
        client_socket.close()
        print(f"Connection to client ({addr[0]}:{addr[1]}) closed")  #ends connection with that client

def broadcast(message_to_send,connection):
    message = message_to_send
    for clients in list_of_clients: #chescks through all clients
        if clients!=connection:     #if not the main client, eg 1 sends message
            try:
                clients.send(message.encode("utf-8"))
            except:
                
                clients.close()
                
                #remove(clients)


def run_server():
    server_ip = "0.0.0.0"  # server hostname or IP address
    port = 8000  # server port number
    # create a socket object
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # bind the socket to the host and port
        server.bind((server_ip, port))
        # listen for incoming connections
        server.listen()
        print(f"Listening on {server_ip}:{port}")

        while True:
            # accept a client connection
            client_socket, addr = server.accept()
            list_of_clients.append(client_socket)
            print(f"Accepted connection from {addr[0]}:{addr[1]}")
            # start a new thread to handle the client
            thread = threading.Thread(target=handle_client, args=(client_socket, addr,))
            thread.start()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.close()



run_server()



"""
def broadcast(message,connection):
    for clients in list_of_clients:
        if clients!=connection:
            try:
                clients.send(message)
            except:
                
                clients.close()
                remove(clients)
"""

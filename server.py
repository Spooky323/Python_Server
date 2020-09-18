import socket
import threading

IP = "10.100.102.2"
HEADER = 64
PORT = 5555
FORMAT = 'utf-8'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = ('', PORT)
DISCONNECTED = "!DISCONNECTED"
server.bind(ADDR)
print("Socket Created")

def handle_client(conn, addr):
    print(f"New Connection on {addr}")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == "!DISCONNECTED":
                print(f"{addr} Has Disconnected")
                connected = False
            else:
                print(f"New Message received from {addr} : {msg}")

    conn.close()




def start():
    server.listen()
    print(f"Server is listening on {ADDR}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Current Connections {threading.activeCount() - 1}")

start()
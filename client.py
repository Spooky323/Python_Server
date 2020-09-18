import socket


IP = str(input("Enter IP : "))
PORT = 5556
HEADER = 64
FORMAT = 'utf-8'
ADDR = (IP, PORT)
DISCONNECTED = "!DISCONNECTED"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def send_message():
    print("Type ""exit"" to disconnected from the server")
    line = True
    while line:
        msg = input(f"{socket.gethostname()} : ")
        if msg == "exit":
            msg = DISCONNECTED
            line = False
        msg_length = len(msg)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(msg.encode(FORMAT))

def start():
    input("Press Any Key to Connect to the Server")
    client.connect(ADDR)
    print(f"Connected To Server {IP}")
    send_message()
    print("Disconnecting...")
    client.close()
start()
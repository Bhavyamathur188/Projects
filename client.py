import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected to server.")

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()

            if message.lower() == "exit":
                print("\nServer disconnected.")
                break

            print(f"\nServer: {message}")

        except:
            break

def send_messages():
    while True:
        message = input("You: ")

        client.send(message.encode())

        if message.lower() == "exit":
            break

threading.Thread(target=receive_messages).start()
threading.Thread(target=send_messages).start()
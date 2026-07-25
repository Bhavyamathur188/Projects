import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server is running...")
print(f"Listening on {HOST}:{PORT}")

client, address = server.accept()
print(f"Connected with {address}")

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()

            if message.lower() == "exit":
                print("\nClient disconnected.")
                break

            print(f"\nClient: {message}")

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
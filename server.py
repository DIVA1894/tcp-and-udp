# server.py

import os
import socket

HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 12345  # Port to listen on

# Function to receive the file over TCP
def receive_file_tcp(server_socket):
    with server_socket:
        file_name = server_socket.recv(1024).decode()
        with open(f'received_{file_name}', 'wb') as f:
            while True:
                data = server_socket.recv(1024)
                if not data:
                    break
                f.write(data)
        print(f"File {file_name} received successfully!")

# Function to receive the file over UDP
def receive_file_udp(server_socket):
    while True:
        data, addr = server_socket.recvfrom(1024)
        file_name = data.decode()
        with open(f'received_{file_name}', 'wb') as f:
            while True:
                data, addr = server_socket.recvfrom(1024)
                if not data:
                    break
                f.write(data)
        print(f"File {file_name} received successfully!")

# Function to start the TCP server
def start_tcp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"TCP Server listening on port {PORT}...")
        
        while True:
            conn, addr = server_socket.accept()
            print(f"Connection from {addr}")
            receive_file_tcp(conn)

# Function to start the UDP server
def start_udp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((HOST, PORT))
        print(f"UDP Server listening on port {PORT}...")

        while True:
            receive_file_udp(server_socket)

# Main entry for running either TCP or UDP server
if __name__ == "__main__":
    protocol = input("Enter protocol (TCP/UDP): ").strip().upper()
    
    if protocol == 'TCP':
        start_tcp_server()
    elif protocol == 'UDP':
        start_udp_server()
    else:
        print("Invalid protocol")

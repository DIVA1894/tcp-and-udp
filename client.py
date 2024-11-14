# client.py

import os
import socket

# Function to send the file over TCP
def send_file_tcp(file_path, server_ip, server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((server_ip, server_port))
        
        # Send the file name first
        file_name = os.path.basename(file_path)
        client_socket.send(file_name.encode())
        
        # Open the file and send its content
        with open(file_path, 'rb') as f:
            data = f.read(1024)
            while data:
                client_socket.send(data)
                data = f.read(1024)
        print("File sent successfully!")

# Function to send the file over UDP
def send_file_udp(file_path, server_ip, server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        file_name = os.path.basename(file_path)
        
        # Send the file name first
        client_socket.sendto(file_name.encode(), (server_ip, server_port))
        
        # Open the file and send its content
        with open(file_path, 'rb') as f:
            data = f.read(1024)
            while data:
                client_socket.sendto(data, (server_ip, server_port))
                data = f.read(1024)
        print("File sent successfully!")

# Function to handle the file transfer based on the protocol
def start_file_transfer(file_path, server_ip, server_port, protocol):
    if protocol == 'TCP':
        send_file_tcp(file_path, server_ip, server_port)
    elif protocol == 'UDP':
        send_file_udp(file_path, server_ip, server_port)
    else:
        print("Invalid protocol selected")

# Main entry to initiate file transfer from frontend
def send_file_to_server(file_path, server_ip, protocol):
    # Define the server port
    server_port = 12345

    # Start the file transfer
    start_file_transfer(file_path, server_ip, server_port, protocol)

# Example usage
if __name__ == "__main__":
    # Sample file to send (this would come from frontend)
    file_path = "path_to_file"  # Replace with actual file path
    server_ip = "server_ip_from_form"  # Replace with actual server IP
    protocol = "TCP"  # 'TCP' or 'UDP' (user-selected protocol)

    send_file_to_server(file_path, server_ip, protocol)

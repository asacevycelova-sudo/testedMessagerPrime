import socket
hostname = "google.com"
ip_address = socket.gethostbyname(hostname)

print(f"IP адрес {hostname}: {ip_address}")
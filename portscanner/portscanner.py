#!/usr/bin/python3

import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("[*] Enter the host to Scan: ")
port = int(input("[*] Enter the port to Scan: "))


def portscanner(port):
    if sock.connect_ex((host, port)):
        print(f"Port {port} is closed")
    else:
        print(f"Port {port} is open")


portscanner(port)

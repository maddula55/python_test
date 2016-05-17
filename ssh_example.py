#!/usr/bin/env python
import time
import paramiko

def main():
    IP= "50.76.53.27"
    username="pyclass"
    password="88newclass"
    port= 8022
    remote_conn_pre= paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_conn_pre.connect(IP, username=username, password=password, port=port, look_for_keys=False, allow_agent=False)
    remote_conn= remote_conn_pre.invoke_shell()
    #time.sleep(2)
    #remote_conn.send("\n")
    #time.sleep(2)
    remote_conn.send("show ip int brief\n")
    time.sleep(2)
    output= remote_conn.recv(5000)
    print output
if __name__ == "__main__":
	main()

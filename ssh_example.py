#!/usr/bin/env pyhton
import paramiko
import time

def main():
	ip = "50.76.53.27"
	username="pyclass"
	password="88newclass"
	remote_conn=paramiko.SSHClient()
	remote_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	remote_conn.connect(ip, username=username, password=password)
	remote_conn=remote_conn.invoke_shell()
	time.sleep(2)
	remote_conn.send("\n")
	remote_conn.send("show ip int brief\n")
	time.sleep(2)
	output = remote_conn.recv(5000)
	print output
if __name__ == "__main__":
	main()
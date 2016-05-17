#!/usr/bin/env python
import time
import paramiko
from getpass import getpass

def main():
    IP= "50.76.53.27"
    username="pyclass"
    password=getpass()
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
'''
handling ssh keys
paramiko won't connect to unknown hosts
we need to load the known hosts to connect(secure) or accept any keys(security issue)
remote_conn_pre.load_system_host_keys()

why invoke shell

stdin, stdout, stderr = remote_conn_pre.exec_command("sh ip int br\n")
print stdout.read()

after one command exec command will terminate the underlying tcp connection and apperently ssh session on cisco routers 
so we need to use invoke_shell() to execute multiple commands on the same ssh connection.

remote_conn.settimeout(6.0)
remote_conn.gettimeout()

connection times out if there is no receive data available and indefinitely if no time is set

remote_conn.recv_ready() --> to check if any data is available or not. returns boolean
use if condition to avoid timeouts

max we can read is 65535 bytes

remote_conn.send("q") --> to quit in middle of command like show run
remote_conn.send("terminal length 0\n") --> to disable paging

if output>65535
have some form of while loop until recv_ready is False  and use some wait time


introduce delays while writing in a script
'''


import telnetlib
import time
import socket
import sys
import getpass
from telnet_class import TelnetClass

ip_addr = raw_input("IP address: ")
ip_addr = ip_addr.strip()
username = 'pyclass'
password = getpass.getpass()
cmd = "show ip int br"
TELNET_PORT = 23
TELNET_TIMEOUT = 6

telnet_object=TelnetClass(ip_addr, username, password, TELNET_PORT, TELNET_TIMEOUT)


remote_conn = telnet_object.telnet_connect()
print telnet_object.login(remote_conn)

time.sleep(1)
remote_conn.read_very_eager()
telnet_object.disable_paging(remote_conn)

output = telnet_object.send_command(remote_conn, cmd)

print "\n\n"
print output
print "\n\n"

remote_conn.close()
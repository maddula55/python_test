#!/usr/bin/env python
'''
Write a script that connects to the lab pynet-rtr1, logins, and executes the
'show ip int brief' command.
'''

import telnetlib
import time
import socket
import sys
import getpass

class TelnetClass(object):
	def __init__(self, ip_addr, username, password, TELNET_PORT, TELNET_TIMEOUT):
		
		self.ip_addr = ip_addr
		self.username = username
		self.password = password
		self.TELNET_PORT = TELNET_PORT
		self.TELNET_TIMEOUT = TELNET_TIMEOUT
		

	def send_command(self, remote_conn, cmd):
		'''
		Send a command down the telnet channel
		Return the response
		'''
		cmd = cmd.rstrip()
		remote_conn.write(cmd + '\n')
		time.sleep(1)
		return remote_conn.read_very_eager()

	def login(self, remote_conn):
		'''
		Login to network device
		'''
		output = remote_conn.read_until("sername:", self.TELNET_TIMEOUT)
		remote_conn.write(self.username + '\n')
		output += remote_conn.read_until("ssword:", self.TELNET_TIMEOUT)
		remote_conn.write(self.password + '\n')
		return output

	def disable_paging(self, remote_conn, paging_cmd='terminal length 0'):
		'''
		Disable the paging of output (i.e. --More--)
		'''
		return self.send_command(remote_conn, paging_cmd)

	def telnet_connect(self):
		'''
		Establish telnet connection
		'''
		try:
			return telnetlib.Telnet(self.ip_addr, self.TELNET_PORT, self.TELNET_TIMEOUT)
		except socket.timeout:
			sys.exit("Connection timed-out")


	

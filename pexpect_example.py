#!/usr/bin/env python
#useful for interactive nodes like n/w elements and eleminates some problems with paramiko

import pexpect
import sys
import re
def main():
	IP= "50.76.53.27"
    username="pyclass"
    password=getpass()
    port= 8022
	
	ssh_conn = pexpect.spawn("ssh -l {} {} -p {}".format(username, ip_addr, port))
	#ssh_conn.logfile = sys.stdout
	ssh_conn.timeout =3
	ssh_conn.expect('ssword:')
	ssh_conn.sendline(password)
	ssh_conn.expect("#")
	print ssh_conn.before
	print ssh_conn.after
	
	ssh_conn.sendline("sh ip int br")
	ssh_conn.expect("#")
	print ssh_conn.before
	
	ssh_conn.sendline("sh version")
	ssh_conn.expect("pynet-rtr#")
	print ssh_conn.before
	
	
	try:
		ssh_conn.sendline("show version")
		ssh_conn.expect("zzzz")
	except pexpect.TIMEOUT:
		print "timeout occured"
	
	pattern = re.compile(r"^Lic.*DI:*$", re.MULTILINE)
	# the re says start with Lic match any sequece of zero or more char (.*), then ends with DI:, any seq zero or more char, the  end of line ($), multiline matches line by line
	
	ssh_conn.sendline("show version")
	ssh_conn.excpect(pattern)
	print ssh_conn.after
		
if __name__ == "__main__"
	main()
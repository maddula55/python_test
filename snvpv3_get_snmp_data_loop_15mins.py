from snmpv3_exercise1_week3_yaml import get_snmpv3_data, write_output
import snmp_helper
import time
import yaml
import os.path
import email_helper

def config_change_time(file):
	with open(file) as f:
		a=yaml.load(f)
	if a[-1]["ccmHistoryRunningLastChanged"] == a[-2]["ccmHistoryRunningLastChanged"]:
		print "nothing changed on the router in the last 2 polled intervals"
	if a[-1]["ccmHistoryRunningLastChanged"] != a[-2]["ccmHistoryRunningLastChanged"]:
		time_diff = int(a[-1]["sysUptime"]) - int(a[-1]["ccmHistoryRunningLastChanged"])
		c=time_diff/6000
		print "running config changed %s minutes ago"% c
		return c
	

if __name__ == "__main__":
	config_update_oids=(("ccmHistoryRunningLastChanged", '1.3.6.1.4.1.9.9.43.1.1.1.0'),
	('ccmHistoryRunningLastSaved','1.3.6.1.4.1.9.9.43.1.1.2.0'),
	('ccmHistoryStartupLastChanged','1.3.6.1.4.1.9.9.43.1.1.3.0'),
	("sysUptime", '1.3.6.1.2.1.1.3.0'))
	IP = "50.76.53.27"
	a_user="pysnmp"
	auth_key = "galileo1"
	encrypt_key= "galileo1"
	snmp_user = (a_user, auth_key, encrypt_key)
	pynet_rtr1 = (IP, 7961)
	pynet_rtr2 = (IP, 8061)
	'''
	i=0
	
	while True:
		output = get_snmpv3_data(config_update_oids, pynet_rtr2, snmp_user)
		write_output("config_change_data.yaml",output)
		time.sleep(900)
		i+=1
		if i==2:
			break
	'''			
	time_diff=config_change_time("config_change_data.yaml")
	recipient = 'gowtham.maddula@gmail.com'
	subject = 'config chanage'
	message = "rtr2 changed config at approximately %s minutes ago" % time_diff
	sender = 'ktbyers@twb-tech.com'
	email_helper.send_mail(recipient, subject, message, sender)
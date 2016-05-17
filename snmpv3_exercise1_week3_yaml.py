import snmp_helper
import time
import yaml
import os.path
import email_helper

def get_snmpv3_data(config_update_oids, pynet_rtr1, snmp_user):
	dict_result = {}
	for i,j in config_update_oids:
		snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr1, snmp_user, oid=j)
		output = snmp_helper.snmp_extract(snmp_data)
		#print "%s %s"%(i, output)
		dict_result.update({i:output})
	return dict_result
def write_output(file,output):
	if os.path.isfile(file):
		##open the file and load the contents##
		f_read=open(file, "r")
		a=yaml.load(f_read)
		f_read.close()
		##open file in write mode, add the new object and dump the contents ##
		f_write=open(file, "w")
		a.append(output)
		yaml.dump(a, f_write)
		f_write.close()
	##create file if there isn't one##
	elif os.path.isfile(file)==False:
		f=open(file, "w")
		a = [output]
		yaml.dump(a, f)
		f.close()
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
	
	##loop to get data##
	
	i=0
	
	while True:
		output = get_snmpv3_data(config_update_oids, pynet_rtr2, snmp_user)
		write_output("config_change_data.yaml",output)
		time.sleep(900)
		i+=1
		if i==2:
			break
		
	##sending email###
	time_diff=config_change_time("config_change_data.yaml")
	recipient = 'gowtham.maddula@gmail.com'
	subject = 'config chanage'
	message = "rtr2 changed config at approximately %s minutes ago" % time_diff
	sender = 'gowtham.maddula@gmail.com'
	email_helper.send_mail(recipient, subject, message, sender)
	
	

	
	
		
	


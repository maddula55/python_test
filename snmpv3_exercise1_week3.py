import snmp_helper
import time
import pickle

def get_snmpv3_data(config_update_oids, pynet_rtr1, snmp_user):
	dict_result = {}
	for i,j in config_update_oids:
		snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr1, snmp_user, oid=j)
		output = snmp_helper.snmp_extract(snmp_data)
		#print "%s %s"%(i, output)
		dict_result.update({i:output})
	return dict_result
	
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
	output = get_snmpv3_data(config_update_oids, pynet_rtr1, snmp_user)
	#print output
	f=open("config_change_data.pkl", "ab")
	pickle.dump(output, f)
	f.close()
	g=open("config_change_data.pkl","rb")
	a=pickle.load(g)
	b=pickle.load(g)
	print a
	print b
	g.close()
	
		
	


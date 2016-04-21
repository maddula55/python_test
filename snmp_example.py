#!/usr/bin/env python

from snmp_helper import snmp_get_oid, snmp_extract


COMMUNITY_STRING = "galileo"
SNMP_PORT_r1 = 7961
SNMP_PORT_r2 = 8061

def snmp_get_data(nw_element_tuple, oid):
	snmp_data = snmp_get_oid(nw_element_tuple, oid=oid)
	output = snmp_extract(snmp_data)
	return output


def main():
	sys_desc_oid = "1.3.6.1.2.1.1.1.0"
	sys_name_oid = "1.3.6.1.2.1.1.5.0"
	ip = "50.76.53.27"
	pynet_rtr1 = (ip, COMMUNITY_STRING, SNMP_PORT_r1)
	pynet_rtr2 = (ip, COMMUNITY_STRING, SNMP_PORT_r2)
	
	rtr1_sys_desc=snmp_get_data(pynet_rtr1, sys_desc_oid)
	print "rtr1 description"+"\n\n"+rtr1_sys_desc+"\n\n"
	rtr1_sys_name=snmp_get_data(pynet_rtr1, sys_name_oid)
	print "rtr1 system name "+"\n\n"+rtr1_sys_name+"\n\n"
	
	
	rtr2_sys_desc=snmp_get_data(pynet_rtr2, sys_desc_oid)
	print "rtr2 description"+"\n\n"+rtr2_sys_desc+"\n\n"

	rtr2_sys_name=snmp_get_data(pynet_rtr2, sys_name_oid)
	print "rtr2 system name"+"\n\n"+rtr2_sys_name+"\n\n"
#	print rtr2_sys_name
	
if __name__ == "__main__":
	main()
	
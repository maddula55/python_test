#!/usr/bin/env python

import snmp_helper

if True:
	IP = "50.76.53.27"
	a_user="pysnmp"
	auth_key = "galileo1"
	encrypt_key= "galileo1"
	snmp_user = (a_user, auth_key, encrypt_key)
	pynet_rtr1 = (IP, 7961)
	pynet_rtr2 = (IP, 8061)

snmp_oids = (
("ifInOctets", "1.3.6.1.2.1.2.2.1.10.5", True),
("ifOutOctets", "1.3.6.1.2.1.2.2.1.16.5", True),
("ifInUcastPkts", "1.3.6.1.2.1.2.2.1.11.5", True),
("ifOutUcastPkts", "1.3.6.1.2.1.2.2.1.17.5", True),
("ifSpeed", "1.3.6.1.2.1.2.2.1.5.5", True)
)

for desc,an_oid,is_count in snmp_oids:
	snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr1, snmp_user, oid=an_oid)
	output = snmp_helper.snmp_extract(snmp_data)
	print "%s %s"%(desc, output)

# function snmp_get_oid_v3 is part of snmp helper module 

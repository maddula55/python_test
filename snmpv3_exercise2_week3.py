from snmpv3_exercise1_week3_yaml import get_snmpv3_data, write_output

import time
import yaml
import pygal


def delta_calculator(list):
	a=[]
	for j in range(len(list)):
		if j < len(list)-1:
			a.append(list[j+1]-list[j])
	return a

	
if __name__=="__main__":
	interface_stat_oids=(('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5'),
	('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5'),
	('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5'),
	('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5'),
	('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5'))
	IP = "50.76.53.27"
	a_user="pysnmp"
	auth_key = "galileo1"
	encrypt_key= "galileo1"
	snmp_user = (a_user, auth_key, encrypt_key)
	pynet_rtr1 = (IP, 7961)
	pynet_rtr2 = (IP, 8061)
	
	
#	for i in range(12):
#		output = get_snmpv3_data(interface_stat_oids, pynet_rtr1, snmp_user)
#		write_output("interface_stat_data.yaml",output)
#		time.sleep(300)
	with open("interface_stat_data.yaml") as f:
		a=yaml.load(f)
	p=[]
	q=[]
	r=[]
	s=[]
	

	for i in a:
		p.append(int(i["ifInOctets_fa4"]))
		q.append(int(i["ifOutOctets_fa4"]))
		r.append(int(i["ifInUcastPkts_fa4"]))
		s.append(int(i["ifOutUcastPkts_fa4"]))
	
	fa4_in_octets=delta_calculator(p)
	fa4_out_octets=delta_calculator(q)
	fa4_in_packets=delta_calculator(r)
	fa4_out_packets=delta_calculator(s)
	
	# Create a Chart of type Line
	line_chart = pygal.Line()

	# Title
	line_chart.title = 'Input/Output Packets and Bytes'

	# X-axis labels (samples were every five minutes)
	line_chart.x_labels = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60']

	# Add each one of the above lists into the graph as a line with corresponding label
	line_chart.add('InPackets', fa4_in_packets)
	line_chart.add('OutPackets',  fa4_out_packets)
	line_chart.add('InBytes', fa4_out_octets)
	line_chart.add('OutBytes', fa4_in_octets)

	# Create an output image file from this
	line_chart.render_to_file('test.svg')



from ciscoconfparse import CiscoConfParse
import re

			
def interface_to_connected_map(source_file, target_file):
	int_ref = CiscoConfParse(source_file)
	list_with_connected_name=int_ref.find_objects_w_child(parentspec=r"interface ethernet", childspec=r"port-name")
	with open(target_file, "w") as f:
		f.write("")
	for i in list_with_connected_name:
		for j in i.children:
			if "port-name" in j.text:
				k = re.search(r"port-name (.+)", j.text)
				m = k.group(1)
				with open(target_file, "a") as f:		
					l = i.text+"  connected network element is: " + m  +"\n"
					f.write(l)



#interface_to_connected_map("r1_fo_acc4.log","r1_fo_acc4_interface_connections.txt")

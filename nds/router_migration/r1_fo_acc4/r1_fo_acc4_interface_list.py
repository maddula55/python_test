from ciscoconfparse import CiscoConfParse

def conf_int_iterator(list_int):
	for i in list_int:
		print i.text
		with open("r1_fo_acc4_interface_list.txt", "a") as f:
			f.write(i.text)
			f.write("\n")
		conf_int_iterator(i.children)

			


int_ref = CiscoConfParse("r1_fo_acc4.log")
list_int=int_ref.find_objects(r"^interface")

conf_int_iterator(list_int)

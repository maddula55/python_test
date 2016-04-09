from ciscoconfparse import CiscoConfParse
conf_ref = CiscoConfParse("../pynet/pyth_ans_ecourse/class1/cisco_ipsec.txt")
print conf_ref
crypto_map=conf_ref.find_objects(r"^crypto map")
print '''
crypto map entries
'''

for j in crypto_map:
    print j.text
    for p in j.children:
        print p.text
print '''
crypto map entries with pfs group 2
 '''
for j in crypto_map:
    for p in j.children:
        if "pfs group2" in p.text:
            print j.text
print '''
crypto map entries with AES protection
'''

for j in crypto_map:
    for p in j.children:
        if "transform-set" in p.text:
            if "AES-SHA" in p.text:
                print j.text
                print p.text



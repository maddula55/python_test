from ciscoconfparse import CiscoConfParse
conf_ref = CiscoConfParse("lb1-bo-acc4.log")

vs_ref=conf_ref.find_objects(r"virtual-server")

def func_parse(vs_ref):
    for j in vs_ref:
        print j.text
        with open("vs_list.txt", 'a') as f:
            f.write(j.text)
            f.write("\n")
        func_parse(j.children)

func_parse(vs_ref)            

for j in vs_ref:
    for p in j.children:
        if "pfs group2" in p.text:
            print " " 

for j in vs_ref:
    for p in j.children:
        if "transform-set" in p.text:
            if "AES-SHA" not in p.text:
                r = p.text.split()
                for q in r:
                    if "transform-set" == q:
                        print "%s : encrption is %s" %(j.text, r[r.index(q)+1])

                



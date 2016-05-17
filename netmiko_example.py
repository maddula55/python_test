from netmiko import ConnectHandler
from getpass import getpass
password = getpass()


# define network dictionaries
pynet1 = {
"device_type" : "cisco_ios",
"ip" : "50.76.53.27",
"username" : "pyclass",
"password": password
}

pynet2 = {
"device_type" : "cisco_ios",
"ip" : "50.76.53.27",
"username" : "pyclass",
"password": password,
"port":8022
}

juniper_srx = {
"device_type" : "juniper",
"ip" : "50.76.53.27",
"username" : "pyclass",
"password": password,
"secret":"",
"port":9822
}

# create network connection
pynet_rtr1 = ConnectHandler(**pynet1)
#** will pass dictionary key value pairs as arguments to function
pynet_rtr2 = ConnectHandler(**pynet2)
srx = ConnectHandler(**juniper_srx)

# netstat -an | grep 50.76.53.27
# dir(pynet_rtr1)
'''
functions
pynet_rtr1.find_prompt() --> to see the prompt
pynet_rtr1.config_mode() --> to enter config mode
pynet_rtr1.check_config_mode() --> returns boolean
pynet_rtr1.exit_congig_mode()
out=pynet_rtr1.send_command("show version")
print out
## netmiko takes care of paging

##executing change

config_commands = ["logging buffered 19999"]
pynet_rtr1.send_config_set(config_commands)
out = pynet_rtr1.send_command("show run | i logging")
print out

pynet_rtr1.find_prompt()
pynet_rtr1.send_command("wr memory")
## can also do it from a file

#juniper
srx.find_prompt()
config_commands= ["set system host-name test123"]
out = srx.send_config_set(config_commands)
srx.commit()

#ssh dispatcher --> to see supported devices
# other libraries --> trigger, xscript etc..


from  netmiko import ConnectHandler

router = {
'device_type': 'cisco_ios',
'host': 'sandbox-iosxe-latest-1.cisco.com',
'username':'admin',
'password': 'C1sco12345',
'secret': '',
'port': 22,
}

conn = ConnectHandler(**router)


clock= conn.send_command("show clock")
print (clock)

interface=  conn.send_command("show ip int br ")

with open ("interfaces.txt","w") as file :
	file.write(interface)
print ("interfaces.txt")

commands = [
	"interface loopback 8",
	"ip address 10.8.8.8 255.255.255.240",
	"no shutdown"
]

configuration= conn.send_config_set(commands)
print (configuration)

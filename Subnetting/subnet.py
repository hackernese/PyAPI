'''
	Calculating the network Address + Broadcast Address + The hosts range
	Author : Zenix Blurryface
	Version : v0.1
'''

Mask = {
	"255.0.0.0":8,
	"255.128.0.0":9,
	"255.192.0.0":10,
	"255.224.0.0":11,
	"255.240.0.0":12,
	"255.248.0.0":13,
	"255.252.0.0":14,
	"255.254.0.0":15,
	"255.255.0.0":16,
	"255.255.128.0":17,
	"255.255.192.0":18,
	"255.255.224.0":19,
	"255.255.240.0":20,
	"255.255.248.0":21,
	"255.255.252.0":22,
	"255.255.254.0":23,
	"255.255.255.0":24,
	"255.255.255.128":25,
	"255.255.255.192":26,
	"255.255.255.224":27,
	"255.255.255.240":28,
	"255.255.255.248":29,
	"255.255.255.252":30
}

def getnetworkaddr(address=None, netmask=None, auto=False): # Get the network address
	if auto and ( address or netmask ): 
		raise ValueError("too many arguments once once auto is set to True")
	elif auto:
		import sys
		if sys.platform=='win32':

			import subprocess
			
			netmaski = subprocess.check_output(["ipconfig"]).decode()
			
			try:
				netmask = netmaski.split("Subnet Mask . . . . . . . . . . . : ")[1].split("\r\n")[0]
				address = netmaski.split("IPv4 Address. . . . . . . . . . . : ")[1].split("\r\n")[0]
			except IndexError:
				raise SystemError("Unable to identify the subnet mask and the local IPv4")
		elif sys.platform=="linux":
			pass
		else:
			raise SystemError("Unsupported platform : %s" % sys.platform)
	elif not address or not netmask:
		raise TypeError("getrangeaddr() missing 2 positional arguments: 'address' and 'netmask'")

	import ipaddress, socket 

	try:
		socket.inet_aton(address)
	except (socket.error, OSError):
		raise TypeError("Invalid IP Address %s" % address)

	if netmask not in Mask:
		raise TypeError("Invalid netmask Address %s" % netmask)

	if not ipaddress.ip_address(address).is_private:
		raise TypeError("Not a private address %s " % address)

	address = [(maskoct & addroct) for maskoct, addroct in zip(
			map(int , netmask.split(".")), 
			map(int , address.split("."))
		)
	]
	
	return ".".join(map(str, address))


def getbroadcast(address=None, netmask=None, auto=False): # Get the broadcast address
	if auto and ( address or netmask ): 
		raise ValueError("too many arguments once once auto is set to True")
	elif auto:
		import sys
		if sys.platform=='win32':

			import subprocess
			
			netmaski = subprocess.check_output(["ipconfig"]).decode()
			
			try:
				netmask = netmaski.split("Subnet Mask . . . . . . . . . . . : ")[1].split("\r\n")[0]
				address = netmaski.split("IPv4 Address. . . . . . . . . . . : ")[1].split("\r\n")[0]
			except IndexError:
				raise SystemError("Unable to identify the subnet mask and the local IPv4")
		elif sys.platform=="linux":
			pass
		else:
			raise SystemError("Unsupported platform : %s" % sys.platform)
	elif not address or not netmask:
		raise TypeError("getbroadcast() missing 2 positional arguments: 'address' and 'netmask'")

	import ipaddress, socket 

	try:
		socket.inet_aton(address)
	except (socket.error, OSError):
		raise TypeError("Invalid IP Address %s" % address)

	if netmask not in Mask:
		raise TypeError("Invalid netmask Address %s" % netmask)

	if not ipaddress.ip_address(address).is_private:
		raise TypeError("Not a private address %s " % address)

	octet = "".join(["0"*(8-len(i[2:])) + i[2:] for i in map(bin,map(int, address.split(".")))])[:Mask[netmask]]
	octet = octet + (32-len(octet))*"1"
	octet = [
		int(octet[:8]   ,2),
		int(octet[8:16] ,2),
		int(octet[16:24],2),
		int(octet[24:]  ,2)
	]
	
	return ".".join(map(str, octet))



def getrangeaddr(address=None, netmask=None, auto=False): # Get the hosts range in the current network
	if auto and ( address or netmask ): 
		raise ValueError("too many arguments once once auto is set to True")
	elif auto:
		import sys
		if sys.platform=='win32':

			import subprocess
			
			netmaski = subprocess.check_output(["ipconfig"]).decode()
			
			try:
				netmask = netmaski.split("Subnet Mask . . . . . . . . . . . : ")[1].split("\r\n")[0]
				address = netmaski.split("IPv4 Address. . . . . . . . . . . : ")[1].split("\r\n")[0]
			except IndexError:
				raise SystemError("Unable to identify the subnet mask and the local IPv4")
		elif sys.platform=="linux":
			pass
		else:
			raise SystemError("Unsupported platform : %s" % sys.platform)
	elif not address or not netmask:
		raise TypeError("getrangeaddr() missing 2 positional arguments: 'address' and 'netmask'")

	import ipaddress, socket 

	try:
		socket.inet_aton(address)
	except (socket.error, OSError):
		raise TypeError("Invalid IP Address %s" % address)

	if netmask not in Mask:
		raise TypeError("Invalid netmask Address %s" % netmask)

	if not ipaddress.ip_address(address).is_private:
		raise TypeError("Not a private address %s " % address)

	octet = "".join(["0"*(8-len(i[2:])) + i[2:] for i in map(bin,map(int, address.split(".")))])[:Mask[netmask]]
	octet = octet + (32-len(octet))*"1"
	octet = [                                                    # Extracting the broadcast address of the local network
		int(octet[:8]   ,2),
		int(octet[8:16] ,2),
		int(octet[16:24],2),
		int(octet[24:]  ,2)-1
	]
	address = [(maskoct & addroct) for maskoct, addroct in zip(  # Extracting the network address
			map(int , netmask.split(".")), 
			map(int , address.split("."))
		)
	]
	address[-1] = address[-1] + 1

	return (
		".".join(map(str, address)),
		".".join(map(str, octet))
	)

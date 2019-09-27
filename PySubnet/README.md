# PySubnet
---
+ Caculating the network address + broadcast address and the hots range
+ Version 0.1

#### Manual :
---
+ getnetworkaddr(address=None, netmask=None, auto=False)
    + => Caculate the network address
        + address : Your local IPv4
        + netmask : Your Subnet mask
        + auto    : Automatically identify the address and the netmask then calculate it ( remember to omit 'address' and 'netmask' if this argument is set to True )
+ getbroadcast(address=None, netmask=None, auto=False)
    + => Caculate the broadcast address
        + address : Your local IPv4
        + netmask : Your Subnet mask
        + auto    : Automatically identify the address and the netmask then calculate it ( remember to omit 'address' and 'netmask' if this argument is set to True )
+ getrangeaddr(address=None, netmask=None, auto=False)
    + => Caculate the hosts range
        + address : Your local IPv4
        + netmask : Your Subnet mask
        + auto    : Automatically identify the address and the netmask then calculate it ( remember to omit 'address' and 'netmask' if this argument is set to True )
#### Usage :
---
```sh
>> import pysubet         # Importing the function
>> pysubet.getnetworkaddr("192.168.0.1", "255.255.255.0") # Network address
192.168.0.0
>> pysubet.getbroadcast("192.168.0.1", "255.255.255.0") # Broadcast address
192.168.0.255
>> pysubet.getrangeaddr("192.168.0.1", "255.255.255.0") # Hosts range
('192.168.0.1', '192.168.0.254')

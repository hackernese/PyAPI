# Pywinreg
---
-  Basically winreg but with an enumerating feature which collects all sub-registry and registry paths of a specific registry ( including hive ) 
-  Version 0.1 
#### Manual :
---
You will first need to initialize an instance of the `EnumRegistry` class ( pywinreg.EnumRegistry ) to access its methods ( `EnumRegKey` or `EnumRootKey` )

##### pywinreg.py ( Inner codes )

```py
# pywinreg.py
class EnumRegistry:

    def __init__(self, root, strict=True):
        self.SubDir   = []
        self.strict   = strict
        self.rootname = root
        self.root     = __class__.Hives[root]
    ...
```
- **root** : name of the hive/root registry you wanna enumerate ( Ex : "HKEY_LOCAL_MACHINE", "HKEY_CURRENT_CONFIG", ... )
- **strict** : define whether the enumeration requires strict rule, exception or not ( `True` or `False` ) 
    - `True` : Enumerate with strict rule, means if there is an error it will instantly raise it 
    - `False` : Enumerate loosely, means there will be some errors which once encountered, it won't be raised ( like `PermissionError` which is encountered once you enumerate a registry without escalated or suited privilege )
##### How to initialize : 
```py
import pywinreg
regobj = pywinreg.EnumRegistry("hive") # Create an instance to enumerate
```
 Once initialized you can now use its method to enumerate registries and collect its sub-registries
##### pywinreg.py ( Inner codes / instance's methods )
```py
    def EnumRegKey(self, KeyName):
        ...
    def EnumRootKey(self):
        ...
```
+ ###### `ignore "self", when you use the function you can see it with only one parameter and any value you pass in will be placed into KeyName`
+ **EnumRegKey** : Enumerate through a specific registry and collect its sub-registries
    + **KeyName** : name of a specific registry you wanna enumerate ( if it's a sub-registry you need to pass in the full path )
+ **EnumRootKey** : Enumerate through an entire hive ( root registry )
    + ( No value should be passed, it will automatically enumerate once it's simply called )
##### How to call : 
+ Using ***EnumRegKey*** method
```py
import pywinreg
regobj = pywinreg.EnumRegistry("hive")       # Create an instance to enumerate
All_registry = regobj.EnumRegKey("registry") # Create an enumerator
for reg in All_registry:                     # Loop through the enumerator
    print(reg)                               # Print out the registry
```
+ Using ***EnumRootKey*** method
```py
import pywinreg
regobj = pywinreg.EnumRegistry("hive")  # Create an instance to enumerate
All_registry = regobj.EnumRootKey()     # Create an enumerator
for reg in All_registry:                # Loop through the enumerator
    print(reg)                          # Print out the registry
```
> emember to replace "hive" and "registry" with real values 
---
#### Usage :
---
> Say... you wanna enumerate through every registry and its sub-registry in ***HKEY_CURRENT_CONFIG***
##### enumroot.py ( example )
```py
import pywinreg
regobj = pywinreg.EnumRegistry("HKEY_CURRENT_CONFIG")  # Create an instance to enumerate
All_registry = regobj.EnumRootKey()     # Enumerator of HKEY_CURRENT_CONFIG
for reg in All_registry:                # Loop through the enumerator
    print(reg)                          # Print out the registry
```
##### enumroot.py ( Output )
```
System
System\CurrentControlSet
System\CurrentControlSet\Control
System\CurrentControlSet\Control\Print
System\CurrentControlSet\Control\Print\Printers
System\CurrentControlSet\Control\VIDEO
System\CurrentControlSet\Control\VIDEO\{2D5BA881-99A8-4757-A06E-CB5493B97A39
System\CurrentControlSet\Control\VIDEO\{2D5BA881-99A8-4757-A06E-CB5493B97A39
00
System\CurrentControlSet\Control\VIDEO\{2D5BA881-99A8-4757-A06E-CB5493B97A39
00\Mon12345678
...
```
> Now say... you wanna enumerate through every registry and its sub-registry of **System\CurrentControlSet\SERVICES** inside **HKEY_CURRENT_CONFIG**
##### enumreg.py ( example )
```py
import pywinreg
regobj = pywinreg.EnumRegistry("HKEY_CURRENT_CONFIG")  # Create an instance to enumerate
All_registry = regobj.EnumRegKey("System\\CurrentControlSet\\SERVICES")     # Enumerator of HKEY_CURRENT_CONFIG
for reg in All_registry:                # Loop through the enumerator
    print(reg)                          # Print out the registry
```
##### enumreg.py ( Output )
```
System\CurrentControlSet\SERVICES
System\CurrentControlSet\SERVICES\TSDDD
System\CurrentControlSet\SERVICES\TSDDD\DEVICE0
System\CurrentControlSet\SERVICES\VGASAVE
System\CurrentControlSet\SERVICES\VGASAVE\DEVICE0
```
---
####  Error Messages : 
---
> There are a few tracebacks or error messages which you may encounter when you misdo something 
##### PermissionError : 
+ When you try to access a registry which is forbidden or can only accessed with a valid privilege 
##### FileNotFoundError :
+ When you try to access an unavailable registry ( non-existing )
##### OSError :
+ When you try to support an unsupported hive ( root registry ) like when your system doesn't support **HKEY_DYN_DATA** but you try to enumerate it 
##### KeyError :
+ Similar to OSError but the only difference is OSError means the hive name you pass in is not supported on your system but it *could be* supported by the others, but KeyError is when you pass in a totally invalid piece of text which can't be determined which hive it is 




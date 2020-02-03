from winreg import *

class EnumRegistry:

    def __init__(self, root, strict=True):
        self.SubDir   = []
        self.strict   = strict
        self.rootname = root
        self.root     = __class__.Hives[root]

    Hives = { # If you enum a non-existing one it will return an empty list
        "HKEY_PERFORMANCE_DATA":HKEY_PERFORMANCE_DATA,
        "HKEY_CURRENT_CONFIG"  :HKEY_CURRENT_CONFIG,
        "HKEY_DYN_DATA"        :HKEY_DYN_DATA,
        "HKEY_USERS"           :HKEY_USERS,
        "HKEY_LOCAL_MACHINE"   :HKEY_LOCAL_MACHINE,
        "HKEY_CURRENT_USER"    :HKEY_CURRENT_USER,
        "HKEY_CLASSES_ROOT"    :HKEY_CLASSES_ROOT
    }
    reg = None

    def __IsSubReg(self,Key): # Please don't poke !!!
        try:
            registry = OpenKey(self.root, Key, 0, KEY_READ)
            EnumKey(registry, 0)
            return True
        except OSError:
            return False

    def EnumRegKey(self, KeyName): # I totally forgot how i wrote this amazing shit .-.
        count  = 0
        errora = None
        try:
            currentn = "\\".join(self.SubDir + [KeyName])
            reg = OpenKey(self.root, currentn, 0, KEY_READ)# OPen registry
            yield currentn
            while 1:
                name = EnumKey(reg, count)
                count += 1
                if self.__IsSubReg("\\".join(self.SubDir + [KeyName,name])):
                    self.SubDir.append(KeyName)
                    data_registry = self.EnumRegKey(name)
                    for i in data_registry:
                        yield i
                else:
                    yield "\\".join(self.SubDir + [KeyName, name])
        except OSError as error: # Either permission or it's out of thing to loop\
            if (isinstance(error, PermissionError) and self.strict) or isinstance(error, FileNotFoundError):
                errora = error
            else:
                self.SubDir.pop() if self.SubDir else None
        if errora:
            raise type(errora)(errora)

    def EnumRootKey(self):
        int_key = 0
        _return_root = []
        erroraise = False
        try:
            while 1:
                reg = EnumKey(self.root,int_key)
                for i in self.EnumRegKey(reg):
                    yield i
                int_key += 1
                self.SubDir=[]
        except OSError as error:
            if isinstance(error, PermissionError) or "reg" not in locals():
                erroraise = error
        if erroraise:
            raise type(erroraise)(erroraise)

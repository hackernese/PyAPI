

''''
            ( You can omit these lines when you implement )
-------------------------------------------------------------------------
    Description : Reading files backward, both text and binary files
    Author : Zenix Blurryface
    Date   : 2/9/2019
    Release: v0.1
-------------------------------------------------------------------------
'''

class bopen:

    File_Size  = None # Please don't touch
    Size_Lines = None # This as well, keep your dirty hand out :P

    def __init__(self, file, mode): # Initialize an object for reading

        self.file = file
        self.mode = mode
        self.IgnoreCondition = False
        import os

        if mode not in ("r", "rb"):
            raise ValueError("This function is used for reading only")
            return
        self.FileObject = open(self.file, self.mode)
        __class__.File_Size = self.ConstantSize = __class__.Size_Lines = os.path.getsize(self.file)

    def read(self,byte=None,reverse=None): # REading the files

        if self.IgnoreCondition:

            if not byte:
                return self.FileObject.read()[::(-1 if reverse else 1)]
            if type(byte)!=int:
                raise TypeError("integer argument expected, got '%s' ( byte )" % type(byte).__name__)
            if reverse and type(reverse) not in (bool, int):
                raise TypeError("integer argument expected, got '%s' ( reverse )" % type(reverse).__name__)

        if __class__.File_Size<0:
            return ("" if self.mode == "r" else b"")
        elif (__class__.File_Size-byte)<0:
            self.FileObject.seek(0)
            self.Data = self.FileObject.read(__class__.File_Size)[::(1 if not reverse else -1)]
            __class__.File_Size -= byte
            return self.Data
        else:
            __class__.File_Size -= byte
            self.FileObject.seek(__class__.File_Size)
            return self.FileObject.read(byte)[::(1 if not reverse else -1)]

    def readlines(self, line=None, reverse=None): # Reading the files in lines

        if not line:
            return self.FileObject.readlines()[::-1]
        if type(line)!=int:
            raise TypeError("integer argument expected, got '%s' ( byte )" % type(byte).__name__)
        if reverse and type(reverse) not in (bool, int):
            raise TypeError("integer argument expected, got '%s' ( reverse )" % type(reverse).__name__)

        self.n = 0
        self.minus = 1
        self.data = NULL = ("" if self.mode=="r" else b"")

        while(line!=0):
            inte = self.ConstantSize-self.minus
            self.FileObject.seek(0 if inte < 0 else inte)
            self.char = self.FileObject.read(1)
            self.minus += 1
            if self.char==("\n" if self.mode=="r" else b"\n") or self.FileObject.read(1)==NULL or inte < 0:
                self.n += 1
            if self.n==2:
                line -= 1
                if line!=0:
                    self.data = NULL
                self.n = 1
            if self.n==1:
                self.data += self.char

        self.FileObject.seek(__class__.File_Size)
        return [self.data[::(-1 if not reverse else 1)][1:]]

    def close(self): # Closing the file
        self.FileObject.close()

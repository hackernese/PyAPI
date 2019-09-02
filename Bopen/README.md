# Bopen
---
-  Reading a text or binary file backward
-  Version 0.1 
#### Manual :
---
Initializing a file object --> bopen(file, mode)
* `mode` : "r" or "rb" ( read text file or binary file )
* `file` : The file you wanna read
* Functions :
    * read(`byte`=None, `reverse`=None) :
    * => Read some bytes out of the files ( backward )
        * `byte` : How many bytes you wanna read ( None for all )
        * `reverse` : Reverse the bytes once you read them ( None for no reversing )
    * readlines(`lines`=None, `reverse`=None) :
    * => Read some lines out of the files ( backward )
        * `lines` : Which line you wanna read ( None for all lines )
        * `reverse` : Reverse the line once you read them ( None for no reversing )
    * close() :
    * => Closing the file
#### Usage :
---
example.txt : 
>Line 1 (first line )
>line 2 ( something )
>line 3 ( final )

Testcase ( read all ) :
```sh
>> from Bopen import bopen         # Importing the function
>> file = bopen("exmaple.txt", "r")# open up a file
>> data = file.read()               # Read all bytes within it
>> file.close() # Closing the file # Close the file
>> print(data) 
```
Output :
>) lanif ( 3 enil
>) gnihtemos ( 2 enil
>) enil tsrif( 1 eniL

Testcase 2 ( 5 bytes ):
```sh
>> from Bopen import bopen         # Importing the function
>> file = bopen("exmaple.txt", "r")# open up a file
>> data = file.read(5)             # Read 5 bytes within it
>> file.close() # Closing the file # Close the file
>> print(data) 
```
Output :
> eniL

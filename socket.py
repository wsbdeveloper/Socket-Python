#!/usr/bin/python
import socket
try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(("HOST", port INT))
        #ex s.connect(("192.168.1.40", 80))
        
        if s :
            print "porta aberta"
        else :
            print "porta fechada"
except:
        print "ocorreu um erro!"
       
#Socket simples!

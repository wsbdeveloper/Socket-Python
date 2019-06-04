#!/usr/bin/python
import socket
try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(("HOST", port INT))
        
        if s :
            print "porta aberta"
        else :
            print "porta fechada"
except:
        print "ocorreu um erro!"
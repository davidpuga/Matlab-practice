#!/usr/bin/env python

import socket # python library
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create internet socket. create stream socket to receive ordered information
mysock.connect( ('www.pythonlearn.com', 80) )
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n') # HTTP/1.0 will include the HTTP headers. If it's not present, only the content (and not the metadata) of the website will be transmitted

while True:
	data = mysock.recv(512) # receive up to 512 characters
	if ( len(data) < 1 ) : 	# when there is nothing more to transmit
		break
	print data

mysock.close()	
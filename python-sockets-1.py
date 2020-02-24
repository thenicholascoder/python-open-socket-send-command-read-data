#import the socket library
import socket

#create a socket(it is like a file handler)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect socket across the internet
#use the method from the created handler .connect with domain name of 'data.pr4e.org' and second parameter of tuple is port 80
#this is a function call with single tuple parameter 
#tuple[0] = 'data.pr4e.org'
#tuple[1] = 80
mysock.connect(('data.pr4e.org', 80))

#this is going to go to the link
#send http rules, followed by end of line\n , followed by another \n,
#.encode() is UNICODE to UTFA bytes converter
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

#then send
mysock.send(cmd)

#while indefinite loop
while True:

    #receive up to 512 characters and store to data
    data = mysock.recv(512)

    #filter if data is last line
    #data is 0 when it is the last line
    if len(data) < 1:

        #break if filter is met
        break

    #print data with decode()
    #decode() = UTFA to internal data UNICODE converter
    print(data.decode(),end='')

#when done close the connection
mysock.close()


telnet data.pr4e.org 80
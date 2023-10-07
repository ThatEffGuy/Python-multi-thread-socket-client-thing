#import socket module
import socket

def Main():
    # local host IP 127.0.0.1
    host = '127.0.0.1'

    #define the port you want to connect 
    port = 12345

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #connect to server on local PC
    s.connect((host,port))

    #message you send to the server
    message = "we are the hnc cyber group at ayrshire college"

    while True:

        #message sent to the server
        s.send(message.encode('ascii'))

        #message recieved from the server
        data = s.recv(1024)

        #print the recieved message
        #here it would be the reverse of the send message
        print('recieved from the server : ',str(data.decode('ascii')))

        #ask the client whether he wants to continue
        ans = input('\n do you want to continue Y/N: ')
        if ans == 'y':
            continue
        else:
            break

    #close the connection
    s.close()

if __name__ == '__main__':
    Main()
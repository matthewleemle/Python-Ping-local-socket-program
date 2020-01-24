from socket import *
import time

clientSocket = socket(AF_INET,SOCK_DGRAM)
clientSocket.settimeout(1)
clientSocket.bind(('localhost', 1024))


for i in range(0,10):
    message = 'ping'
    start = time.time()
    clientSocket.sendto(message.encode(),('localhost',12000))

    try: 
        message, address = clientSocket.recvfrom(12000)
        timepassed = time.time() - start
        print(i," " ,message.decode())
        print("round trip is " + str(timepassed) + "seconds")
    except:
        print('timeout, ', i)

clientSocket.close()

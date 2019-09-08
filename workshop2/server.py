import socket
from _thread import *
import threading
import datetime
import time


print_lock = threading.Lock()


def threaded(c):
    for i in range(5):
        msg = 'Welcome at '+str(time.time())
        c.send(msg.encode('ascii'))
        time.sleep(3)
    c.close()


def main():

    host = socket.gethostname()
    port = 8888

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((host, port))

    serversocket.listen(5)

    while True:

        clientsocket, addr = serversocket.accept()
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        start_new_thread(threaded, (clientsocket,))

    serversocket.close()


if __name__ == '__main__':
    main()

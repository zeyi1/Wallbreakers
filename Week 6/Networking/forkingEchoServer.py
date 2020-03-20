import os
import sys
import time
import socket
import multiprocessing


def echo(sock, seconds):
    print(f'Child process with id: {os.getpid()} has been created.')
    print(f'Sleeping for {seconds} seconds.')
    time.sleep(seconds)
    print('Done sleeping.')

    while True:
        # Establish a connection with the client.
        connection, client_address = sock.accept()

        # Receive message from client
        data = connection.recv(1024)
        msg = data.decode('utf-8')
        echoMessage = ''

        if data:
            echoMessage = f"Child pid {os.getpid()} echo'd: {msg}."
            print(echoMessage)
        # Send a message to the client
        connection.send(bytes(echoMessage, 'utf-8'))
        
        connection.close()  
        break  
    
    
if __name__ == '__main__':
    # Creating a socket for IPv4 using TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('Socket has been successfully created.')

    port = 9001

    try:
        sock.bind(('', port))
        print(f'Socket has been binded to port: {port}.')
    except socket.error as e:
        print(str(e))

    sock.listen(5)
    print('Socket is now listening.')

    processes = []
    print(f'\nInside Parent Process with id: {os.getpid()}.\n')

    for _ in range(3):     
        pid = multiprocessing.Process(target=echo, args=[sock, 3])
        pid.start()
        processes.append(pid)
      
    for process in processes:
        process.join()

    sock.close()
    sys.exit()
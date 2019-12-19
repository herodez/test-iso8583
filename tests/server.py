import socket

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 3000))
    sock.listen()

    while True:
        con, con_addr = sock.accept()
        while True:
            data = con.recv(16)
            print(data)

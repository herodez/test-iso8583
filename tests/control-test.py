from settings import CONNECTION_SETTINGS
import socket

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Connecting to Host:{host} and Port:{port}'.format(host=CONNECTION_SETTINGS['host'],
                                                             port=CONNECTION_SETTINGS['port']))
    sock.connect((CONNECTION_SETTINGS['host'], CONNECTION_SETTINGS['port']))
    print('Connection successful')
    byarray = bytearray([0x01, 0x23, 0x60, 0x00, 0x01, 0x80, 0x00, 0x02,
                         0x00, 0xb0, 0x38, 0x45, 0x00, 0x00, 0xc0, 0x10,
                         0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x43,
                         0xe2, 0x00, 0x30, 0x00, 0x00, 0x00, 0x00, 0x00,
                         0x00, 0x16, 0x00, 0x11, 0x31, 0x15, 0x06, 0x25,
                         0x07, 0x23, 0x59, 0x96, 0x08, 0x01, 0x00, 0x05,
                         0x32, 0x39, 0x30, 0x30, 0x30, 0x31, 0x31, 0x30,
                         0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x38, 0x33,
                         0x31, 0x33, 0x37, 0x36, 0x20, 0x20, 0x20, 0x4a,
                         0x61, 0x87, 0x72, 0x95, 0x3f, 0xce, 0x4b, 0x00,
                         0x84, 0x30, 0x33, 0x4d, 0x32, 0x34, 0x30, 0x32,
                         0x30, 0x30, 0x30, 0x35, 0x30, 0x30, 0x30, 0x33,
                         0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30,
                         0x30, 0x30, 0x30, 0x30, 0x31, 0x33, 0x44, 0x32,
                         0x36, 0x30, 0x30, 0x39, 0x39, 0x30, 0x30, 0x30,
                         0x30, 0x30, 0x32, 0x32, 0x30, 0x36, 0x35, 0x39,
                         0x33, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30,
                         0x30, 0x30, 0x30, 0x55, 0x32, 0x33, 0x30, 0x30,
                         0x30, 0x30, 0x30, 0x35, 0x32, 0x30, 0x30, 0x33,
                         0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30,
                         0x30, 0x30, 0x30, 0x30, 0x31, 0x00, 0x06, 0x30,
                         0x30, 0x30, 0x30, 0x35, 0x35, 0x00, 0x24, 0x30,
                         0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30,
                         0x30, 0x31, 0x33, 0x30, 0x30, 0x30, 0x30, 0x30,
                         0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x31, 0x00,
                         0x27, 0x32, 0x31, 0x30, 0x30, 0x30, 0x30, 0x30,
                         0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x32, 0x33,
                         0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30,
                         0x30, 0x30, 0x30, 0x30, 0x00, 0x04, 0x31, 0x30,
                         0x37, 0x35, 0x00, 0x40, 0xdc, 0xcc, 0x1c, 0x16,
                         0xe8, 0xd4, 0x45, 0xda, 0x20, 0xa2, 0xe7, 0x39,
                         0xf7, 0xa6, 0xd4, 0x8c, 0x34, 0x6e, 0xdf, 0x2a,
                         0xfe, 0xf9, 0x76, 0x9b, 0x0c, 0xe7, 0x6a, 0xfa,
                         0x03, 0xd6, 0x00, 0xc4, 0xc1, 0xb8, 0xb0, 0xfa,
                         0x75, 0xa7, 0x5e, 0x78, 0x00, 0x08, 0x12, 0x34,
                         0x56, 0x78, 0x90, 0xab, 0xcd, 0xef, 0x00, 0x05,
                         0x32, 0x2e, 0x30, 0x2e, 0x31])
    sock.sendall(byarray)

    data = b''
    while True:
        print('Receiving data...')
        dataRc = sock.recv(CONNECTION_SETTINGS['BUFFER_SIZE'])
        if dataRc:
            data += dataRc
            print('Data Receiving end')
            break

    print(data)
    sock.close()

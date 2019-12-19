from settings import CONNECTION_SETTINGS
import iso8583
import socket
from iso8583.specs import default


def generate_network_message():
    default['h'] = {
        "data_enc": "b",
        "len_enc": "b",
        "len_type": 0,
        "max_len": 7,
        "desc": "Message Header"
    }
    doc_dec = {}
    iso8583.add_field(doc_dec, 't', '0800')
    iso8583.add_field(doc_dec, '11', '000001')
    iso8583.add_field(doc_dec, '37', '001234567910')
    iso8583.add_field(doc_dec, '70', '270')
    iso8583.add_field(doc_dec, 'h', "002E6000018000")

    return iso8583.encode(doc_dec, spec=default)


if __name__ == '__main__':
    message, dec = generate_network_message()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Connecting to Host:{host} and Port:{port}'.format(host=CONNECTION_SETTINGS['host'],
                                                             port=CONNECTION_SETTINGS['port']))
    sock.connect((CONNECTION_SETTINGS['host'], CONNECTION_SETTINGS['port']))
    sock.sendall(message)
    bytearray = bytearray([0x00, 0x2e, 0x60, 0x00, 0x01, 0x80, 0x00, 0x30,
                          0x38, 0x30, 0x30, 0x80, 0x20, 0x00, 0x00, 0x08,
                          0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x30, 0x30, 0x30, 0x30, 0x30,
                          0x31, 0x30, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35,
                          0x36, 0x37, 0x39, 0x31, 0x30, 0x32, 0x37, 0x30])
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

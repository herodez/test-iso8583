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
    iso8583.add_field(doc_dec, 'h', "2E3D0000000000")

    return iso8583.encode(doc_dec, spec=default)


if __name__ == '__main__':
    message, _ = generate_network_message()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Connecting to Host:{host} and Port:{port}'.format(host=CONNECTION_SETTINGS['host'],
                                                             port=CONNECTION_SETTINGS['port']))
    sock.connect((CONNECTION_SETTINGS['host'], CONNECTION_SETTINGS['port']))
    print('Connection successful')
    sock.sendall(message)

    data = b''
    while True:
        print('Receiving data...')
        dataRc = sock.recv(CONNECTION_SETTINGS['BUFFER_SIZE'])
        if not dataRc:
            print('Data Receiving end')
            break
        data += dataRc

    print(data)
    sock.close()

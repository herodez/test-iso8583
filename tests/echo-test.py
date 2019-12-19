from settings import CONNECTION_SETTINGS
import iso8583
import socket
from iso8583.specs import default


def generate_network_message():
    doc_dec = {}
    iso8583.add_field(doc_dec, 't', '0800')
    iso8583.add_field(doc_dec, '11', '000001')
    iso8583.add_field(doc_dec, '37', '001234567910')
    iso8583.add_field(doc_dec, '70', '270')

    return iso8583.encode(doc_dec, spec=default)


if __name__ == '__main__':
    message, _ = generate_network_message()
    print(type(message))

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Connecting to Host:{host} and Port:{port}'.format(host=CONNECTION_SETTINGS['host'],
                                                             port=CONNECTION_SETTINGS['port']))
    sock.connect((CONNECTION_SETTINGS['host'], CONNECTION_SETTINGS['port']))
    message = '0046'.encode('ascii') + '`'.encode('ascii') + '000000'.encode('ascii') + message
    sock.sendall(message)

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

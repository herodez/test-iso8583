from settings import CONNECTION_SETTINGS
from speficifications.specifications import MEDIANET_SPECIFICATION
import iso8583
import socket
import pprint
from iso8583.specs import default


MEDIANET_SPECIFICATION = {
    "h": {"data_enc": "b", "len_enc": "b", "len_type": 0, "max_len": 7, "desc": "Message Header"},
    "t": {"data_enc": "b", "len_enc": "b", "len_type": 0, "max_len": 2, "desc": "Message Type"},
    "p": {"data_enc": "b", "len_enc": "b", "len_type": 0, "max_len": 8, "desc": "Bitmap, Primary"},
    "1": {"data_enc": "b", "len_enc": "b", "len_type": 0, "max_len": 8, "desc": "Bitmap, Secondary"},
    "11": {"data_enc": "b", "len_enc": "b", "len_type": 0, "max_len": 12, "desc": "System Trace Audit Number"},
    "37": {"data_enc": "b", "len_enc": "b", "len_type": 0, "max_len": 6, "desc": "Retrieval Reference Number"},
    "70": {"data_enc": "b", "len_enc": "b", "len_type": 0, "max_len": 6}
}


def generate_network_message():
    doc_dec = {}
    iso8583.add_field(doc_dec, 't', '0800')
    iso8583.add_field(doc_dec, '11', '000000010010001110000010')
    iso8583.add_field(doc_dec, '37', '001234567910')
    iso8583.add_field(doc_dec, '70', '001001110000')
    iso8583.add_field(doc_dec, 'h', "002E6000018000")

    return iso8583.encode(doc_dec, spec=MEDIANET_SPECIFICATION)


if __name__ == '__main__':
    message, dec = generate_network_message()

    # control_test_data = "012360000180000200b038450000c0101000000000000043e2003000000000000016001131150625072359960801000532393030303131303030303030303833313337362020204a618772953fce4b008430334d3234303230303035303030333030303030303030303030303133443236303039393030303030323230363539333030303030303030303055323330303030303532303033303030303030303030303030310006303030303535002430303030303030303030313330303030303030303030303100273231303030303030303030303032333030303030303030303030300004313037350040dccc1c16e8d445da20a2e739f7a6d48c346edf2afef9769b0ce76afa03d600c4c1b8b0fa75a75e7800081234567890abcdef0005322e302e31".replace(
    #     ' ', '')
    # read_type_data = "00 84 60 54 45 53 54 02 00 f0 3c 45 00 00 c0 80 10 00 00 00 00 00 00 41 00 16 51 81 72 35 01 70 80 17 00 30 00 00 00 00 00 09 00 01 23 82 14 24 41 06 11 21 01 05 43 00 11 00 05 43 4e 50 30 30 31 30 31 30 30 30 30 30 30 38 36 37 36 34 30 20 20 20 09 78 00 24 30 32 30 30 30 30 30 30 30 37 30 30 30 37 31 30 30 30 30 30 30 30 32 35 00 06 30 30 30 39 36 32 00 14 31 35 30 30 30 30 30 30 30 30 30 39 30 30".replace(' ', '')
    # data_test = '0200B038470000C0021000000000000043E20030000000000018730041951935200905581400510001000533313135313938353030303030303837303534392020200136FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF008430334D32343032303030353030303330303030303030303030303031324432363030393930303030303235303635393330303030303030303030553233303030303035303030333030303030303030303030303100063030303238330024303030303030303031363732303030303030303030303030001431313030303030303030303230310004464646460040FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF0008FFFFFFFFFFFFFFFF0005322E302E31'
    # s = b'0200\x40\x10\x00\x00\x00\x00\x00\x00161234567890123456123456'
    # dec, dec_scp = iso8583.decode(bytearray.fromhex(control_test_data), spec=MEDIANET_SPECIFICATION)
    # dec, dec_scp = iso8583.decode(control_test_data, spec=MEDIANET_SPECIFICATION)
    # pprint.pprint(dec_scp)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Connecting to Host:{host} and Port:{port}'.format(host=CONNECTION_SETTINGS['host'],
                                                             port=CONNECTION_SETTINGS['port']))
    print(message)
    sock.connect((CONNECTION_SETTINGS['host'], CONNECTION_SETTINGS['port']))
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

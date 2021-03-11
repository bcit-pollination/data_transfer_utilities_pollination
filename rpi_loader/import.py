import os
import sys
from cryptography.fernet import Fernet
from common import load_key
def decrypt_data(keyfile, input_path):
    os.system('./decode-crc32 {}encoded_data.txt > decoded_data.txt'.format(input_path))

    with open('decoded_data.txt', 'rb') as file:
        data = file.read()

    key = load_key(keyfile)
    f = Fernet(key)
    decrypted_msg = f.decrypt(data)
    print(decrypted_msg.decode('ascii'));
    # encrypt_output_file = open('./data.json', "wb" )
    # encrypt_output_file.write(decrypted_msg)
    # encrypt_output_file.close()


decrypt_data(sys.argv[1], sys.argv[2])
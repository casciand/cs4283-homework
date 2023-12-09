import argparse
import socket
import sys
import time

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding


def driver(args):
    for i in args.hosts:
        print(f'----------Intermediate {i + 1} ----------')

        print('Connecting socket...')
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((f'10.0.0.{i + 2}', int(args.port)))
        print('Connected!')

        # Generate RSA keys
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        public_key = private_key.public_key()
        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        # Send RSA public key
        client_socket.sendall(pem)
        print('Sent RSA public key')

        #  Receive Fernet (symmetric) key
        encrypted_symmetric_key = client_socket.recv(1024)
        print('Received key:', encrypted_symmetric_key)
        symmetric_key = private_key.decrypt(
            encrypted_symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        print('Decrypted symmetric key:', symmetric_key)

        # Encrypt message
        plaintext = b'SECRET MESSAGE'
        print('Plaintext:', plaintext)
        f = Fernet(symmetric_key)
        ciphertext = f.encrypt(plaintext)
        client_socket.sendall(ciphertext)
        print('Sent ciphertext:', ciphertext)

        client_socket.close()


def parse_args():
    # Parse the command line
    parser = argparse.ArgumentParser()

    # Add optional arguments
    parser.add_argument("-n", "--hosts", type=int, default=3,
                        help="Number of intermediate hosts (default: 3)")
    parser.add_argument("-p", "--port", type=int, default=5556,
                        help="Port that server is listening on (default: 5556)")
    args = parser.parse_args()

    return args


def main():
    parsed_args = parse_args()
    driver(parsed_args)


if __name__ == '__main__':
    main()

import argparse
import socket
import sys
import time

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding


def driver(args):
    host_num = int(args.addr[-1])

    print('---------- Key Exchange ----------\n')

    print('Binding socket...')
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((args.addr, int(args.port)))

    print('Listening for connections...')
    server_socket.listen(1)
    client_socket, client_address = server_socket.accept()
    print(f'Connection established with {client_address}')

    # Receive client RSA public key
    pem = client_socket.recv(1024)
    print('Received RSA public key!')
    public_key = serialization.load_pem_public_key(pem)

    #  Generate Fernet (symmetric) key
    symmetric_key = Fernet.generate_key()
    encrypted_symmetric_key = public_key.encrypt(
        symmetric_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    client_socket.sendall(encrypted_symmetric_key)
    print('Sent encrypted symmetric key:', encrypted_symmetric_key)

    print('---------- Unwrapping the Onion ----------\n')

    # Close sockets
    client_socket.close()
    server_socket.close()

    # Establish connection with previous node
    print('Binding socket...')
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((args.addr, int(args.port)))

    print('Listening for connections...')
    server_socket.listen(1)
    prev_socket, prev_address = server_socket.accept()
    print(f'Connection established with {prev_address}')

    # Receive and decrypt single layer of encryption
    ciphertext = prev_socket.recv(1024)
    print('Received wrapped ciphertext:', ciphertext)
    f = Fernet(symmetric_key)
    message = f.decrypt(ciphertext)
    print('Decrypted single layer:', message)

    # Establish connection with next node
    print('\nConnecting socket...')
    next_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    next_socket.connect((f'10.0.0.{host_num + 1}', int(args.port)))

    next_socket.sendall(message)

    server_socket.close()
    prev_socket.close()
    next_socket.close()


def parse_args():
    # Parse the command line
    parser = argparse.ArgumentParser()

    # Add optional arguments
    parser.add_argument("-i", "--intf", default="*", help="Interface to bind to (default: *)")
    parser.add_argument("-p", "--port", type=int, default=5556, help="Port to bind to (default: 5556)")
    parser.add_argument("-a", "--addr", default="127.0.0.1",
                        help="IP Address to connect to (default: localhost i.e., 127.0.0.1)")
    args = parser.parse_args()

    return args


def main():
    parsed_args = parse_args()
    driver(parsed_args)


if __name__ == '__main__':
    main()

import argparse
import socket
import sys
import time

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding


def driver(args):
    symmetric_keys = []
    entry_node_addr = '10.0.0.2'
    packet_size = 1024

    start_time_1 = time.time()

    for i in range(args.hosts):
        print(f'---------- Intermediate {i + 1} ----------\n')

        print('Connecting socket...')
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((f'10.0.0.{i + 2}', int(args.port)))

        # Generate RSA keys
        print('Generating new RSA key pair...')
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
        print('Sent RSA public key!')

        #  Receive Fernet (symmetric) key
        encrypted_symmetric_key = client_socket.recv(packet_size)
        print('Received encrypted Fernet key:', encrypted_symmetric_key)
        symmetric_key = private_key.decrypt(
            encrypted_symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        symmetric_keys.append(symmetric_key)
        print('Decrypted Fernet key:', symmetric_key)
        print()

        client_socket.close()

    print('---------- Wrapping the Onion ----------\n')

    # Encrypt message
    message = b'SECRET MESSAGE'
    print('Plaintext:', message)

    start_time_2 = time.time()

    for i, key in enumerate(reversed(symmetric_keys)):
        f = Fernet(key)
        message = f.encrypt(message)
        print(f'Encrypted Message (Layer {i + 1}):', message)

    # Establish connection with entry host
    print('\nConnecting socket...')
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((entry_node_addr, int(args.port)))

    # Send wrapped message
    try:
        size = bytes(str(len(message)), 'utf-8')
        client_socket.sendall(size)
        client_socket.sendall(message)
    except err:
        print(err)

    print(f'Sent wrapped message to {entry_node_addr} (with {args.hosts} layers of encryption!)\n')

    print('---------- Unwrapping the Onion ----------\n')

    # Receive wrapped response
    message_size = client_socket.recv(packet_size).decode('utf-8')
    message_size = int(message_size)

    response = client_socket.recv(message_size)
    recv_length = len(response)
    while message_size - recv_length > 0:
        response += client_socket.recv(message_size - recv_length)
        recv_length = len(response)

    # response = client_socket.recv(packet_size)
    print('Received wrapped response:', response)

    # Unwrap the onion
    for i, key in enumerate(symmetric_keys):
        f = Fernet(key)
        response = f.decrypt(response)
        print(f'Decrypted Response (Layer {len(symmetric_keys) - i}):', response)

    # Calculate latencies
    end_time = time.time()
    print(f'\nEnd-to-end latency (including key exchange): {end_time - start_time_1:.3f}')
    print(f'End-to-end latency (NOT including key exchange): {end_time - start_time_2:.3f}')

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

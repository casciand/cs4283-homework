import argparse
import sys
import time

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
import zmq


def driver(args):
    try:
        context = zmq.Context()
    except zmq.ZMQError as err:
        print("ZeroMQ Error: {}".format(err))
        return
    except:
        print("Some exception occurred getting context {}".format(sys.exc_info()[0]))
        return

    # Create socket
    try:
        socket = context.socket(zmq.REQ)
        connection_addr = "tcp://" + args.addr + ":" + str(args.port)
        socket.connect(connection_addr)
    except zmq.ZMQError as err:
        print("ZeroMQ Error obtaining context: {}".format(err))
        return
    except:
        print("Some exception occurred getting REQ socket {}".format(sys.exc_info()[0]))
        return

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
    socket.send(pem)
    print('Sent RSA public key')

    #  Receive Fernet (symmetric) key
    encrypted_symmetric_key = socket.recv()
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
    socket.send(ciphertext)
    print('Sent ciphertext:', ciphertext)


def parse_args():
    # parse the command line
    parser = argparse.ArgumentParser()

    # add optional arguments
    parser.add_argument("-a", "--addr", default="127.0.0.1",
                        help="IP Address to connect to (default: localhost i.e., 127.0.0.1)")
    parser.add_argument("-p", "--port", type=int, default=5556,
                        help="Health port that server is listening on (default: 5556)")
    args = parser.parse_args()

    return args


def main():
    parsed_args = parse_args()
    driver(parsed_args)


if __name__ == '__main__':
    main()

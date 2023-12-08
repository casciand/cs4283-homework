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
        print("ZeroMQ Error obtaining context: {}".format(err))
        return
    except:
        print("Some exception occurred getting context {}".format(sys.exc_info()[0]))
        return

    # Create socket
    try:
        socket = context.socket(zmq.REP)
        connection_addr = "tcp://" + args.intf + ":" + str(args.port)
        socket.bind(connection_addr)
    except zmq.ZMQError as err:
        print("ZeroMQ Error obtaining REP socket: {}".format(err))
        return
    except:
        print("Some exception occurred getting REP socket {}".format(sys.exc_info()[0]))
        return

    # Receive client RSA public key
    pem = socket.recv()
    print('Received RSA public key from client')
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
    socket.send(encrypted_symmetric_key)
    print('Sent encrypted symmetric key:', encrypted_symmetric_key)

    # Decrypt ciphertext
    ciphertext = socket.recv()
    print('Received ciphertext:', ciphertext)
    f = Fernet(symmetric_key)
    plaintext = f.decrypt(ciphertext)
    print('Decrypted message:', plaintext)


def parse_args():
    # parse the command line
    parser = argparse.ArgumentParser()

    # add optional arguments
    parser.add_argument("-i", "--intf", default="*", help="Interface to bind to (default: *)")
    parser.add_argument("-p", "--port", type=int, default=5556, help="Port to bind to (default: 5556)")
    args = parser.parse_args()

    return args


def main():
    parsed_args = parse_args()
    driver(parsed_args)


if __name__ == '__main__':
    main()

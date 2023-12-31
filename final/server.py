import argparse
import socket
import sys
import time


def driver(args):
    packet_size = 1024

    # Establish connection with previous node
    print('Binding socket...')
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((args.addr, int(args.port)))

    print('Listening for connections...')
    server_socket.listen(1)
    prev_socket, prev_address = server_socket.accept()
    print(f'Connection established with {prev_address}')

    # Receive and send response
    message_size = prev_socket.recv(4).decode('utf-8')
    message_size = int(message_size)

    message = prev_socket.recv(message_size)
    recv_length = len(message)
    while message_size - recv_length > 0:
        message += prev_socket.recv(message_size - recv_length)
        recv_length = len(message)

    # message = prev_socket.recv(packet_size)
    print('Received decrypted message:', message)

    response = b'SECRET RESPONSE'

    try:
        size = str(len(response))
        size = '0' * (4 - len(size)) + size
        size = bytes(size, 'utf-8')
        prev_socket.sendall(size)
        # time.sleep(0.1)
        prev_socket.sendall(response)
    except err:
        print(err)

    # prev_socket.sendall(response)
    print(f'Sent unencrypted response to exit node at {prev_address[0]}')

    server_socket.close()
    prev_socket.close()


def parse_args():
    # Parse the command line
    parser = argparse.ArgumentParser()

    # Add optional arguments
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

import argparse
import sys
import zmq
import time
from messages import HealthMessage, OrderMessage, Veggies, Bottles, Cans, Milk, Drinks
import serialize as sz


def driver(args):
    # create context
    try:
        context = zmq.Context()
    except zmq.ZMQError as err:
        print("ZeroMQ Error: {}".format(err))
        return
    except:
        print("Some exception occurred getting context {}".format(sys.exc_info()[0]))
        return

    # create sockets
    try:
        health_socket = context.socket(zmq.REQ)
        order_socket = context.socket(zmq.REQ)
    except zmq.ZMQError as err:
        print("ZeroMQ Error obtaining context: {}".format(err))
        return
    except:
        print("Some exception occurred getting REQ socket {}".format(sys.exc_info()[0]))
        return

    # connect sockets to servers
    try:
        health_string = "tcp://" + args.health_addr + ":" + str(args.hport)
        order_string = "tcp://" + args.order_addr + ":" + str(args.oport)
        health_socket.connect(health_string)
        order_socket.connect(order_string)

    except zmq.ZMQError as err:
        print("ZeroMQ Error connecting REQ socket: {}".format(err))
        health_socket.close()
        order_socket.close()
        return
    except:
        print("Some exception occurred connecting REQ socket {}".format(sys.exc_info()[0]))
        health_socket.close()
        order_socket.close()
        return

    health_latencies = []
    order_latencies = []

    for i in range(args.iters):
        print(f'\n------Iteration {i + 1}------')
        # create and send health message
        msg = HealthMessage()
        print("Created request:\n")
        print(msg)
        print()

        start_time = time.time()
        health_socket.send_serialized(msg, sz.serialize_to_frames)
        health_message = sz.deserialize_response(health_socket.recv())
        end_time = time.time()

        health_latencies.append(round((end_time - start_time) * 1000, 3))

        print("Received response:\n")
        print(health_message)
        print()

        # create and send order message
        msg = OrderMessage()
        print("Created request:\n")
        print(msg)
        print()
        start_time = time.time()
        order_socket.send_serialized(msg, sz.serialize_to_frames)
        order_message = sz.deserialize_response(order_socket.recv())
        end_time = time.time()
        print("Received response:\n")
        print(order_message)
        print()

        order_latencies.append(round((end_time - start_time) * 1000, 3))

        time.sleep(0.1)

    print(f'Health latencies: {health_latencies}')
    print(f'Order latencies: {order_latencies}')

##################################
# Command line parsing
##################################
def parseCmdLineArgs():
    # parse the command line
    parser = argparse.ArgumentParser()

    # add optional arguments
    parser.add_argument("-a1", "--health_addr", default="127.0.0.1",
                        help="IP Address to connect to (default: localhost i.e., 127.0.0.1)")
    parser.add_argument("-a2", "--order_addr", default="127.0.0.1",
                        help="IP Address to connect to (default: localhost i.e., 127.0.0.1)")
    parser.add_argument("-i", "--iters", type=int, default=100, help="Number of iterations (default: 100")
    parser.add_argument("-p1", "--hport", type=int, default=5577,
                        help="Health port that server is listening on (default: 5556)")
    parser.add_argument("-p2", "--oport", type=int, default=5578,
                        help="Order port that server is listening on (default: 5557)")
    args = parser.parse_args()

    return args


# ------------------------------------------
# main function
def main():
    """ Main program """

    print("Demo program for TCP Client with ZeroMQ")

    # first parse the command line args
    parsed_args = parseCmdLineArgs()

    # start the driver code
    driver(parsed_args)


# ----------------------------------------------
if __name__ == '__main__':
    # here we just print the version numbers
    print("Current libzmq version is %s" % zmq.zmq_version())
    print("Current pyzmq version is %s" % zmq.pyzmq_version())

    main()

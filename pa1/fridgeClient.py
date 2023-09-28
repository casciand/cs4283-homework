import argparse
import sys
import zmq
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
        health_string = "tcp://" + args.addr + ":" + str(args.hport)
        order_string = "tcp://" + args.addr + ":" + str(args.oport)
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

    # create and send health message
    msg = HealthMessage()
    print("created message {}".format(msg))
    health_socket.send_serialized(msg, sz.serialize_to_frames)
    health_message = sz.deserialize_response(health_socket.recv())
    print("received message {}".format(health_message))

    # create and send bad health message
    bad_msg = b'bad message'
    print("created message {}".format(bad_msg))
    health_socket.send(bad_msg)
    bad_msg_resp = sz.deserialize_response(health_socket.recv())
    print("received message {}".format(bad_msg_resp))

    # create and send order message
    msg = CreateOrder()
    print("created message {}".format(msg))
    order_socket.send_serialized(msg, sz.serialize_to_frames)
    order_message = sz.deserialize_response(order_socket.recv())
    print("received message {}".format(order_message))

    # since we are a client, we actively send something to the server
    # for i in range(args.iters):
    #     try:
    #         health_socket.send(b"HelloWorld")
    #         order_socket.send(b"HelloWorld")
    #     except zmq.ZMQError as err:
    #         print("ZeroMQ Error sending: {}".format(err))
    #         health_socket.close()
    #         order_socket.close()
    #         return
    #     except:
    #         print("Some exception occurred receiving/sending {}".format(sys.exc_info()[0]))
    #         health_socket.close()
    #         order_socket.close()
    #         return
    #
    #     try:
    #         # receive a reply
    #         health_message = health_socket.recv()
    #         order_message = order_socket.recv()
    #         print("Received replies in iteration {} is {} and {}".format(i, health_message, order_message))
    #     except zmq.ZMQError as err:
    #         print("ZeroMQ Error receiving: {}".format(err))
    #         health_socket.close()
    #         order_socket.close()
    #         return
    #     except:
    #         print("Some exception occurred receiving/sending {}".format(sys.exc_info()[0]))
    #         health_socket.close()
    #         order_socket.close()
    #         return

def CreateOrder():
    veggies = Veggies(0.2, 0.4)
    cans = Cans(1)
    bottles = Bottles(0)
    drinks = Drinks(cans, bottles)
    contents = OrderMessage.OrderContents(veggies, drinks, [], [], [])
    return OrderMessage(contents)

##################################
# Command line parsing
##################################
def parseCmdLineArgs():
    # parse the command line
    parser = argparse.ArgumentParser()

    # add optional arguments
    parser.add_argument("-a", "--addr", default="127.0.0.1",
                        help="IP Address to connect to (default: localhost i.e., 127.0.0.1)")
    parser.add_argument("-i", "--iters", type=int, default=10, help="Number of iterations (default: 10")
    parser.add_argument("-p1", "--hport", type=int, default=5556,
                        help="Health port that server is listening on (default: 5556)")
    parser.add_argument("-p2", "--oport", type=int, default=5557,
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

import argparse
# import flatbuffers
import sys
import zmq

def driver(args):
    # builder = flatbuffers.Builder(1024)

    # create context
    try:
        context = zmq.Context()
    except zmq.ZMQError as err:
        print("ZeroMQ Error: {}".format(err))
        return
    except:
        print("Some exception occurred getting context {}".format(sys.exc_info()[0]))
        return

    # create socket
    try:
        health_socket = context.socket(zmq.REQ)
        order_socket = context.socket(zmq.REQ)
    except zmq.ZMQError as err:
        print("ZeroMQ Error obtaining context: {}".format(err))
        return
    except:
        print("Some exception occurred getting REQ socket {}".format(sys.exc_info()[0]))
        return

    # TODO - connect socket to multiple servers
    # connect socket to servers
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

    # since we are a client, we actively send something to the server
    for i in range(args.iters):
        try:
            health_socket.send(b"HelloWorld")
            order_socket.send(b"HelloWorld")
        except zmq.ZMQError as err:
            print("ZeroMQ Error sending: {}".format(err))
            health_socket.close()
            order_socket.close()
            return
        except:
            print("Some exception occurred receiving/sending {}".format(sys.exc_info()[0]))
            health_socket.close()
            order_socket.close()
            return

        try:
            # receive a reply
            health_message = health_socket.recv()
            order_message = order_socket.recv()
            print("Received replies in iteration {} is {} and {}".format(i, health_message, order_message))
        except zmq.ZMQError as err:
            print("ZeroMQ Error receiving: {}".format(err))
            health_socket.close()
            order_socket.close()
            return
        except:
            print("Some exception occurred receiving/sending {}".format(sys.exc_info()[0]))
            health_socket.close()
            order_socket.close()
            return


##################################
# Command line parsing
##################################
def parseCmdLineArgs():
    # parse the command line
    parser = argparse.ArgumentParser()

    # add optional arguments
    parser.add_argument("-a", "--addr", default="127.0.0.1", help="IP Address to connect to (default: localhost i.e., 127.0.0.1)")
    parser.add_argument("-i", "--iters", type=int, default=10, help="Number of iterations (default: 10")
    parser.add_argument("-p1", "--hport", type=int, default=5556, help="Health port that server is listening on (default: 5556)")
    parser.add_argument("-p2", "--oport", type=int, default=5557, help="Order port that server is listening on (default: 5557)")
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

import argparse
import sys
import time
import zmq


def driver(args):
    try:
        context = zmq.Context()  # returns a singleton object
    except zmq.ZMQError as err:
        print("ZeroMQ Error obtaining context: {}".format(err))
        return
    except:
        print("Some exception occurred getting context {}".format(sys.exc_info()[0]))
        return

    try:
        socket = context.socket(zmq.REP)
    except zmq.ZMQError as err:
        print("ZeroMQ Error obtaining REP socket: {}".format(err))
        return
    except:
        print("Some exception occurred getting REP socket {}".format(sys.exc_info()[0]))
        return

    try:
        bind_string = "tcp://" + args.intf + ":" + str(args.port)
        socket.bind(bind_string)
    except zmq.ZMQError as err:
        print("ZeroMQ Error binding REP socket: {}".format(err))
        socket.close()
        return
    except:
        print("Some exception occurred binding REP socket {}".format(sys.exc_info()[0]))
        socket.close()
        return

    # since we are a server, we service incoming clients forever
    print("Server now waiting to receive something")
    while True:
        try:
            #  Wait for next request from client
            message = socket.recv()
            print("Received request: %s" % message)
        except zmq.ZMQError as err:
            print("ZeroMQ Error receiving: {}".format(err))
            socket.close()
            return
        except:
            print("Some exception occurred receiving/sending {}".format(sys.exc_info()[0]))
            socket.close()
            return

        #  Do some 'work'. In this case we just sleep.
        time.sleep(1)

        try:
            #  Send reply back to client
            print("Send dummy reply")
            socket.send(b"ACK")
        except zmq.ZMQError as err:
            print("ZeroMQ Error sending: {}".format(err))
            socket.close()
            return
        except:
            print("Some exception occurred receiving/sending {}".format(sys.exc_info()[0]))
            socket.close()
            return


##################################
# Command line parsing
##################################
def parseCmdLineArgs():
    # parse the command line
    parser = argparse.ArgumentParser()

    # add optional arguments
    parser.add_argument("-i", "--intf", default="*", help="Interface to bind to (default: *)")
    parser.add_argument("-p", "--port", type=int, default=5556, help="Port to bind to (default: 5556)")
    args = parser.parse_args()

    return args


# ------------------------------------------
# main function
def main():
    """ Main program """

    print("Demo program for TCP Server with ZeroMQ")

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
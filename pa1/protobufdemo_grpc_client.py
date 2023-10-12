#  Author: Aniruddha Gokhale
#  Created: Fall 2023
#
#  Purpose: demonstrate serialization of a user-defined data structure using
#  Protocol Buffers combined with gRPC. Note that here we
#  are more interested in how a serialized packet gets sent over the network
#  and retrieved. To that end, we really don't care even if the client and
#  server were both on the same machine or remote to each other.

# This one implements the client functionality
#

# Note that this code mimics what we did with FlatBufs+ZeroMQ but this time
# we mix Protocol Buffers and gRPC

# The different packages we need in this Python driver code
import os
import sys
import time  # needed for timing measurements and sleep

import random  # random number generator
import argparse  # argument parser

import logging

import grpc  # for gRPC

# import generated packages
import schema_pb2 as spb
import schema_pb2_grpc as spb_grpc


##################################
#        Driver program
##################################

def create_order():
    order = spb.Order()
    order.type = 'ORDER'

    order.contents.veggies.tomato = 2.2
    order.contents.veggies.cucumber = 1.8
    order.contents.drinks.cans.coke = 2
    order.contents.drinks.bottles.sprite = 1

    milk = order.contents.milk.add()
    milk.type = order.contents.Milk.WHOLE
    milk.quantity = 3.89
    milk = order.contents.milk.add()
    milk.type = order.contents.Milk.SKIM
    milk.quantity = 2.3

    bread = order.contents.bread.add()
    bread.type = order.contents.Bread.WHEAT
    bread.quantity = 3.89

    meat = order.contents.meat.add()
    meat.type = order.contents.Meat.CHICKEN
    meat.quantity = 3.89
    return order

def driver(name, iters, vec_len, health_port, order_port):
    print(
        "Driver program: Name = {}, Num Iters = {}, Vector len = {}, Health port = {}, Order port = {}".format(name, iters, vec_len, health_port, order_port))

    # first obtain a peer and initialize it
    print("Driver program: create handle to the client and then run the code")
    try:

        # Use the insecure channel to establish connection with server
        print("Instantiate insecure channel")
        health_channel = grpc.insecure_channel("localhost:" + str(health_port))
        order_channel = grpc.insecure_channel("localhost:" + str(order_port))
        print("Obtain a proxy object to the server")
        health_stub = spb_grpc.HealthServiceStub(health_channel)
        order_stub = spb_grpc.OrderServiceStub(order_channel)

        # now send the serialized custom message for the number of desired iterations
        print("Allocate the Request object that we will then populate in every iteration")
        health_mes = spb.HealthMessage(
            dispenser=spb.DispenserStatus.OPTIMAL,
            icemaker=2,
            lightbulb=spb.Status.GOOD,
            fridge_temp=45,
            freezer_temp=10,
            sensor_status=spb.Status.GOOD
        )

        order_mes = create_order()

        print("Peer client sending the serialized health message")
        start_time = time.time()
        resp = health_stub.method(health_mes)
        end_time = time.time()
        print("sending/receiving took {} secs".format(end_time - start_time))
        print("response: {}".format(resp))

        time.sleep(0.050)

        print("Peer client sending the serialized order message")
        start_time = time.time()
        resp = order_stub.method(order_mes)
        end_time = time.time()
        print("sending/receiving took {} secs".format(end_time - start_time))
        print("response: {}".format(resp))

        time.sleep(0.050)

        # print("Peer client sending the serialized bad message")
        # start_time = time.time()
        # resp = order_stub.method("hello")
        # end_time = time.time()
        # print("sending/receiving took {} secs".format(end_time - start_time))
        # print("response: {}".format(resp))


        # req = spb.Request()
        #
        # for i in range(iters):
        #     # for every iteration, let us fill up our custom message with some info
        #     req.seq_no = i  # this will be our sequence number
        #     req.ts = time.time()  # current time
        #     req.name = name  # assigned name
        #     req.data[:] = [random.randint(1, 1000) for j in range(vec_len)]
        #     print("-----Iteration: {} contents of message before sending\n{} ----------".format(i, req))
        #
        #     # now let the client send the message to its server part
        #     print("Peer client sending the serialized message")
        #     start_time = time.time()
        #     resp = stub.method(req)
        #     end_time = time.time()
        #     print("sending/receiving took {} secs".format(end_time - start_time))
        #
        #     # sleep a while before we send the next serialization so it is not
        #     # extremely fast
        #     time.sleep(0.050)  # 50 msec

    except:
        print("Some exception occurred {}".format(sys.exc_info()[0]))
        return


##################################
# Command line parsing
##################################
def parseCmdLineArgs():
    # parse the command line
    parser = argparse.ArgumentParser()

    # add optional arguments
    parser.add_argument("-i", "--iters", type=int, default=10, help="Number of iterations to run (default: 10)")
    parser.add_argument("-l", "--veclen", type=int, default=20,
                        help="Length of the vector field (default: 20; contents are irrelevant)")
    parser.add_argument("-n", "--name", default="ProtoBuf gRPC Demo", help="Name to include in each message")
    parser.add_argument("-hp", "--health_port", type=int, default=5577,
                        help="Port where the health server part of the peer listens and client side connects to (default: 5577)")
    parser.add_argument("-op", "--order_port", type=int, default=5578,
                        help="Port where the health server part of the peer listens and client side connects to (default: 5577)")

    # parse the args
    args = parser.parse_args()

    return args


# ------------------------------------------
# main function
def main():
    """ Main program """

    print("Demo program for Protocol Buffers with gRPC serialization/deserialization")

    # first parse the command line args
    parsed_args = parseCmdLineArgs()

    # start the driver code
    driver(parsed_args.name, parsed_args.iters, parsed_args.veclen, parsed_args.health_port, parsed_args.order_port)


# ----------------------------------------------
if __name__ == '__main__':
    main()
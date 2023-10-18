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
    order.contents.veggies.carrot = 9.8
    order.contents.veggies.broccoli = 3.8
    order.contents.veggies.asparagus = 1.4
    order.contents.drinks.cans.coke = 2
    order.contents.drinks.cans.beer = 3
    order.contents.drinks.cans.fanta = 4
    order.contents.drinks.bottles.sprite = 1
    order.contents.drinks.bottles.gingerale = 2
    order.contents.drinks.bottles.wine = 3

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

def driver(name, iters, vec_len, health_port, order_port, hip, oip):
    print(
        "Driver program: Name = {}, Num Iters = {}, Vector len = {}, Health port = {}, Order port = {}".format(name, iters, vec_len, health_port, order_port))

    # first obtain a peer and initialize it
    print("Driver program: create handle to the client and then run the code")
    try:

        # Use the insecure channel to establish connection with server
        hpath = "{}:{}".format(hip, str(health_port))
        opath = "{}:{}".format(oip, str(order_port))
        print("Instantiate insecure channel to {} and {}".format(hpath, opath))
        health_channel = grpc.insecure_channel(hpath)
        order_channel = grpc.insecure_channel(opath)
        print("Obtain a proxy object to the server")
        health_stub = spb_grpc.HealthServiceStub(health_channel)
        order_stub = spb_grpc.OrderServiceStub(order_channel)

        for i in range(iters):
            print(f'\n------Iteration {i + 1}------')
            # now send the serialized custom message for the number of desired iterations
            health = spb.Health()
            health.type = 'HEALTH'
            health.contents.dispenser = health.contents.DispenserStatus.OPTIMAL
            health.contents.icemaker = 2
            health.contents.lightbulb = spb.Status.GOOD
            health.contents.fridge_temp = 45
            health.contents.freezer_temp = 10
            health.contents.sensor_status = spb.Status.GOOD
            health.contents.motor_status = health.contents.MotorStatus.RUNNING

            print("Created request:\n")
            print(health)
            print()

            order_mes = create_order()

            # print("Peer client sending the serialized health message")
            start_time = time.time()
            resp = health_stub.method(health)
            end_time = time.time()
            print("sending/receiving took {} secs".format(end_time - start_time))
            # print("response: {}".format(resp))

            print("Received response:\n")
            print(resp)
            print()

            time.sleep(1)

            print("Created request:\n")
            print(order_mes)
            print()

            # print("Peer client sending the serialized order message")
            start_time = time.time()
            resp = order_stub.method(order_mes)
            end_time = time.time()
            print("sending/receiving took {} secs".format(end_time - start_time))
            # print("response: {}".format(resp))

            print("Received response:\n")
            print(resp)

            time.sleep(5)
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
    parser.add_argument("-i", "--iters", type=int, default=100, help="Number of iterations to run (default: 100)")
    parser.add_argument("-l", "--veclen", type=int, default=20,
                        help="Length of the vector field (default: 20; contents are irrelevant)")
    parser.add_argument("-n", "--name", default="ProtoBuf gRPC Demo", help="Name to include in each message")
    parser.add_argument("-hp", "--health_port", type=int, default=5577,
                        help="Port where the health server part of the peer listens and client side connects to (default: 5577)")
    parser.add_argument("-op", "--order_port", type=int, default=5578,
                        help="Port where the health server part of the peer listens and client side connects to (default: 5577)")
    parser.add_argument("-hip", "--health_ip", type=str, default="localhost",
                        help="ip address of health server container")
    parser.add_argument("-oip", "--order_ip", type=str, default="localhost",
                        help="ip address of order server container")
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
    driver(parsed_args.name, parsed_args.iters, parsed_args.veclen, parsed_args.health_port, parsed_args.order_port, parsed_args.health_ip, parsed_args.order_ip)


# ----------------------------------------------
if __name__ == '__main__':
    main()

import argparse
import grpc
from messages import OrderMessage
import order_service_pb2_grpc
import health_service_pb2
import health_service_pb2_grpc

def driver(args):
    health_channel = grpc.insecure_channel(f'{args.addr}:{args.hport}')
    order_channel = grpc.insecure_channel(f'{args.addr}:{args.oport}')
    
    health_stub = health_service_pb2_grpc.HealthServiceStub(health_channel)
    order_stub = order_service_pb2_grpc.OrderServiceStub(order_channel)

    # Health check
    try:
        health_response = health_stub.CheckHealth(health_service_pb2.HealthRequest())
        print("Received health response:", health_response.message)
    except grpc.RpcError as rpc_err:
        print(f"RPC failed with code {rpc_err.code()} and details: {rpc_err.details()}")

    # Send order
    order_request = OrderMessage()
    try:
        order_response = order_stub.PlaceOrder(order_request)
        print("Received order response:", order_response.message)
    except grpc.RpcError as rpc_err:
        print(f"RPC failed with code {rpc_err.code()} and details: {rpc_err.details()}")


def parseCmdLineArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--addr", default="127.0.0.1", help="IP Address to connect to (default: localhost i.e., 127.0.0.1)")
    parser.add_argument("-i", "--iters", type=int, default=10, help="Number of iterations (default: 10")
    parser.add_argument("-p1", "--hport", type=int, default=5556, help="Health port that server is listening on (default: 5556)")
    parser.add_argument("-p2", "--oport", type=int, default=5557, help="Order port that server is listening on (default: 5557)")
    args = parser.parse_args()
    return args

def main():
    print("Demo program for gRPC Client")

    parsed_args = parseCmdLineArgs()
    driver(parsed_args)

if __name__ == '__main__':
    main()

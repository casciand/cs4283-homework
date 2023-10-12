import argparse
import grpc
import time
import order_service_pb2
import order_service_pb2_grpc
import messages
import serialize as sz
from concurrent import futures


class OrderServiceServicer(order_service_pb2_grpc.OrderServiceServicer):
    def PlaceOrder(self, request, context):
        try:
            # Process the request (deserialize, handle, etc.)
            print("Received request:", request.contents)
            
            # Simulate some processing time
            time.sleep(1)
            
            # Send a response
            response_message = "Order Received!"
            return order_service_pb2.OrderResponse(message=response_message)
        except Exception as e:
            print("Exception handling order:", e)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('Server error in processing order')
            return order_service_pb2.OrderResponse(message="Error processing order")

def serve(args):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_service_pb2_grpc.add_OrderServiceServicer_to_server(OrderServiceServicer(), server)
    server.add_insecure_port('[::]:{}'.format(args.port))
    server.start()
    print("Order gRPC server started on port:", args.port)
    server.wait_for_termination()

def parseCmdLineArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--intf", default="0.0.0.0", help="Interface to bind to (default: [::])")
    parser.add_argument("-p", "--port", type=int, default=5557, help="Port to bind to (default: 5557)")
    args = parser.parse_args()
    return args

def main():
    print("Starting the Order gRPC Server")
    parsed_args = parseCmdLineArgs()
    try:
        serve(parsed_args)
    except Exception as e:
        print(f"Error starting the server: {e}")

if __name__ == '__main__':
    main()

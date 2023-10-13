import grpc
from concurrent import futures
import argparse
import time
import health_service_pb2
import health_service_pb2_grpc

class HealthServicer(health_service_pb2_grpc.HealthServiceServicer):

    def CheckHealth(self, request, context):
        print("Received request:", request.request_content)
        ack_message = "You are Healthy"
        return health_service_pb2.HealthResponse(code=messages.ResponseCode.OK, message=ack_message)


def serve(args):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    health_service_pb2_grpc.add_HealthServiceServicer_to_server(HealthServicer(), server)
    bind_string = args.intf + ':' + str(args.port)
    server.add_insecure_port(bind_string)
    server.start()
    print("Server started at", bind_string)
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


def parseCmdLineArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--intf", default="[::]", help="Interface to bind to (default: [::])")
    parser.add_argument("-p", "--port", type=int, default=5556, help="Port to bind to (default: 5556)")
    args = parser.parse_args()
    return args


def main():
    print("Demo program for TCP Server with gRPC")
    parsed_args = parseCmdLineArgs()
    serve(parsed_args)


if __name__ == '__main__':
    main()

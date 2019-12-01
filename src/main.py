import logging

from .grpc.server import GRPCServer
from .proto import helloworld_pb2_grpc
from .services.greeter import Greeter


def add_services(server):
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)


if __name__ == '__main__':
    logging.basicConfig()

    server = GRPCServer()
    add_services(server.server)
    server.serve()

import logging
import signal
import sys

from .grpc.server import GRPCServer
from .proto import helloworld_pb2_grpc
from .services.greeter import Greeter


def add_services(server):
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)


def signalHandler(signal, frame):
    print('Process Interrupted!\n\a')
    server.stop()
    sys.exit(0)


if __name__ == '__main__':
    logging.basicConfig()

    server = GRPCServer(address='0.0.0.0', port=4242)
    signal.signal(signal.SIGINT, signalHandler)

    addServices(server.instance)
    server.serve()

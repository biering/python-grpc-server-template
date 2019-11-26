import logging

import grpc

from proto import helloworld_pb2_grpc
from proto import helloworld_pb2


class GreeterClient(object):
    """
    Client for accessing the gRPC functionality
    """

    def __init__(self):
        # configure the host and the
        # the port to which the client should connect
        # to.
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a communication channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client to the server channel
        self.stub = helloworld_pb2_grpc.GreeterStub(self.channel)

    def get_say_hello(self, name):
        response = self.stub.SayHello(helloworld_pb2.HelloRequest(name=name))
        print("Greeter client received: " + response.message)

    def get_say_hello_often(self, name):
        message = helloworld_pb2.HelloRequest(name=name)
        response = self.stub.SayHelloOften(message)
        for r in response:
            print(r)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))

    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()

    client = GreeterClient()
    # client.get_say_hello_often('lala')
    client.get_say_hello('test')

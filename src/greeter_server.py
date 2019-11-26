from concurrent import futures
import logging

import grpc

from proto import helloworld_pb2_grpc
from proto import helloworld_pb2


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)

    def SayHelloAgain(self, request, context):
        return helloworld_pb2.HelloReply(
            message='Hello again, %s!' % request.name)

    def SayHelloOften(self, request, context):
        messages = ['a', 'b', 'c', 'd', 'e']

        for message in messages:
            yield helloworld_pb2.HelloReply(message=message)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    print('Serving...')
    serve()

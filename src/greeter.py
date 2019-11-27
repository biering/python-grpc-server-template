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

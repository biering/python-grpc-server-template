from concurrent import futures

import grpc


class GRPCServer(object):

    @property
    def instance(self):
        return self.__server

    def __init__(self, address='[::]', port=50051):
        self.__address = address
        self.__port = port
        self.__server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    def serve(self):
        endpoint = f'{self.__address}:{str(self.__port)}'

        print(f'Started GRPC Server at {endpoint}')
        print('Serving...')

        self.__server.add_insecure_port(endpoint)
        self.__server.start()
        self.__server.wait_for_termination()

    def stop(self):
        print("Stopping GRPC Server gracefully")
        self.__server.stop(3)


if __name__ == '__main__':
    server = GRPCServer()
    server.serve()

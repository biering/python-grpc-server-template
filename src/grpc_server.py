from concurrent import futures

import grpc


class GRPCServer(object):
    def __init__(self, address='[::]', port=50051):
        self.address = address
        self.port = port
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    def serve(self):
        endpoint = f'{self.address}:{str(self.port)}'

        print(f'Started GRPC Server at {endpoint}')
        print('Serving...')

        self.server.add_insecure_port(endpoint)
        self.server.start()
        self.server.wait_for_termination()


if __name__ == '__main__':
    server = GRPCServer()
    server.serve()

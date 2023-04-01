from concurrent import futures
import grpc
import calculator_pb2
import calculator_pb2_grpc
import registry_pb2_grpc, registry_pb2


class Calculator(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.first_number + request.second_number
        response = calculator_pb2.Response(result=result)
        return response

    def Multiply(self, request, context):
        result = request.first_number * request.second_number
        response = calculator_pb2.Response(result=result)
        return response

    def Subtract(self, request, context):
        result = request.first_number - request.second_number
        response = calculator_pb2.Response(result=result)
        return response

    def Divide(self, request, context):
        result = request.first_number / request.second_number
        response = calculator_pb2.Response(result=result)
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    register_microservice() # TODO get response and error handle.
    # if error:
    #    print(error)
    #    exit(0)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


def register_microservice():
    with grpc.insecure_channel('localhost:50123') as channel:
        stub = registry_pb2_grpc.RegistryServiceStub(channel)
        register_request = registry_pb2.RegistryRequest(serviceName="calculator", serviceAddress="127.0.0.1", servicePort=50051)
        response = stub.RegisterService(register_request)
        print("registered microservice", response)


if __name__ == '__main__':
    serve()

from concurrent import futures
import grpc
import calculator_pb2
import calculator_pb2_grpc
import registry_pb2_grpc
import registry_pb2


class Calculator(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.first_number + request.second_number
        response = calculator_pb2.Response(
            result=result, status=calculator_pb2.Status(code=0, message="Success"))
        return response

    def Multiply(self, request, context):
        result = request.first_number * request.second_number
        response = calculator_pb2.Response(
            result=result, status=calculator_pb2.Status(code=0, message="Success"))
        return response

    def Subtract(self, request, context):
        result = request.first_number - request.second_number
        response = calculator_pb2.Response(
            result=result, status=calculator_pb2.Status(code=0, message="Success"))
        return response

    def Divide(self, request, context):
        if request.second_number == 0:
            return calculator_pb2.Response(status=calculator_pb2.Status(code=1, message="Division by zero error"))
        result = request.first_number / request.second_number
        response = calculator_pb2.Response(
            result=result, status=calculator_pb2.Status(code=0, message="Success"))
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    register_microservice()
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


def register_microservice():
    with grpc.insecure_channel('localhost:50123') as channel:
        stub = registry_pb2_grpc.RegistryServiceStub(channel)
        register_request = registry_pb2.RegistryRequest(
            serviceName="calculator", serviceAddress="127.0.0.1", servicePort=50051)
        response = stub.RegisterService(register_request)

        if response.status.code == 0:
            print(
                f"Registered microservice {response.serviceName} successfully")
        else:
            print(
                f"Failed to register microservice {response.serviceName}: {response.status.message}")


if __name__ == '__main__':
    serve()

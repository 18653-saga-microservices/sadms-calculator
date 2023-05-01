from concurrent import futures
import grpc
from protos.gen_py import calculator_pb2_grpc
from protos.gen_py import calculator_pb2
from protos.gen_py import registry_pb2_grpc
from protos.gen_py import registry_pb2


class Calculator(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.first_number + request.second_number
        response = calculator_pb2.Response(
            result=result, status=0, message="Success")
        return response

    def Multiply(self, request, context):
        result = request.first_number * request.second_number
        response = calculator_pb2.Response(
            result=result, status=0, message="Success")
        return response

    def Subtract(self, request, context):
        result = request.first_number - request.second_number
        response = calculator_pb2.Response(
            result=result, status=0, message="Success")
        return response

    def Divide(self, request, context):
        if request.second_number == 0:
            return calculator_pb2.Response(status=1, message="Divide by zero Warning")
        result = request.first_number / request.second_number
        response = calculator_pb2.Response(
            result=result, status=0, message="Success")
        return response

# register the calculator service to the orchestrator
# return True if registration success
# False otherwise


def register_microservice(serviceName, serviceIP, servicePort):
    with grpc.insecure_channel('localhost:50123') as channel:
        stub = registry_pb2_grpc.RegistryServiceStub(channel)

        register_request = registry_pb2.RegistryRequest(
            serviceName=serviceName, serviceAddress=serviceIP, servicePort=servicePort)

        # try to register the service to the orchestrator
        try:
            response = stub.RegisterService(register_request)
        except grpc.RpcError as e:
            print(
                f"The SAGAFramework orchestrator is not running; GRPC error status = {e.code()}")
            return False

        if response.status.code == 0:  # if registration success
            print(
                f"Registered microservice {response.serviceName} successfully")
            return True
        else:  # if registration failed, print error message
            print(
                f"Failed to register microservice {response.serviceName} \
                 service id: {response.serviceId}\
                 status code: {response.status}\
                 error message:{response.message}")
            return False


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(
        Calculator(), server)

    # create service name, ip, and address
    serviceName = "calculator"
    serviceIP = "127.0.0.1"
    servicePort = 50051

    # register the calculator service to the orchestrator
    register_result = register_microservice(
        serviceName, serviceIP, servicePort)

    # if registration failed, stop the server
    if register_result is False:
        print("Failed to register microservice; exiting...")
        exit(1)

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

import grpc
import calculator_pb2
import calculator_pb2_grpc
from flask import Flask, request

app = Flask(__name__)


@app.route('/add')
def add():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        operand1 = int(request.args.get('a'))
        operand2 = int(request.args.get('b'))
        print(operand1, operand2)
        add_request = calculator_pb2.AddRequest(
            operand1=operand1, operand2=operand2)
        response = stub.Add(add_request)
        print(response.result)
        return str(response.result)


@app.route('/multiply')
def multiply():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        operand1 = int(request.args.get('a'))
        operand2 = int(request.args.get('b'))
        print(operand1, operand2)
        multiply_request = calculator_pb2.MultiplyRequest(
            operand1=operand1, operand2=operand2)
        response = stub.Multiply(multiply_request)
        print(response.result)
        return str(response.result)


if __name__ == '__main__':
    app.run()

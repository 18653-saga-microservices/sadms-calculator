import grpc
import calculator_pb2
import calculator_pb2_grpc
from flask import Flask, request

app = Flask(__name__)


@app.route('/calculate')
def add():
    first_number = int(request.args.get('first_number'))
    second_number = int(request.args.get('second_number'))
    operation = request.args.get('operation')
    print(first_number, second_number, operation)
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        add_request = calculator_pb2.Request(
            first_number=first_number, second_number=second_number)
        if operation == 'add':
            response = stub.Add(add_request)
        elif operation == 'multiply':
            response = stub.Multiply(add_request)
        elif operation == 'subtract':
            response = stub.Subtract(add_request)
        elif operation == 'divide':
            response = stub.Divide(add_request)
        else:
            return ("illegal operation")
        print(response.result)
        return str(response.result)


if __name__ == '__main__':
    app.run()

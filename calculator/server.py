import grpc
from concurrent import futures
import time

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# import the original calculator.py
import calculator

class AdditionServicer(calculator_pb2_grpc.AdditionServicer):

    def Addition(self, request, context):
        response = calculator_pb2.AdditionResponse()
        response.c = calculator.Addition(request.a, request.b)
        return response

class SubstractionServicer(calculator_pb2_grpc.SubstractionServicer):

    def Substraction(self, request, context):
        response = calculator_pb2.SubstractionResponse()
        response.c = calculator.Substraction(request.a, request.b)
        return response
#
class MultiplicationServicer(calculator_pb2_grpc.MultiplicationServicer):

    def Multiplication(self, request, context):
        response = calculator_pb2.MultiplicationResponse()
        response.c = calculator.Multiplication(request.a, request.b)
        return response
#
class DivisionServicer(calculator_pb2_grpc.DivisionServicer):

    def Division(self, request, context):
        response = calculator_pb2.DivisionResponse()
        response.c = calculator.Division(request.a, request.b)
        return response



server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

calculator_pb2_grpc.add_AdditionServicer_to_server(AdditionServicer(), server)

calculator_pb2_grpc.add_SubstractionServicer_to_server(SubstractionServicer(), server)

calculator_pb2_grpc.add_MultiplicationServicer_to_server(MultiplicationServicer(), server)

calculator_pb2_grpc.add_DivisionServicer_to_server(DivisionServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
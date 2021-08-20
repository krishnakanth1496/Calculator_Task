# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import calculator_pb2 as calculator__pb2


class AdditionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Addition = channel.unary_unary(
                '/Addition/Addition',
                request_serializer=calculator__pb2.AdditionRequest.SerializeToString,
                response_deserializer=calculator__pb2.AdditionResponse.FromString,
                )


class AdditionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Addition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AdditionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Addition': grpc.unary_unary_rpc_method_handler(
                    servicer.Addition,
                    request_deserializer=calculator__pb2.AdditionRequest.FromString,
                    response_serializer=calculator__pb2.AdditionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Addition', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Addition(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Addition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Addition/Addition',
            calculator__pb2.AdditionRequest.SerializeToString,
            calculator__pb2.AdditionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class SubstractionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Substraction = channel.unary_unary(
                '/Substraction/Substraction',
                request_serializer=calculator__pb2.SubstractionRequest.SerializeToString,
                response_deserializer=calculator__pb2.SubstractionResponse.FromString,
                )


class SubstractionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Substraction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SubstractionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Substraction': grpc.unary_unary_rpc_method_handler(
                    servicer.Substraction,
                    request_deserializer=calculator__pb2.SubstractionRequest.FromString,
                    response_serializer=calculator__pb2.SubstractionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Substraction', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Substraction(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Substraction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Substraction/Substraction',
            calculator__pb2.SubstractionRequest.SerializeToString,
            calculator__pb2.SubstractionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class MultiplicationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Multiplication = channel.unary_unary(
                '/Multiplication/Multiplication',
                request_serializer=calculator__pb2.MultiplicationRequest.SerializeToString,
                response_deserializer=calculator__pb2.MultiplicationResponse.FromString,
                )


class MultiplicationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Multiplication(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MultiplicationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Multiplication': grpc.unary_unary_rpc_method_handler(
                    servicer.Multiplication,
                    request_deserializer=calculator__pb2.MultiplicationRequest.FromString,
                    response_serializer=calculator__pb2.MultiplicationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Multiplication', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Multiplication(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Multiplication(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Multiplication/Multiplication',
            calculator__pb2.MultiplicationRequest.SerializeToString,
            calculator__pb2.MultiplicationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class DivisionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Division = channel.unary_unary(
                '/Division/Division',
                request_serializer=calculator__pb2.DivisionRequest.SerializeToString,
                response_deserializer=calculator__pb2.DivisionResponse.FromString,
                )


class DivisionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Division(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DivisionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Division': grpc.unary_unary_rpc_method_handler(
                    servicer.Division,
                    request_deserializer=calculator__pb2.DivisionRequest.FromString,
                    response_serializer=calculator__pb2.DivisionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Division', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Division(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Division(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Division/Division',
            calculator__pb2.DivisionRequest.SerializeToString,
            calculator__pb2.DivisionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

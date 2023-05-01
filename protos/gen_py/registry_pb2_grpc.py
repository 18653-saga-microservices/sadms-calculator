# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import registry_pb2 as registry__pb2


class RegistryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterService = channel.unary_unary(
            '/registry.RegistryService/RegisterService',
            request_serializer=registry__pb2.RegistryRequest.SerializeToString,
            response_deserializer=registry__pb2.RegistryResponse.FromString,
        )


class RegistryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterService(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RegistryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'RegisterService': grpc.unary_unary_rpc_method_handler(
            servicer.RegisterService,
            request_deserializer=registry__pb2.RegistryRequest.FromString,
            response_serializer=registry__pb2.RegistryResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'registry.RegistryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

 # This class is part of an EXPERIMENTAL API.


class RegistryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterService(request,
                        target,
                        options=(),
                        channel_credentials=None,
                        call_credentials=None,
                        insecure=False,
                        compression=None,
                        wait_for_ready=None,
                        timeout=None,
                        metadata=None):
        return grpc.experimental.unary_unary(request, target, '/registry.RegistryService/RegisterService',
                                             registry__pb2.RegistryRequest.SerializeToString,
                                             registry__pb2.RegistryResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import grpc_dialout_pb2 as grpc__dialout__pb2


class GRPCDialoutStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Dialout = channel.stream_unary(
                '/grpc_dialout.GRPCDialout/Dialout',
                request_serializer=grpc__dialout__pb2.DialoutMsg.SerializeToString,
                response_deserializer=grpc__dialout__pb2.DialoutResponse.FromString,
                )


class GRPCDialoutServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Dialout(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GRPCDialoutServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Dialout': grpc.stream_unary_rpc_method_handler(
                    servicer.Dialout,
                    request_deserializer=grpc__dialout__pb2.DialoutMsg.FromString,
                    response_serializer=grpc__dialout__pb2.DialoutResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc_dialout.GRPCDialout', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GRPCDialout(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Dialout(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/grpc_dialout.GRPCDialout/Dialout',
            grpc__dialout__pb2.DialoutMsg.SerializeToString,
            grpc__dialout__pb2.DialoutResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

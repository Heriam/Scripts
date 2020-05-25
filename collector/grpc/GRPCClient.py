import traceback
from concurrent import futures
import grpc
import grpc_dialout_pb2
import grpc_dialout_pb2_grpc as dialout
import time
import configparser
import logging
import json
import datetime
import socket


class UDPReceiver:
    UDP_IP = "192.168.254.2"
    UDP_PORT = 50066
    MSG_LEN = 1024

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
        self.sock.bind((self.UDP_IP, self.UDP_PORT))

    def __iter__(self):
        return self

    def __next__(self):
        try:
            data, addr = self.sock.recvfrom(self.MSG_LEN)
            msg = data.split(b'\x00')[0].decode("utf-8")
            deviceMsg = grpc_dialout_pb2.DeviceInfo(producerName='H3C', deviceName='67-215', deviceModel='H3C S6850-56HF')
            dialoutmsg = grpc_dialout_pb2.DialoutMsg(deviceMsg=deviceMsg, sensorPath='TelemetryFTrace/GenEvent', jsonData=msg)
            return dialoutmsg
        except Exception as e:
            print("Got exception trying to recv %s" % e)
            raise StopIteration


def sendmsg(grpcClient):
    recv = UDPReceiver()
    # while recv.__next__():
    #     print(recv.__next__())
    grpcClient.Dialout(recv)


def run():
    with grpc.insecure_channel('localhost:51235') as channel:
        grpcClient = dialout.GRPCDialoutStub(channel)
        sendmsg(grpcClient)


if __name__ == '__main__':
    logging.basicConfig()
    run()
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
import socket, threading

logging.basicConfig(
    level=logging.INFO,
    filemode="w",
    filename="log/grpc.log",
    format="[%(asctime)s][%(levelname)s]:%(message)s"
)

# Config Keys
KEY_GRPC = "grpc"
KEY_GRPC_OLD_SERVER = "grpcServerNew"
KEY_GRPC_NEW_SERVER = "grpcServerOld"
# Template Keys
KEY_SENSOR_PATHS = "sensor-paths"
KEY_SENSOR_GROUPS = "sensor-groups"
KEY_DST_GROUPS = "destination-groups"
KEY_SUBSCRIPTIONS = "subscriptions"
KEY_DEV_KPIS = "device-kpis"
KEY_INT_KPIS = "interface-kpis"
KEY_BUF_MON = "buffer-monitor"
KEY_RES_MON = "resource-monitor"
KEY_TRANSCEIVERS = "transceivers"
KEY_CHANGEANALYSIS = "change-analysis"
# Dev KPIs
DEV_BOARDS = "Device/Boards"
DEV_PHY = "Device/PhysicalEntities"
DEV_EXTPHY = "Device/ExtPhysicalEntities"
# IF KPIs
IF_STATIS = "Ifmgr/Statistics"
IF_INTFS = "Ifmgr/Interfaces"
IF_ETHSTATIS = "Ifmgr/EthPortStatistics"
# BUF KPIs
BUF_HDROOMUSE = "BufferMonitor/CommHeadroomUsages"
BUF_BUFUSE = "BufferMonitor/CommBufferUsages"
BUF_ECNWRED = "BufferMonitor/EcnAndWredStatistics"
BUF_EDROPS = "BufferMonitor/EgressDrops"
BUF_PFCSTATIS = "BufferMonitor/PFCStatistics"
BUF_PFCSPEEDS = "BufferMonitor/PFCSpeeds"
BUF_INDROPS = "BufferMonitor/IngressDrops"
# RES MON KPIs
RES_RESOURCES = "ResourceMonitor/Resources"
RES_MONITORS = "ResourceMonitor/Monitors"
# Transceivers
DEV_TRANSCEIVERS = "Device/Transceivers"
# Change Analysis
IPV6_ROUTES = "Route/Ipv6Routes"
IPV4_ROUTES = "Route/Ipv4Routes"
MAC = "MAC/MacUnicastTable"
LLDP = "LLDP/LLDPNeighbors"
ARP = "ARP/ArpTable"
# Old Sensors
GRPC_OLD_SENSOR_PATHS = [DEV_PHY, DEV_BOARDS, DEV_EXTPHY, IF_INTFS, IF_STATIS]


class MsgGenerator:
    def __init__(self, is_new, device_ip=None):
        with open("grpc_template/templates.json", "r+") as file:
            self.senDaDi = json.load(file)[KEY_SENSOR_PATHS]
        if is_new:
            self.jDataTuLi = [(s, j) for s, j in self.senDaDi.items() if s not in GRPC_OLD_SENSOR_PATHS] * 1000000
        else:
            self.jDataTuLi = [(s, self.senDaDi[s]) for s in GRPC_OLD_SENSOR_PATHS] * 10000
        self.device_ip = device_ip

    def __iter__(self):
        return self

    def __next__(self):
        try:
            sensor_path, json_data = self.jDataTuLi.pop()
            dial_msg = self.__2msg__(sensor_path, json_data)
            print(threading.currentThread().getName())
            return dial_msg
        except Exception:
            raise StopIteration

    def __2msg__(self, sensor_path, json_data):
        device_msg = grpc_dialout_pb2.DeviceInfo(producerName='H3C', deviceName='vSwitch', deviceModel='H3C S6850-56HF',
                                                 deviceIpAddr=self.device_ip, eventType='sample')
        dial_msg = grpc_dialout_pb2.DialoutMsg(deviceMsg=device_msg, sensorPath=sensor_path,
                                               jsonData=json_data)
        return dial_msg


def run():
    with grpc.insecure_channel('3.2.113.2:50051') as channel:
        g_client = dialout.GRPCDialoutStub(channel)
        msg_gen = MsgGenerator(is_new=True)
        g_client.Dialout(msg_gen)
    with grpc.insecure_channel('3.2.113.2:50051') as channel:
        g_client = dialout.GRPCDialoutStub(channel)
        msg_gen = MsgGenerator(is_new=False)
        g_client.Dialout(msg_gen)


if __name__ == '__main__':
    logging.basicConfig()
    tds = []
    for i in range(8):
        t = threading.Thread(target=run)
        tds.append(t)
        t.setDaemon(True)
        t.setName('thread %s' % i)
        t.start()
    for t in tds:
        t.join()

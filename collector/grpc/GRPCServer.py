import traceback
from concurrent import futures
import grpc
import grpc_dialout_pb2 as pb2
import grpc_dialout_pb2_grpc as dialout
import time
import configparser
import logging
import datetime


logging.basicConfig(
    level=logging.INFO,
    filemode="w",
    filename="log/grpc.log",
    format="[%(asctime)s][%(levelname)s]:%(message)s"
)

LISTEN_PORT = "listeningPort"

TIMESTAMP = "timestamp"
SOURCE = "src"
IP = "ip"
DATA = "data"
TOPIC_PREFIX = "avro.grpc."
GRPC = "grpc"
KAFKA = "kafka"
ENABLE = "enabled"

JSON_DATA = "jsonData"
SENSOR_PATH = "sensorPath"
DEVICE_NAME = "deviceName"
DEVICE_MODEL = "deviceModel"
PRODUCER_NAME = "producerName"

round = 0
deviceBaseTime = None
v4StartTime = None
v4EndTime = None
v6StartTime = None
v6EndTime = None

class GRPCServer(dialout.GRPCDialoutServicer):
    def __init__(self, config):
        # if config[KAFKA].get(ENABLE):
        #     import KafkaConnector
        #     self.kafka = KafkaConnector.KafkaConnector(config)
        logging.info("GRPCServer initiated")

    def Dialout(self, request_iterator, context):
        global round, v4StartTime, v4EndTime, v6StartTime, v6EndTime, deviceBaseTime
        for request in request_iterator:
            try:
                sensorPath = request.sensorPath
                jsonData = request.jsonData
                chunkMsg = request.chunkMsg
                nodeId = chunkMsg.nodeId
                totalFrag = chunkMsg.totalFragments
                deviceMsg = request.deviceMsg
                producerName = deviceMsg.producerName
                deviceName = deviceMsg.deviceName
                deviceModel = deviceMsg.deviceModel
                deviceIpAddr = deviceMsg.deviceIpAddr
                eventType = deviceMsg.eventType
                host_ip = context.peer().split(":")[1]
                if sensorPath == 'Device/Base':
                    if v4StartTime and v4EndTime and v6StartTime and v6EndTime and deviceBaseTime and v4EndTime >= v4StartTime > deviceBaseTime and v6EndTime >= v6StartTime > deviceBaseTime:
                        round = round + 1
                        logging.info('轮次%s，时间%s，IPv6发送延迟%s，IPv6传输耗时%s，IPv4发送延迟%s，IPv4传输耗时%s' % (
                        round, deviceBaseTime, v6StartTime-deviceBaseTime, v6EndTime-v6StartTime, v4StartTime-deviceBaseTime, v4EndTime-v4StartTime))
                        print('轮次%s，时间%s，IPv6发送延迟%s，IPv6传输耗时%s，IPv4发送延迟%s，IPv4传输耗时%s' % (
                        round, deviceBaseTime, v6StartTime-deviceBaseTime, v6EndTime-v6StartTime, v4StartTime-deviceBaseTime, v4EndTime-v4StartTime))
                    deviceBaseTime = datetime.datetime.now()
                    print('收到Device/Base')
                elif sensorPath == 'Route/Ipv4Routes':
                    if nodeId == 1:
                        v4StartTime = datetime.datetime.now()
                        print('收到首个IPv4Routes Chunk')
                    elif nodeId == totalFrag:
                        v4EndTime = datetime.datetime.now()
                        print('收到最后一个IPv4Routes Chunk')
                        if nodeId == 0:
                            v4StartTime = v4EndTime
                elif sensorPath == 'Route/Ipv6Routes':
                    if nodeId == 1:
                        v6StartTime = datetime.datetime.now()
                        print('收到首个IPv6Routes Chunk')
                    elif nodeId == totalFrag:
                        v6EndTime = datetime.datetime.now()
                        print('收到最后一个IPv6Routes Chunk')
                        if nodeId == 0:
                            v6StartTime = v6EndTime
            except Exception as err:
                print(request)
                traceback.print_exc()
        return pb2.DialoutResponse(response="")

def serve(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dialout.add_GRPCDialoutServicer_to_server(GRPCServer(config), server)
    server.add_insecure_port("[::]:%s" % config[GRPC].get(LISTEN_PORT))
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve("conf/grpc.properties")

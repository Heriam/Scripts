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


class GRPCServer(dialout.GRPCDialoutServicer):
    def __init__(self, config):
        # if config[KAFKA].get(ENABLE):
        #     import KafkaConnector
        #     self.kafka = KafkaConnector.KafkaConnector(config)
        logging.info("GRPCServer initiated")

    def Dialout(self, request_iterator, context):
        for request in request_iterator:
            try:
                print("[%s] %s" % (datetime.datetime.now(), request))
                # jsonData = json.loads(request.jsonData)
                # sensorPath = request.sensorPath
                # deviceMsg = request.deviceMsg
                # producerName = deviceMsg.producerName
                # deviceName = deviceMsg.deviceName
                # deviceModel = deviceMsg.deviceModel
                # host_ip = context.peer().split(":")[1]
                # topic = TOPIC_PREFIX + sensorPath.split("/")[-1].lower()
                # timestamp = int(jsonData["Notification"]["Timestamp"])
                # metadata = {
                #     TIMESTAMP: timestamp,
                #     SOURCE: GRPC,
                #     IP: host_ip,
                #     DATA: (
                #         '{ "' + JSON_DATA
                #         + '": {%s}, "' % request.jsonData
                #         + SENSOR_PATH
                #         + '": "%s", "' % sensorPath
                #         + DEVICE_NAME
                #         + '": "%s", "' % deviceName
                #         + DEVICE_MODEL
                #         + '": "%s", "' % deviceModel
                #         + PRODUCER_NAME
                #         + '": "%s"}' % producerName
                #     ).encode()
                # }
                # if self.config[KAFKA].get(ENABLE):
                #     self.kafka.publish(metadata, topic)
            except Exception as err:
                print(request)
                traceback.print_exc()
        return grpc_dialout_pb2.DialoutResponse(response="")

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

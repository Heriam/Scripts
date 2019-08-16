import json
import threading
import requests
import time
from collections import namedtuple
from KafkaConnector import KafkaConnector


class VCFCRequester:
    CFG_PATH = "cfg/subscription.json"

    def __init__(self):
        self.name = self.__class__.__name__
        try:
            with open(self.CFG_PATH) as f:
                self.cfg = json.loads(f.read(), object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        except Exception as e:
            self.console_info("error when loading configs. %s" % e)
        self.kafka = KafkaConnector(self.cfg.kafkaAddr)
        self.dataLock = threading.Lock()
        self.threads = []

    def console_info(self, info):
        print("[%s] %s" % (self.name, info))

    def subscribe(self, path, interval):
        url = "http://%s%s" % (self.cfg.vcfcIp, path)
        while True:
            metadata = {
                "timestamp": int(round(time.time() * 1000)),
                "src": "vcfc",
                "host_ip": self.cfg.vcfcIp,
                "rawdata": requests.get(url).content
            }
            self.kafka.publish(metadata, self.cfg.topic)
            time.sleep(interval)

    def run(self):
        for sensor in self.cfg.sensors:
            t = threading.Thread(target=self.subscribe, args=(sensor.path, sensor.interval))
            t.setDaemon(True)
            t.start()
            self.threads.append(t)
        for t in self.threads:
            t.join()

if __name__ == "__main__":
    VCFCRequester().run()
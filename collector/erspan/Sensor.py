import pyshark
import time, sys
from KafkaConnector import KafkaConnector


class Sensor:
    def __init__(self, interface, kafka_servers, timeout=None, interval=None, bpf_filter='ip proto 0x2f'):
        self.name = self.__class__.__name__
        self.interface = interface
        self.timeout = timeout
        self.interval = interval
        self.bpf_filter = bpf_filter
        self.capture = None
        self.on = False
        self.kafkaConnector = KafkaConnector(kafka_servers)

    def console_info(self, info):
        print('[%s][%s] %s' % (self.name, time.strftime('%Y-%m-%d %H-%M-%S',time.gmtime()), info))

    def run(self):
        self.capture = pyshark.LiveCapture(interface=self.interface, bpf_filter=self.bpf_filter)
        # self.capture = pyshark.FileCapture('C:\\Users\\j16492\\Desktop\\erspan.cap')
        while True:
            try:
                self.on = True
                self.capture.apply_on_packets(self.proc_pkt, timeout=self.timeout)
            except TimeoutError as terr:
                self.console_info('Timeout')
                self.on = False
            if self.interval:
                time.sleep(self.interval)
            else:
                return

    def proc_pkt(self, pkt):
        if not ('erspan' in pkt):
            return
        if 'tcp' in pkt:
            self.proc_tcp_pkt(pkt)

    def proc_tcp_pkt(self, pkt):
        metadata = {
            "timestamp": int(round(time.time()*1000)),
            "src": "erspan",
            "host_ip" : pkt[1].src,
            "rawdata": ('{ "src": "%s", "dst": "%s"}'% (pkt[5].src, pkt[5].dst)).encode()
        }
        self.kafkaConnector.publish(metadata, 'avro.mirror.erspan')

if __name__ == "__main__":
    if(len(sys.argv[1:])!=2) or sys.argv[1] == '--help':
        print('      Usage: python Sensor.py <interface> <kafka server ip:port list separated by "," with no space>')
    else:
        try:
            interface = sys.argv[1]
            kafka_servers = map(str, sys.argv[2].split(','))
            Sensor(interface, kafka_servers).run()
        except Exception as e:
            print(e)
            print('      Usage: python Sensor.py <interface> <kafka server ip:port list separated by "," with no space>')



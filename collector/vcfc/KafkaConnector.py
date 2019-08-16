import io
import time
import avro.schema
import avro.io
from kafka import KafkaProducer
import ssl


class KafkaConnector:
    AVRO_SCHEMA = '''
        {"namespace": "pnda.entity", 
         "type": "record",
         "name": "event",
         "fields": [
             {"name": "timestamp",   "type": "long"},
             {"name": "src",         "type": "string"},
             {"name": "host_ip",     "type": "string"},
             {"name": "rawdata",     "type": "bytes"}
         ]
        }
        '''

    def __init__(self, bootstrap_servers, ssl_enable=False):
        self.name = self.__class__.__name__
        self.sslEnable = ssl_enable
        self.schema = avro.schema.Parse(self.AVRO_SCHEMA)
        self.kafka_servers = bootstrap_servers
        self.producer = None
        self.consumer = None
        if self.sslEnable:
            self.console_info("setting up SSL to PROTOCOL_TLSv23")
            ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
            ctx.load_cert_chain(certfile="../ca-cert", keyfile="../ca-key", password="test1234")
            self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers, security_protocol="SASL_SSL",
                                     ssl_context=ctx,
                                     sasl_mechanism="PLAIN", sasl_plain_username="test", sasl_plain_password="test")
        else:
            self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    def console_info(self, info):
        print('[%s][%s] %s' % (self.name, time.strftime('%Y-%m-%d %H-%M-%S',time.gmtime()), info))

    def publish(self, metadata_dict, topic):
        writer = avro.io.DatumWriter(self.schema)
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        writer.write(metadata_dict, encoder)
        raw_bytes = bytes_writer.getvalue()
        self.producer.send(topic, raw_bytes)

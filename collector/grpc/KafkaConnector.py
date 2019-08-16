import io
import time
import avro.schema
import avro.io
from kafka import KafkaProducer
import logging

KAFKA_BROKERS = "kafkaBrokers"
SCHEMA_PATH = "schemaPath"
KAFKA = "kafka"


class KafkaConnector:
    def __init__(self, config):
        self.conf = config[KAFKA]
        schema = self.conf.get(SCHEMA_PATH)
        self.name = self.__class__.__name__
        with open(schema, "r") as f:
            self.schema = avro.schema.Parse(f.read())
        kafka_servers = self.conf.get(KAFKA_BROKERS).split(",")
        self.producer = None
        self.consumer = None
        self.producer = KafkaProducer(bootstrap_servers=kafka_servers)
        logging.info("KafkaConnector initiated")

    def publish(self, metadata_dict, topic):
        writer = avro.io.DatumWriter(self.schema)
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        writer.write(metadata_dict, encoder)
        raw_bytes = bytes_writer.getvalue()
        self.producer.send(topic, raw_bytes)

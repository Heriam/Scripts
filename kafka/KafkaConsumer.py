import Kafka

if __name__ == '__main__':


    class KafkaConnector:
        def __init__(self, config):
            self.name = self.__class__.__name__
            with open(schema, "r") as f:
                self.schema = avro.schema.Parse(f.read())
            kafka_servers = ['3.2.12.36:30091','3.2.12.37:30092','3.2.12.38:30093']
            self.consumer = KafkaProducer(bootstrap_servers=kafka_servers)
            logging.info("KafkaConnector initiated")

        def publish(self, metadata_dict, topic):
            writer = avro.io.DatumWriter(self.schema)
            bytes_writer = io.BytesIO()
            encoder = avro.io.BinaryEncoder(bytes_writer)
            writer.write(metadata_dict, encoder)
            raw_bytes = bytes_writer.getvalue()
            self.producer.send(topic, raw_bytes)
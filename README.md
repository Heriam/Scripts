
Kafka can be tuned to handle large messages. This can be done by configuring broker and consumer properties relating to maximum message and file sizes. However, before doing so, Cloudera recommends that you try and reduce the size of messages first. Review the following options that can help you reduce message size.
	* 
The Kafka producer can compress messages. For example, if the original message is a text-based format (such as XML), in most cases the compressed message will be sufficiently small.
	* 
Use the compression.type producer configuration parameters to enable compression. gzip, lz4, Snappy, and Zstandard are supported.//消息压缩
	* 
If shared storage (such as NAS, HDFS, or S3) is available, consider placing large files on the shared storage and using Kafka to send a message with the file location. In many cases, this can be much faster than using Kafka to send the large file itself.//共享存储
	* 
Split large messages into 1 KB segments with the producing client, using partition keys to ensure that all segments are sent to the same Kafka partition in the correct order. The consuming client can then reconstruct the original large message.//分段



启用消息压缩
压缩格式：lz4
参考资料：
https://intl.cloud.tencent.com/document/product/597/34004
https://blog.cloudflare.com/squeezing-the-firehose/
https://www.cnblogs.com/huxi2b/p/10330607.html



支持消息大小
属性
配置端
默认值
说明
调整值

























参考资料：
https://docs.cloudera.com/runtime/7.2.0/kafka-performance-tuning/topics/kafka-tune-large-messages.html
https://docs.cloudera.com/documentation/enterprise/6/6.3/topics/kafka_performance_large_messages.html
https://www.cnblogs.com/MyOnlyBook/p/10035670.html
https://www.cnblogs.com/doubletree/p/4264969.html
https://www.jianshu.com/p/61b6220a9ef2
https://blog.csdn.net/levy_cui/article/details/54695452
https://blog.csdn.net/sinat_27143551/article/details/93860869
https://zhuanlan.zhihu.com/p/107351723

Producer端

Broker端
	* 
message.max.bytes - this is the largest size of the message that can be received by the broker from a producer.
	* 
max.message.bytes - this is the largest size of the message the broker will allow to be appended to the topic. This size is validated pre-compression. (Defaults to broker's message.max.bytes.)
	* 
replica.fetch.max.bytes - this will allow for the replicas in the brokers to send messages within the cluster and make sure the messages are replicated correctly. If this is too small, then the message will never be replicated, and therefore, the consumer will never see the message because the message will never be committed (fully replicated).


Consumer端
	* 
fetch.message.max.bytes - this will determine the largest size of a message that can be fetched by the consumer.


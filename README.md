# NTP
# 开启NTP服务。

ntp-service enable

# 配置通过NTP协议获取时间。

clock protocol ntp

# 设置H3C的NTP服务器。

ntp-service unicast-server 10.63.5.112



# SNMP
# 开启设备SNMP，读团体名public，写团体名private

snmp-agent 

snmp-agent community write private

snmp-agent community read public

snmp-agent sys-info version all



# NetConf
# 开启设备NetConf, 使能用户名admin, 密码admin

local-user admin class manage



password simple admin



service-type telnet http https ssh terminal



service-type ftp



authorization-attribute user-role network-admin



authorization-attribute user-role network-operator



quit



netconf soap http enable



netconf soap https enable



netconf ssh server enable



public-key local create rsa



public-key local create dsa



ssh user admin service-type all authentication-type password



ssh server enable



line class vty



user-role network-operator



line vty 0 63



authentication-mode scheme



user-role network-admin



user-role network-operator



idle-timeout 0 0



quit



# gRPC
# 进入视图
telemetry

# 配置GRPC新采集组
sensor-group  grpc-new
sensor path resourcemonitor/resources
sensor path resourcemonitor/monitors
sensor path ifmgr/ethportstatistics
sensor path device/transceivers
sensor path buffermonitor/ecnandwredstatistics
sensor path buffermonitor/pfcstatistics
sensor path buffermonitor/pfcspeeds
sensor path buffermonitor/commheadroomusages
sensor path buffermonitor/ingressdrops
sensor path buffermonitor/egressdrops
sensor path buffermonitor/commbufferusages
sensor path route/ipv4routes
sensor path route/ipv6routes
sensor path mac/macunicasttable
sensor path arp/arptable
sensor path lldp/lldpneighbors
quit

# 配置GRPC事件采集组
sensor-group grpc-event
sensor path tcb/tcbpacketinfoevent
sensor path resourcemonitor/resourceevent
sensor path buffermonitor/portquedropevent
sensor path buffermonitor/portqueoverrunevent
quit

# 配置GRPC新目的地组
destination-group grpc-new
ipv4-address X.X.X.X port 50051
quit

# 配置GRPC新订阅策略
subscription grpc-new
sensor-group grpc-new sample-interval 60
sensor-group grpc-event
destination-group grpc-new
quit

# 配置GRPC老采集组
sensor-group grpc-old
sensor path ifmgr/interfaces
sensor path Ifmgr/statistics
sensor path device/extphysicalentities
sensor path device/boards
sensor path device/physicalentities
quit

# 配置GRPC老目的地组
destination-group grpc-old
ipv4-address X.X.X.X port 50052
quit

# 配置GRPC订阅策略
subscription grpc-old
sensor-group grpc-old sample-interval 25
destination-group grpc-old
quit

# SNMPTrap
# 开启设备SNMPTrap上报，默认上送 UDP 162 端口

snmp-agent target-host trap address udp-domain X.X.X.X params securityname public v2c

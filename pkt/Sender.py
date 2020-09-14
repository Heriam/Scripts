import threading
import scapy
from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import Ether
from scapy.sendrecv import sendpfast
import sys,os
import traceback
import logging
logger = logging.getLogger('ICS')
logger.setLevel(logging.DEBUG)
while logger.hasHandlers():
    for i in logger.handlers:
        logger.removeHandler(i)
formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s')
fh = logging.FileHandler(filename='log.log', encoding='utf-8', mode='w')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

if __name__ == '__main__':
    logger.info("instance initiated")
    pkt = Ether()/IP(dst="111.111.111.1-254")/TCP()/"hello there"
    sendpfast(pkt, pps=1000, loop=10000, parse_results=1)
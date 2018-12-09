#!/usr/bin/python
from scapy.all import *

def print_pkt(pkt):
	pkt.show()



pkt = sniff(filter='tcp [src|dst] port 23',prn=print_pkt)

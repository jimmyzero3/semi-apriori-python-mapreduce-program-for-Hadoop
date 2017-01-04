#!/usr/bin/env python

import os
import sys

def dataFromFile():
	
	for line in sys.stdin:
		lines = line.rstrip("\n").rsplit(" ")
		for word in lines:
			print '%s%s%d' % (word, '\t', 1)



if __name__ == "__main__":

	
	dataFromFile()
	

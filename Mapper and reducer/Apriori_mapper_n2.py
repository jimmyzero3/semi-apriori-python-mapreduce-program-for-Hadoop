#!/usr/bin/env python

import os
import sys
from collections import defaultdict

def readn1():
	Itemlist = set()
	with open('/your_path/MapRedSorted_n1_top100') as inf:
		for line in inf:
			parts = line.split('\t') # split line into parts
			if len(parts) > 1:   # if at least 2 parts/columns
				Itemlist.add(parts[0])   # only take column 1 , i.e. don't take the counting numbers

	return Itemlist


def readfile():	
	transactionList = list()
	itemSet = set()
	for record in sys.stdin:
		transaction = frozenset(record.rstrip("\n").rsplit(" "))
		transactionList.append(transaction)
		for item in transaction:
			itemSet.add(frozenset([item]))
	return itemSet, transactionList


def counting(Trans,top100ls):

	for tran in Trans:
		bucket = defaultdict(list)

		for item in tran:
			if( item in top100ls ):
				bucket[item] += [item]

		for item1 in bucket:
			for item2 in bucket:
				if( item1 < item2 ):
					print '%s%s%d' % (','.join([item1,item2]),'\t',1)



if __name__ == "__main__":

	AllItems, Transactions = readfile()
	n1_top100_Items = readn1() 
	counting(Transactions,n1_top100_Items)


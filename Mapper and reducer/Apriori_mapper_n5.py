#!/usr/bin/env python

import os
import sys
from collections import defaultdict

def readn4():
	Itemlist = set()
	with open('/home/yuki_n/MapRedSorted_n4_top100') as inf:
		for line in inf:
			parts = line.split('\t')
			items = parts[0].split(',')
			if len(parts) > 1:
				Itemlist.add(items[0])
				Itemlist.add(items[1])
				Itemlist.add(items[2])
				Itemlist.add(items[3])

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
				for item3 in bucket:
					for item4 in bucket:
						for item5 in bucket:
							if( item1 < item2  and item2 < item3 and item3 < item4 and item4 < item5):
								print '%s%s%d' % (','.join([item1,item2,item3,item4,item5]),'\t',1)


if __name__ == "__main__":

	AllItems, Transactions = readfile()
	n4_top100_Items = readn4() 

	counting(Transactions,n4_top100_Items)

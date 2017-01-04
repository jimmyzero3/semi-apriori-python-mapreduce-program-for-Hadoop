#!/usr/bin/env python

import os
import sys
from collections import defaultdict

def readn2():
	Itemlist = set()
	with open('/your_path/MapRedSorted_n2_top100') as inf:
		for line in inf:
			parts = line.split('\t') # split line into parts
			items = parts[0].split(',')
			if len(parts) > 1:   # if at least 2 parts/columns
				Itemlist.add(items[0])  # take column 1
				Itemlist.add(items[1])  # and column 2 , the other nK mappers are the same logic 

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
					if( item1 < item2  and item2 < item3 ):
						print '%s%s%d' % (','.join([item1,item2,item3]),'\t',1)



if __name__ == "__main__":

	AllItems, Transactions = readfile()
	n2_top100_Items = readn2() 
	counting(Transactions,n2_top100_Items)


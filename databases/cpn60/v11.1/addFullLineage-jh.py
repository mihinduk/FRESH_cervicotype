#!/usr/bin/python

import sys, string

if len(sys.argv) != 3:
	print 'addFullLineage.py taxonomyFile fastaFile'
	sys.exit()

f1 = open(sys.argv[1], 'r').readlines()
hash = {} #lineage map

for line in f1[1:]:
	cols = line.strip().split('\t')
	lineage = ['Root']
	for node in cols[1:]:
		if not node == '-':
			lineage.append(node)
	ID = cols[0]
	lineage = string.join(lineage, ';')
	hash[ID] = lineage

f2 = open(sys.argv[2], 'r').readlines()

for line in f2:
	if line[0] == '>':
		extract_from = line.strip().replace(">", "").split()		# Added ".split" to actually separate the header
		ID = extract_from[0]							# from which we only want the first "word"
		
		try:
			lineage = hash[ID]
		except KeyError:
			print ID, 'not in taxonomy file'
			sys.exit()
		print ">" + ID + '\t' + lineage					#changed from print line.strip() to get correct defline
	else:
		print line.strip()



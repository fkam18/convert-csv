#!/usr/bin/python3
# 7 Jan 2022 fkam
# convert csv into mysql datetime field type for import
import sys
import csv

for line in sys.stdin:
	line1 = line.rstrip()
	rows = csv.reader(sys.stdin)
	for each_row in rows:
		time1 = each_row[4].split(' ')
		if (len(time1) > 1):
			date = time1[0].split('/')
			time2 = time1[1].split(':')
			print(each_row[0]+','+ each_row[1] + ',"' + each_row[2] + '",' + each_row[3] + '","' +"20"+date[2]+"-"+date[1]+"-"+ date[0]+" "+ time2[0]+":"+time2[1]+":"+ "00" + '"')
		else:
			print("error")

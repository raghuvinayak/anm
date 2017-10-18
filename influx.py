#!usr/bin/python

import sys
import datetime
from influxdb import InfluxDBClient
import os
import time



client=InfluxDBClient('10.0.1.101',8086,'stark','stark',database='stark')
client.create_database('stark')
def store(bit_rate,time):
      json=[
              {
              "measurement":"tablename",
              "tags":{
                       "tag":"sample",

                       },
                       "time":time,
                       "fields":{
                               "bit_rate":bit_rate

                       }
      }
      ]
      client.write_points(json,time_precision='u')


"""

f= os.fdopen(sys.stdin.fileno(),'r',0)
for line in f:
	print line
"""
while True:
	line= raw_input()
	elements=line.strip().split()
	if len(elements) == 2:
		bit_rate=elements[1]
		unixtime = elements[0].split('.')

		try:
			int(unixtime[0])			
			stdtime = datetime.datetime.utcfromtimestamp(long(float(unixtime[0]))).strftime('%Y-%m-%dT%H:%M:%S')
			influxtime = ".".join([stdtime,unixtime[1]])
			#print (unixtime[0] + "          " + unixtime[1]  + "      " + elements[1])
			
			store(bit_rate,influxtime)
		except:
			pass


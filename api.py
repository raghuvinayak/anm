#!flask/bin/python

import sys
import socket
import threading
from flask import Flask
from flask import send_file
import os
import time
from multiprocessing import Process
import subprocess, shlex



app = Flask(__name__)



#DPMI strings 
@app.route('/run/<string:stream>', methods = ['GET'])
def start_process(stream):
	address = stream.split('_')
	global don
	don=address[0]
	global gstream
	gstream = '::'.join(address[1:])
	Process(target = start_king(stream)).start()
	return "please wait........"

#stop DPMI utils

@app.route('/stop', methods=['GET'])
def stop_service():
         os.system("sudo pkill bitrate")
#sudo pkill bitrate
         return "DPMI bitrate stoped\n"

#add New stream

@app.route('/add/<string:NewStream>', methods=['GET'])
def add_stream(NewStream):

	#       gstream=start_process(stream)
	address = NewStream.split('_')
	global don
	don=address[0]
	addstream = '::'.join(address[1:])
	stop_service()
	time.sleep(1)
	global gstream
	gstream=gstream+' '+addstream
	start_process(don+"_"+ gstream)
	return "stream added\n"

#delete stream

@app.route('/delete/<string:deletestream>', methods=['GET'])
def delete_stream(deletestream):
	 address = deletestream.split('_')
	 global don
	 don=address[0]
	 delstream = '::'.join(address[1:])
	 NewStream = gstream.replace(delstream,'')
	 stop_service()
	 time.sleep(1)
	 start_process(don+"_"+ NewStream)
	 return "stream deleted\n"


@app.route('/showstream', methods=['GET'])
def show_service():
#sudo pkill bitrate myName
	return gstream[1:]


#change stream
@app.route('/change/<string:changestream>', methods=['GET'])
def new_stream(changestream):
	 address = changestream.split('_')
	 global don
	 don=address[0]
	 changestream = '::'.join(address[1:])
	 stop_service()
	 time.sleep(1)
	 start_process(address[0]+"_"+ changestream)
	 return "stream changed\n"



def start_king(stream):
        dpmi(stream).start()
        return "please wait \n"



# Piping done two types  which is using subprocess or exicute commands directly throuth os.system

#def subprocess_cmd(command):
#    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
#    proc_stdout = process.communicate()[0].strip()
#    print proc_stdout


def start_service(stream):
        os.system("unbuffer -p bitrate -i " + don +" --absolute-time --format=matlab " +gstream+ "| python influx.py ")


class dpmi(threading.Thread):
        def __init__(self,stream):
              threading.Thread.__init__(self)
              self.stream = stream
        def run(self):
            start_service(self.stream)


if __name__=='__main__':
       app.run(host ='0.0.0.0')





import sys
import time
import socket
import rrdtool

UDP_IP = "0.0.0.0"
UDP_PORT = 7777
float 

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
 
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    new = float(data)
    ret = rrdtool.update('/media/kingdian/ldr_data.rrd','N:' + `new`);
    print "LDR:", data
    sys.stdout.flush()
    ret = rrdtool.graph("/media/kingdian/light.png",
                  '--imgformat', 'PNG',
                  '--width', '790',
                  '--height', '300',
                  '--start', "-64800",
                  '--end', "now",
                  '--vertical-label', 'intensity',
                  '--title', 'LDR_sensor',
         #         '--lower-limit', '0',
                  'DEF:light=/media/kingdian/ldr_data.rrd:light:MAX',
                  'LINE1:light#8700af:light')

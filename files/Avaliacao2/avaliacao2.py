#!/usr/bin/python3
import os

listIntevals = ['0.1','0.01','0.001']
listPacketSize = ['64','128','512','1024']
listNodes = ['6','11','16','21','26','31','33']

commandNs3 = './waf --run '
localArquivo = '"scratch/mesh-2018-avaliacao2 '
ySize = '--y-size=1 '
step = '--step=90 '
packetInterval = ''
packetSize = ''
xSize = ''
jumps = ''

#./waf --run "scratch/mesh-2018-test --y-size=1 --step=90 --packet-interval=0.1 --packet-size=1024 --x-size=13 --jumps=13"

for x in range(len(listIntevals)):
    packetInterval = '--packet-interval='   
    packetInterval = packetInterval + listIntevals[x] + ' '
    for z in range(len(listNodes)):
        xSize = '--x-size='
        jumps = '--jumps='
        xSize = xSize + listNodes[z] + ' '
        jumps = jumps + listNodes[z] + '"'
        for y in range(len(listPacketSize)):
            packetSize = '--packet-size='
            packetSize = packetSize + listPacketSize[y] + ' '           
            finalString = localArquivo + ySize + step + packetInterval + packetSize + xSize + jumps
            commandline = commandNs3 + finalString       
            print(commandline)
            os.system(commandline)
            


        
        
    


        
        
    

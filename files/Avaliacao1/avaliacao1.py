#!/usr/bin/python3
import os

listIntevals = ['0.1','0.01','0.001']
listPacketSize = ['64','128','512','1024']
listSteps = ['10','20','30','40','50','60','70','80','90','95','96','98','100','101','102','103','104','105']

commandNs3 = './waf --run '
localArquivo = '"scratch/mesh-2018-avaliacao1 '
ySize = '--y-size=1 '
xSize = '--x-size=2 '
packetInterval = ''
packetSize = ''
step = ''

for x in range(len(listIntevals)):
    packetInterval = '--packet-interval='   
    packetInterval = packetInterval + listIntevals[x] + ' '
    for z in range(len(listSteps)):     
        step = '--step='
        step = step + listSteps[z] + ' '    
        for y in range(len(listPacketSize)):
            packetSize = '--packet-size='
            packetSize = packetSize + listPacketSize[y] + '"'
            finalString = localArquivo + ySize + xSize + packetInterval + step + packetSize     
            commandline = commandNs3 + finalString       
            print(commandline)
            os.system(commandline)
            


        
        
    


        
        
    

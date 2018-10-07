#!/usr/bin/python3
import os

listFlows = ['1','2','3','4','5']
listIntevals = ['0.1','0.01','0.001']
listPacketSize = ['64','128','512','1024']


commandNs3 = './waf --run '
localArquivo = '"scratch/mesh-2018-avaliacao3 '
ySize = '--y-size=4 '
xSize = '--x-size=4 '
step = '--step=90 '
referencia = '--n=false '
packetInterval = ''
packetSize = ''
flows = ''


for y in range(len(listIntevals)):
    packetInterval = '--packet-interval='   
    packetInterval = packetInterval + listIntevals[y] + ' '
    for x in range(len(listFlows)):
        flows = '--numFlows='
        flows = flows + listFlows[x] + ' '            
        for z in range(len(listPacketSize)):
            packetSize = '--packet-size='
            packetSize = packetSize + listPacketSize[z] + '"'            
            finalString = localArquivo + ySize + xSize + step + referencia + packetInterval + flows + packetSize 
            commandline = commandNs3 + finalString 
            for a in range(5):
                if listPacketSize[z] == '1024' and a == 4:
                    referencia = '--n=true '
                    finalString = localArquivo + ySize + xSize + step + referencia + packetInterval + flows + packetSize 
                    commandline = commandNs3 + finalString 
                print(commandline)
                referencia = '--n=false '
                os.system(commandline)
        
        
        


            


        
        
    


        
        
    

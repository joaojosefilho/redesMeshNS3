#!/usr/bin/python3
import os
import csv
import re

leitura = ['taxaEntrega.csv','atrasoMedio.csv','variacaoAtraso.csv','vazao.csv']
escrita = ['mediaTaxaEntrega.csv','mediaAtrasoMedio.csv','mediaVariacaoAtraso.csv','mediaVazao.csv']


for arquivo in range(len(leitura)):
    fin = open(leitura[arquivo], mode='r')
    fout = open(escrita[arquivo], mode='w')
    
    

    agrupamento = [5,10,15,20,25]
    aux = 0    
    reader = csv.reader(fin, delimiter=';')    
    writer = csv.writer(fout, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)


    dataset = list(reader)
    media = 0.0
    linha = []
    celula = ' Fluxo'
    
    writer.writerow(['Fluxos','64B','128B','512B','1024B'])

    for x in range(len(dataset)): 
        celula = str(x+1) + celula  
        linha.append(celula)
        for cell in dataset[x]:            
            if(cell != ''):
                if(cell == '-nan'):
                    number = 0.0
                else:
                    number = float(cell)                                         
                if(aux < agrupamento[x]):                                    
                    media = media + number
                    aux = aux + 1                    
                else:
                    media = media/float(agrupamento[x])
                    linha.append(media)                
                    aux = 0
                    media = 0.0
                    media = media + number
                    aux = aux + 1                
        media = media/float(agrupamento[x])
        linha.append(media)
        writer.writerow(linha)
        celula = ' Fluxos'
        linha.clear()    
        aux = 0
        media = 0.0

    fin.close()
    fout.close()
print('Arquivos gerados com sucesso!')    


#!/usr/bin/python3
import os
import csv
import re

leitura = ['taxaEntrega.csv','atrasoMedio.csv','variacaoAtraso.csv','vazao.csv']
escrita = ['mediaTaxaEntrega.csv','mediaAtrasoMedio.csv','mediaVariacaoAtraso.csv','mediaVazao.csv']

#leitura = ['atrasoMedio.csv']
#escrita = ['mediaAtrasoMedio.csv']

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
    decrementarMedia = 0
    #auxDecrementarMedia para qquando um -nan ou 0 estiver como sendo o primeiro valor de uma cadeia de fluxos
    auxDecrementarMedia = 0
    
    writer.writerow(['Fluxos','64B','128B','512B','1024B'])    
    for x in range(len(dataset)):         
        celula = str(x+1) + celula  
        linha.append(celula)
        for cell in dataset[x]:            
            if(cell != ''):                
                if(cell == '-nan' or cell == '0'):
                    if(aux < agrupamento[x]):
                        decrementarMedia = decrementarMedia + 1
                    else:
                        auxDecrementarMedia = 1
                    number = 0.0
                else:                    
                    number = float(cell)                                         
                
                if(aux < agrupamento[x]):                                                        
                    media = media + number                                 
                    aux += 1                            
                else:
                    media = media/float(agrupamento[x] - float(decrementarMedia))     
                    linha.append(media)                
                    aux = 0
                    media = 0.0
                    decrementarMedia = 0
                    decrementarMedia = auxDecrementarMedia
                    auxDecrementarMedia = 0
                    media = media + number
                    aux += 1   
        media = media/float(agrupamento[x] - float(decrementarMedia))
        linha.append(media)
        writer.writerow(linha)
        celula = ' Fluxos'
        linha.clear()    
        aux = 0
        media = 0.0
        decrementarMedia = 0

    fin.close()
    fout.close()
print('Arquivos gerados com sucesso!')    


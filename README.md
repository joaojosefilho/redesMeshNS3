# Execução automática das simulações

## É necessário instalar o python 3

https://docs.python-guide.org/starting/install3/linux/

## Simulações automáticas da avaliação 1

+ copie a pasta 'avaliacao1' para dentro da sua pasta ns-3.x(Paste onde é exucutado o comando ./waf) (ex: home/joaojosefilho/NS3.27/ns-3-allinone/ns-3.27$).  
+ copie o arquivo 'mesh-2018-avaliacao1.cc' para dentro da sua pasta 'scratch' que fica dentro da pasta ns-3.x(Paste onde é exucutado o comando ./waf).  
+ copie o arquivo avaliacao1.py para dentro da sua pasta ns-3.x(Paste onde é exucutado o comando ./waf).  

### Descrição dos arquivos

**Pasta 'avaliacao1':** Dentro dessa pasta existem três outras pastas: 01, 001 e 0001(Referêntes ao intervalo entre o envio dos pacotes). Dentro de cada uma dessas pastas, vão ser criados 4 arquivos csv: taxaEntrega.csv, vazao.csv, atrasoMedio.csv(Delay Mean), variacaoAtraso.csv(Jitter). Esses arquivos vão armazenar os resultados das simulações.

**Arquivo 'mesh-2018-avaliacao1.cc':** arquivo da professora Carina apresentando algumas modificação no código para escrever em um arquivo csv.

**Arquivo 'avaliaco1.py':** scripty em python para executar altomaticamente os comandos ./waf. Dentro Desse arquivo existem três listas, que representão os valores que seram modificados ao decorrer dos comandos ./waf. Os Atributos --y-size=1 e --x-size=2 são fixos, por isso não foi necessário fazer listas.

listIntevals = ['0.1','0.01','0.001']  
listPacketSize = ['64','128','512','1024']  
listSteps = ['10','20','30','40','50','60','70','80','90','95','96','98','100','101','102','103','104','105']  

### Execução:

``` bash
Vá para pasta onde o scripty avaliacao1.py está.  
Para executar o scripty python utilize o seguinte comando:  
$ ./avaliacao1.py

Se der permissão negada use o camando:  
$ chmod 777 avaliacao1.py

Quando o comando for finalizado, as pastas 01, 001 e 0001 vão conter arquivos csv que contém os resultados das simulações.  
Os arquivos csv não contem os cabeçalhos das linhas e colunas. Abaixo estará o cabeçalho

Cabeçalho:  
Distância | 64B | 128B | 512B | 1024B
----------| --- | ---- | ---- | -----
10        |     |      |      |
20        |     |      |      |
30        |     |      |      |
40        |     |      |      |
50        |     |      |      |
60        |     |      |      |
70        |     |      |      |
80        |     |      |      |
90        |     |      |      |
95        |     |      |      |
96        |     |      |      |
98        |     |      |      |
100       |     |      |      |
101       |     |      |      |
102       |     |      |      |
103       |     |      |      |
104       |     |      |      |
105       |     |      |      |

Se quiser executar a simulação novamente, é necessário apagar os arquivos csv dentro das pastas 01,001 e 0001
```



## Simulações automáticas da avaliação 2

+ copie a pasta 'avaliacao2' para dentro da sua pasta ns-3.x(Paste onde é exucutado o comando ./waf) (ex: home/joaojosefilho/NS3.27/ns-3-allinone/ns-3.27$).  
+ copie o arquivo 'mesh-2018-avaliacao2.cc' para dentro da sua pasta 'scratch' que fica dentro da pasta ns-3.x(Paste onde é exucutado o comando ./waf).  
+ copie o arquivo avaliacao2.py para dentro da sua pasta ns-3.x(Paste onde é exucutado o comando ./waf).  

### Descrição dos arquivos

**Pasta 'avaliacao2':** Dentro dessa pasta existem três outras pastas: 01, 001 e 0001(Referêntes ao intervalo entre o envio dos pacotes). Dentro de cada uma dessas pastas, vão ser criados 4 arquivos csv: taxaEntrega.csv, vazao.csv, atrasoMedio.csv(Delay Mean), variacaoAtraso.csv(Jitter). Esses arquivos vão armazenar os resultados das simulações.

**Arquivo 'mesh-2018-avaliacao3.cc':** arquivo da professora Carina apresentando algumas modificação no código para escrever em um arquivo csv. O trabalhos da professora Carina pede para estudar o impacto do número de saltos entre uma fonte e um destino. O código também foi alterado para que o último nó sempre envie pacotes para o primeiro. Ex: Se tever 20 nós em linha, o 10.1.1.20 vai enviar para o 10.1.1.1. Por esse motivo, eu adicionei mais um atributo no código, o --jumps. Esse atributo vai guardar o numero de saltos que a simulação vai fazer. O numero de saltos sempre vai ser igual ao numero de nós menos 1 (--x-size - 1 = jumps). Ex: Se tiver uma rede em linha com 20 nós, vão ser dados 19 saltos. Para facilitar, eu coloquei para o --jumps receber o numero de nós e na hora de rodar o código, eu diminuo 1 do --jumps.

**Exemplo do camando com o novo atributo**  
./waf --run "scratch/mesh-2018-test --y-size=1 --step=90 --packet-interval=0.1 --packet-size=1024 --x-size=13 --jumps=13"

**Arquivo 'avaliaco2.py':** scripty em python para executar altomaticamente os comandos ./waf. Dentro Desse arquivo existem três listas, que representão os valores que seram modificados ao decorrer dos comandos ./waf. Atributos como --y-size=1 --step=90 são fixos, por isso não foi necessário fazer listas.

listNodes = ['6','11','16','21','26','31','33'] //lista de nós   
listIntevals = ['0.1','0.01','0.001'] //packetInterval  
listPacketSize = ['64','128','512','1024'] //packetSize

A lista de saltos vai ser igual a listNodes menos 1  
['5','10','15','20','25','30','32']

O protocolo que a professora Carina utilizou só permite até 32 saltos

### Execução:

``` bash
Vá para pasta onde o scripty avaliacao2.py está.  
Para executar o scripty python utilize o seguinte comando:  
$ ./avaliacao2.py

Se der permissão negada use o camando:  
$ chmod 777 avaliacao2.py

Quando o comando for finalizado, as pastas 01, 001 e 0001 vão conter arquivos csv que contém os resultados das simulações.  
Os arquivos não contem os cabeçalhos das linhas e colunas

Cabeçalhos:  
Nº de saltos | 64B | 128B | 512B | 1024B
------------ | --- | ---- | ---- | -----
5            |     |      |      |
10           |     |      |      |
15           |     |      |      |
20           |     |      |      |
25           |     |      |      |
30           |     |      |      |
32           |     |      |      |

Se quiser executar a simulação novamente, é necessário apagar os arquivos csv dentro das pastas 01,001 e 0001
```

## Simulações automáticas da avaliação 3
    
+ copie a pasta 'avaliacao3' para dentro da sua pasta ns-3.x(Paste onde é exucutado o comando ./waf) (ex: home/joaojosefilho/NS3.27/ns-3-allinone/ns-3.27$).  
+ copie o arquivo 'mesh-2018-avaliacao3.cc' para dentro da sua pasta 'scratch' que fica dentro da pasta ns-3.x(Paste onde é exucutado o comando ./waf).  
+ copie o arquivo avaliacao3.py para dentro da sua pasta ns-3.x(Paste onde é exucutado o comando ./waf).

### Descrição dos arquivos

**Pasta 'avaliacao3':** Dentro dessa pasta existem três outras pastas: 01, 001 e 0001(Referêntes ao intervalo entre o envio dos pacotes). Dentro de cada uma dessas pastas, vão ser criados 5 arquivos csv: fluxo.csv, taxaEntrega.csv, vazao.csv, atrasoMedio.csv(Delay Mean), variacaoAtraso.csv(Jitter). Esses arquivos vão armazenar os resultados das simulações. 

**calcularMedia.py:** Esse scripty está presente nas pastas 01, 001 e 0001 e é responsável por calcular as médias. Vão ser gerados 4 arquivos csv: mediaTaxaEntrega.csv, mediaVazao.csv, mediaAtrasoMedio.csv(Delay Mean), mediaVariacaoAtraso.csv(Jitter). Esses 5 arquivos vão armazenas as médias.

**Arquivo 'mesh-2018-avaliacao3.cc':** arquivo da professora Carina apresentando algumas modificação no código para escrever em um arquivo csv.

**Arquivo'avaliaco3.py':** scripty em python para executar altomaticamente os comandos ./waf. Dentro Desse arquivo existem três listas, que representão os valores que seram modificados ao decorrer dos comandos ./waf. Atributos como --y-size=4 --x-size=4 são fixos, por isso não foi necessário fazer listas.

listFlows = ['1','2','3','4','5'] //Fluxos  
listIntevals = ['0.1','0.01','0.001'] //packetInterval  
listPacketSize = ['64','128','512','1024'] //packetSize

### Execução:

``` bash
Vá para pasta onde o scripty avaliacao3.py está.

Para executar o scripty python utilize o seguinte comando:  
$ ./avaliacao3.py

Se der permissão negada use o camando:  
$ chmod 777 avaliacao3.py

Quando o comando for finalizado, as pastas 01, 001 e 0001 vão conter arquivos csv que contém os resultados das simulações.  
Dentro de cada uma dessas pastas, existe um scripty chamado de calcularMedia.py que vai calcular as médias das simulações.  

Para executar o scripty python utilize o seguinte comando:  
$ ./calcularMedia.py

Se der permissão negada use o camando:  
$ chmod 777 calcularMedia.py

Se quiser executar a simulação novamente, é necessário apagar os arquivos csv dentro das pastas 01,001 e 0001.  
Não apagar calcularMedia.py.
```

import matplotlib.pyplot as plt
from itertools import chain
import json
import urllib.request as req


def BancoDeDados():
   url = "http://albertocn.sytes.net/2019-2/pi/projeto/geracao_energia.json"
   requisicao = req.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
   try:
     dados = req.urlopen(requisicao).read().decode()
     dados_proc = json.loads(dados)
   except:
     print('deu erro :(')
   return(dados_proc) #[x:x] para escolher o dia 


#A função a seguir faz uma lista de listas com as potencias de uma hora
# Pegando os intervalos(das potências) de uma hora ()
def IntervalosHora():
   dados = BancoDeDados()
   for dicionarios in dados:
       potencias = dicionarios["potencia"]
   quantidade_listas = 16
   intervalos_separados = []
   tamanho = len(potencias) ## potencias não ta definido
   for contador in range(quantidade_listas):
       inicio = int(contador*tamanho/quantidade_listas)
       fim = int((contador+1)*tamanho/quantidade_listas)
       intervalos_separados.append(potencias[inicio:fim])
   return(intervalos_separados)


## Tirando os -1
def IntervalosSemMenosUm():
   intervalos_separados = IntervalosHora()
   for potencia_lista in intervalos_separados:
     for potencia in potencia_lista:
       if potencia == -1:
          potencia_lista.append(1)
   return(intervalos_separados)

# Fazendo a media das potencias
##A função a seguir faz a medias das potencias nos intervalos
def MediaPotencias():
   intervalos_separados = IntervalosSemMenosUm()
   potencias_media = list()
   for potencia_lista in intervalos_separados:
     media = sum(potencia_lista)/12
     potencias_media.append(media)
   return(potencias_media)

## Pegando as horas
def Horas():
   horas = ['5:00-6:00', '6:00-7:00',
            '7:00-8:00', '8:00-9:00',
            '9:00-10:00', '10:00-11:00',
            '11:00-12:00', '12:00-13:00',
            '13:00-14:00', '14:00-15:00',
            '15:00-16:00', '16:00-17:00',
            '17:00-18:00', '18:00-19:00',
            '19:00-20:00', '20:00-21:00']
   return(horas)

def FiltrarEntrada():
   potencias = MediaPotencias()
   horas = Horas()
   return(horas,potencias)

def GerarGrafico(x, y):
   plt.bar(x, y,label = 'Potência (kwh)',color='#7FFFD4')
   plt.title('Potência (kwh) por hora')
   plt.legend(bbox_to_anchor=(1, 1), loc=4) ##Legenda
   plt.xlabel('Horário')
   plt.ylabel('Potência (kwh)')
   plt.savefig('barras.png')
   plt.close()

def ApresentarGraficoDeBarras():
   plt.rcParams['figure.figsize'] = (11, 5) ##tamanho grafico
   plt.style.use('dark_background') ## tema do fundo
   plt.grid(True) ##tracejado
   plt.xticks([0,3,6,9,
               12,15]) #Intervalos eixo x 
   tuplaDados = FiltrarEntrada()
   GerarGrafico(tuplaDados[0], tuplaDados[1])

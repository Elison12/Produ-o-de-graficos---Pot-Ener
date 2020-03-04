import matplotlib.pyplot as plt
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
   return(dados_proc)

# Organizando o banco de dados pela data 
def BancoDeDadosOrganizado():
  dados_proc = BancoDeDados()
  dados_organizados = sorted(dados_proc,key=lambda k:k['dia'])
  return(dados_organizados)



# Pegando as energias de cada mês e colocando em uma lista (a posição da lista indica o mês)
def EnergiasListas():
   dados_organizados = BancoDeDadosOrganizado()
   transformar_em_lista = list()
   energias_mes = list()
   mes_comparador = 1
   while mes_comparador != 13:
     for dicionarios in dados_organizados:
       data = dicionarios['dia']
       mes = data[(data.find('-') + 1):7]
       energia = dicionarios['energiaDia']
       if mes < '10':
         if str(mes) == ('0'+str(mes_comparador)):
           transformar_em_lista.append(energia)
       elif mes == str(mes_comparador):
           transformar_em_lista.append(energia)
     energias_mes.append(transformar_em_lista)
     transformar_em_lista = list()
     mes_comparador = mes_comparador + 1
   return(energias_mes)
    

def FiltrarEntrada():
   energias = EnergiasListas()
   meses = ['Jan','Fev','Mar',
            'Abr','Mai','Jun',
            'Jul','Ago','Set',
            'Out','Nov','Dez']
   return(meses,energias)
    

def GerarGrafico(x, y):
   plt.boxplot(y, labels=x)
   plt.title('Geração de energia ao longo de um ano (Meses)')
   plt.xlabel('Meses (2019)')
   plt.ylabel('Energia gerada (kwh)')
   plt.savefig('boxplot.png')
   plt.close()



def ApresentarGraficoBoxplot():
   plt.style.use('classic') ## tema do fundo 
   plt.rcParams['figure.figsize'] = (11, 5) ##tamanho grafico
   tuplaDados = FiltrarEntrada()
   GerarGrafico(tuplaDados[0], tuplaDados[1])

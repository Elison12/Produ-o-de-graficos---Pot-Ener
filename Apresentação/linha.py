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


# Organizando dados 
#A função a seguir organiza o ano
def BancoDeDadosOrganizado():
   dados_proc = BancoDeDados()
   dados_organizados = sorted(dados_proc,key=lambda k:k['dia'])
   return(dados_organizados)

##A funçãoa seguir lista os dias do ano em uma lista de inteiros
def DiasDoAno():
   dias = list()
   for dia in range(1, 366):
    dias.append(dia)
   return(dias)

'''lista as energias do ano 
obs: tamanho da lista 365'''
def EnergiasDoAno():
   energias = list()
   dados_organizados = BancoDeDadosOrganizado()
   for dicionarios in dados_organizados:
    energia_do_dia = dicionarios["energiaDia"]
    energias.append(energia_do_dia)
   return(energias)

'''
A função a seguir retorna os dias do ano em uma lista
e as energias em outras'''
def FiltrarEntrada():
   dias = DiasDoAno()
   energias = EnergiasDoAno()
   return(dias,energias) 

# Gerar o Gráfico usando a biblioteca
def GerarGrafico(x, y):
   plt.plot(x, y, color='#7FFFD4',linewidth=0.25, linestyle="-")
   plt.title('Geração de energia ao longo de um ano')
   plt.xlabel('Dias (2019)')
   plt.ylabel('Energia gerada (kwh)')
   plt.savefig('linha.png')
   plt.close()
   

def ApresentarGraficoDeLinha():
   plt.style.use('dark_background') ## tema do fundo 
   plt.rcParams['figure.figsize'] = (11, 5) ##tamanho grafico
   plt.xticks([1,73,146,219,292,365]) #Intervalos eixo x
   plt.yticks([0,5,11,21,31])  #Intervalos eixo y
   tuplaDados = FiltrarEntrada()
   # Pintado area da linha
   x = tuplaDados[0]
   y = tuplaDados[1]
   plt.fill_between(x, y, color='#7FFFD4')
   # plt.fill_between(x, y, color='None')
   plt.grid(True) ##tracejado
   plt.legend(['Dias (kwh)'],bbox_to_anchor=(1, 1), loc=4, borderaxespad=0.) ## Legenda
   GerarGrafico(tuplaDados[0], tuplaDados[1])

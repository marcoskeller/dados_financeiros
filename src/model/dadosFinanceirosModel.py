import src.controller.dadosFinanceirosController as dadosController
from data import dadosBolsaValores as baseDadosData



#Paises Para Consulta  
def paises():
    resultado = baseDadosData.DadosFinanceirosBancoDeDados.paises()
    return resultado


#Acoes Disponiveis no Yahoo Finance        
def acoesYahooFinance():
    resultado = baseDadosData.DadosFinanceirosBancoDeDados.acoesYahooFinance()
    return resultado


#Intervalo da Consulta
def intervalo(): 
    resultado = baseDadosData.DadosFinanceirosBancoDeDados.intervalo()
    return resultado

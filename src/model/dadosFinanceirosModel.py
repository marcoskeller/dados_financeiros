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


#Formatando as Datas
def format_date(dt, format='%d/%m/%Y'):
	return dt.strftime(format)


#Solicitar Dados Acao Brasileira
def solicitarDadosAcoesBrasileira(acaoEscolhida, data_inicial, data_final):
     resultado = baseDadosData.DadosFinanceirosBancoDeDados.obterDadosAcoesBrasileira(acaoEscolhida, data_inicial, data_final)
     return resultado


#Solicitar Nome Acoes Americana
def solicitarNomeAtivosBolsaAmericana():
     resultado = baseDadosData.DadosFinanceirosBancoDeDados.obterNomeAcoesAmericana()
     return resultado
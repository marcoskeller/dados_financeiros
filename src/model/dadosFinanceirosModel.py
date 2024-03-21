import src.controller.dadosFinanceirosController as dadosController
from data import dadosBolsaValores as baseDadosData
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import pandas_datareader.data as web
import plotly.graph_objects as go



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

#Plota Grafico Simples da Acao Escolhida
def plotaGraficoSimplesModel(acaoEscolhida, data_inicial, data_final):
    df = baseDadosData.DadosFinanceirosBancoDeDados.obterDadosAcoesGetDataYahoo(acaoEscolhida, data_inicial, data_final)
    med_30 = df.Close.rolling(window=30, min_periods=1).mean()
    candle = {
	    'x':df.index,
	    'open': df.Open,
	    'close': df.Close,
	    'high': df.High,
	    'low': df.Low,
	    'type': 'candlestick',
	    'name': acaoEscolhida,
	    'showlegend': False
    }

    tendencia = {
	    'x': df.index,
	    'y': med_30,
	    'type': 'scatter',
	    'mode': 'lines',
	    'line': {
		    'width': 1,
		    'color':'blue'
	    },
	    'name': 'Média (30 Dias)'
    }

    data = [candle, tendencia]

    layout = go.Layout({
    	'title': {
    		'text': 'Gráfico de Candlestick - '+ acaoEscolhida,
    		'font': {
    			'size': 20		
    		}
    	}
    })
    fig = go.Figure(data=data, layout=layout)
    fig.show()

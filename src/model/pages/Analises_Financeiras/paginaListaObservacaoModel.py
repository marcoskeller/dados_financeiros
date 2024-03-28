import data.dadosBolsaValores as baseDados
import streamlit as st
import datetime as dt
from datetime import date, timedelta
import numpy as np
from streamlit_extras.grid import grid
from streamlit_extras.metric_cards import style_metric_cards
import plotly.express as px
import pandas as pd



#Busca os Ativos da Bolsa
def obter_ativos_bolsaValores_model():
    resultado = baseDados.DadosFinanceirosBancoDeDados.ativosBolsaValores()
    return resultado



#Busca Informacoes dos Ativos Selecionados
def obter_dados_ativos_model(tickers, data_inicial, data_final):
    resultado = baseDados.DadosFinanceirosBancoDeDados.obterDadosAcoesDownloadDataYahooCompleto(tickers, data_inicial, data_final)
    return resultado



#Função Principal onde realiza todo o programa
def exibi_data_frame_model(tickers, data_inicial, data_final):
    #obter DataFrame
    #prices = obter_dados_ativos_model(tickers, data_inicial, data_final)
    
    #Normalizando a coluna data
    #df = prices
   
    #Filtrando a Data
    #df = pd.DataFrame(df)
    #df['Date'] = pd.to_datetime(df.index)
    #df['Date'] = df['Date'].dt.strftime('%d/%m/%Y')

 #Buscando as Informacaoes dos Ativos Selecionandos
    if tickers:
        prices = obter_dados_ativos_model(tickers, data_inicial, data_final)
        if len(tickers) == 1:
            #prices = prices.to_frame()
            prices.columns = [tickers[0].rstrip(".SA")]
        
        prices.columns = prices.columns.str.rstrip(".SA")
        return tickers, prices
   
    #Imprimiendo DataFrame Final
    return st.dataframe(prices, use_container_width=True)



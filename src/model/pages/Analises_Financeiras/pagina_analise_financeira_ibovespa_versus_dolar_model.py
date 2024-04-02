import streamlit as st
import data.dadosBolsaValores as baseDados
import pandas as pd
import seaborn as sns



def obter_dados_ativos_ibovespa_versus_dolar_model(tickers, data_inicial, data_final):
    #Busca dos Dados
    resultado = baseDados.DadosFinanceirosBancoDeDados.obterDadosAcoesYahooIbovespaVersusDolar(tickers, data_inicial, data_final)

    #Normalizando a coluna data
    #df = prices
   
    #Filtrando a Data
    resultado.index = pd.to_datetime(resultado.index)
    resultado.index = resultado.index.strftime('%d/%m/%Y')
    
    #Formatando os Ativos Exibidos
    if tickers:
        if len(tickers) == 1:
            resultado = resultado.to_frame()
            resultado.columns = [tickers[0].rstrip(".SA")]
        
        resultado.columns = resultado.columns.str.rstrip(".SA")
    return resultado


def plotar_grafico_ibovespa_versus_dolar_model(tickers, data_inicial, data_final):
    #Busca dos Dados
    prices = baseDados.DadosFinanceirosBancoDeDados.obterDadosAcoesYahooIbovespaVersusDolar(tickers, data_inicial, data_final)

    #Normalizando a coluna data
    resultado = prices
   
    #Filtrando a Data
    resultado.index = pd.to_datetime(resultado.index)
    resultado.index = resultado.index.strftime('%d/%m/%Y')
    
    #Formatando os Ativos Exibidos
    if tickers:
        if len(tickers) == 1:
            resultado = resultado.to_frame()
            resultado.columns = [tickers[0].rstrip(".SA")]
        
        resultado.columns = resultado.columns.str.rstrip(".SA")
    
    
    
    # sns.set()
    # return resultado.plot(subplots=True, figsize=(22,8))
    retornos = resultado.pct_change()[1:]
    resultado =retornos.describe()
    
    resultado = retornos["DOLAR"].rolling(252).corr(retornos["IBOV"]).plot(figsize=(22,8))

    
    return st.pyplot(sns.pairplot(retornos))


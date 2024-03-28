import streamlit as st
import data.dadosBolsaValores as baseDados
import matplotlib.pyplot as plt
import pandas as pd




#Busca os Ativos da Bolsa
def obter_ativos_bolsaValores_cotacao_tempo_model():
    resultado = baseDados.DadosFinanceirosBancoDeDados.ativosBolsaValores()
    return resultado


#Busca Informacoes dos Ativos Selecionados
def obter_nome_ativos_cotacao_tempo_model(tickers, data_inicial, data_final):
    #Busca dos Dados
    resultado = baseDados.DadosFinanceirosBancoDeDados.obterDadosAcoesYahooCotacaoTempo(tickers, data_inicial, data_final)

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


def plotagem_grafico_obter_dados_ativos_cotacao_tempo_model(tickers, data_inicial, data_final):
    prices = pd.DataFrame()    
    prices = baseDados.DadosFinanceirosBancoDeDados.obterDadosAcoesYahooCotacaoTempo(tickers, data_inicial, data_final)
    plt.figure(figsize=(24,6))
    plt.plot(prices)
    plt.legend(tickers)
    plt.grid()
    plt.title("Cotação x Tempo", fontsize = 20)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(plt.show())


def plotagem_grafico_obter_dados_ativo_ibovespa_cotacao_tempo_model(tickers, data_inicial, data_final):
    tickers = "^BVSP"
    prices = pd.DataFrame()    
    prices = baseDados.DadosFinanceirosBancoDeDados.obterDadosAcoesYahooCotacaoIbovespaTempo(tickers, data_inicial, data_final)
    plt.figure(figsize=(24,6))
    plt.plot(prices)
    plt.legend(tickers)
    plt.grid()
    plt.title("Cotação x tempo - IBOVESPA", fontsize = 20)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(plt.show())

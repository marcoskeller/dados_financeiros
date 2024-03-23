#import src.controller.dadosFinanceirosController as dadosController
from data import dadosBolsaValores as baseDadosData
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import pandas_datareader.data as web
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib as mpl
import mplfinance as mpf
import matplotlib.dates as mpdates
#from mplfinance import candlestick_ohlc
from mplfinance.original_flavor import candlestick_ohlc



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
    resultado = fig.show()
    st.pyplot(resultado)
    



#Plotagem do Grafico com a Biblioteca Matplot
def plotaGraficoSimplesMatPlotModel(acaoEscolhida, data_inicial, data_final):
    #Material Utilizado para fazer as Plotagens dos 'Graficos de 1 ao 12' foi o siste "https://medium.com/@ChrisFaig/matplotlib-para-finan%C3%A7as-d1026cded85b"
    #Grafico 1 - Funcionando
    # df = baseDadosData.DadosFinanceirosBancoDeDados.obterDadosAcoesDownloadDataYahoo(acaoEscolhida, data_inicial, data_final)
    # resultado = mpf.plot(df, type = 'candle', style = 'mike', volume = False, show_nontrading=False)
    # st.set_option('deprecation.showPyplotGlobalUse', False)
    # st.pyplot(resultado)
    

    #Grafico 2 - Funcionando
    # df = baseDadosData.DadosFinanceirosBancoDeDados.obterDadosAcoesGetDataYahoo(acaoEscolhida, data_inicial, data_final)
    # resultado = mpf.plot(df[-90:], type='candle', style='charles',
    #      title= 'Media de 3/6/9 Dias - ' + acaoEscolhida,
    #      ylabel='Preço ($)',
    #      ylabel_lower='Volume',
    #      volume=True, 
    #      mav=(3,6,9))
    # st.set_option('deprecation.showPyplotGlobalUse', False)
    # st.pyplot(resultado)


    #Grafico 3 - Funcionando
    # df = baseDadosData.DadosFinanceirosBancoDeDados.obterDadosAcoesGetDataYahoo(acaoEscolhida, data_inicial, data_final)
    # data_rolling = df['Close'].rolling(window=30).mean()
    # plt.figure(figsize=(14,7))
    # plt.fill_between(data_rolling.index, data_rolling, color="skyblue", alpha=0.4)
    # plt.plot(data_rolling, color="blue", alpha=0.8)
    # plt.title('Média Móvel de 30 dias da - '+ acaoEscolhida, fontsize=20)
    # plt.xlabel('Data', fontsize=16)
    # plt.ylabel('Preço de Fechamento (R$)', fontsize=16)
    # plt.grid(True)
    # resultado = plt.show()
    # st.set_option('deprecation.showPyplotGlobalUse', False)
    # st.pyplot(resultado)
     

    #Grafico 4 - Funcionando (Personalizando Eixos e Marcadores)
    # df = baseDadosData.DadosFinanceirosBancoDeDados.obterDadosAcoesGetDataYahoo(acaoEscolhida, data_inicial, data_final)
    # fig, ax = plt.subplots(figsize=(14,7))
    # ax.plot(df['Close'], marker='o', linestyle='-', linewidth=2, markersize=8, color='blue')
    # ax.set_xlabel('Data', fontsize=16)
    # ax.set_ylabel('Preço de Fechamento (R$)', fontsize=16)
    # ax.set_title('Preço de Fechamento da - '+ acaoEscolhida, fontsize=20)

    # ax.xaxis.set_major_locator(plt.MaxNLocator(10)) # Reduz o número de marcas no eixo X
    # plt.xticks(rotation=45) # Rotaciona as marcas do eixo X

    # plt.grid(True)
    # resultado = plt.show()
    # st.set_option('deprecation.showPyplotGlobalUse', False)
    # st.pyplot(resultado)


    #Grafico 5 - Funcionando (Estilo GGPLOT)
    # df = baseDadosData.DadosFinanceirosBancoDeDados.obterDadosAcoesGetDataYahoo(acaoEscolhida, data_inicial, data_final)
    # plt.style.use('ggplot')
    # df['Close'].plot(figsize=(10,5))
    # plt.title('Preço de Fechamento da - '+ acaoEscolhida, fontsize=20)
    # plt.xlabel('Data', fontsize=16)
    # plt.ylabel('Preço de Fechamento ($)', fontsize=16)
    # plt.grid(True)
    # resultado = plt.show()
    # st.set_option('deprecation.showPyplotGlobalUse', False)
    # st.pyplot(resultado)


    #Grafico 6 - Funcionando (Múltiplos eixos)
    # df = baseDadosData.DadosFinanceirosBancoDeDados.obterDadosAcoesGetDataYahoo(acaoEscolhida, data_inicial, data_final)
    # fig, ax1 = plt.subplots()

    # color = 'tab:red'
    # ax1.set_xlabel('Data')
    # ax1.set_ylabel('Preço de Fechamento (R$)', color=color)
    # ax1.plot(df.index, df['Close'], color=color)
    # ax1.tick_params(axis='y', labelcolor=color)

    # ax2 = ax1.twinx()
    # color = 'tab:blue'
    # ax2.set_ylabel('Volume', color=color)
    # ax2.plot(df.index, df['Volume'], color=color)
    # ax2.tick_params(axis='y', labelcolor=color)

    # plt.title('Preço de Fechamento e Volume da - ' + acaoEscolhida, fontsize=15)
    # fig.tight_layout()
    # resultado = plt.show()
    # st.set_option('deprecation.showPyplotGlobalUse', False)
    # st.pyplot(resultado)
     

    #Grafico 7 - Funcionando (Gráficos Subplot)
    # df = baseDadosData.DadosFinanceirosBancoDeDados.obterDadosAcoesGetDataYahoo(acaoEscolhida, data_inicial, data_final)
    # fig, axs = plt.subplots(2)
    # fig.suptitle('Preço de Fechamento e Volume Negociado', fontsize=12)

    # axs[0].plot(df['Close'], color='blue')
    # axs[0].set(ylabel='Preço de Fechamento ($)')

    # axs[1].bar(df.index, df['Volume'], color='grey')
    # axs[1].set(xlabel='Data', ylabel='Volume')
    # resultado = plt.show()
    # st.set_option('deprecation.showPyplotGlobalUse', False)
    # st.pyplot(resultado)
     
    
    #Grafico 8 - Funcionando (Diagrama de caixa (boxplot))
    # data_msft = baseDadosData.DadosFinanceirosBancoDeDados.obterDadosAcoesGetDataYahoo(acaoEscolhida, data_inicial, data_final)
    # df = baseDadosData.DadosFinanceirosBancoDeDados.obterDadosAcoesGetDataYahoo('MSFT', data_inicial, data_final)
    # returns_msft = data_msft['Close'].pct_change().dropna()
    # returns_aapl = df['Close'].pct_change().dropna()
    # plt.figure(figsize=(14,7))
    # plt.boxplot([returns_msft, returns_aapl], labels=["MSFT", acaoEscolhida])
    # plt.title('Boxplot de Retornos da AAPL vs MSFT', fontsize=15)
    # plt.ylabel('Retornos', fontsize=15)
    # plt.grid(True)
    # resultado = plt.show()
    # st.set_option('deprecation.showPyplotGlobalUse', False)
    # st.pyplot(resultado)
    
    
    #Grafico 9 - Funcionando (Gráfico de dispersão)
    # data_msft = baseDadosData.DadosFinanceirosBancoDeDados.obterDadosAcoesGetDataYahoo('MSFT', data_inicial, data_final)
    # df = baseDadosData.DadosFinanceirosBancoDeDados.obterDadosAcoesGetDataYahoo(acaoEscolhida, data_inicial, data_final)
    # returns_msft = data_msft['Close'].pct_change().dropna()
    # returns_aapl = df['Close'].pct_change().dropna()
    # plt.figure(figsize=(14,7))
    # plt.scatter(returns_msft, returns_aapl, alpha=0.5)
    # plt.title('Scatter Plot de Retornos AAPL vs MSFT', fontsize=20)
    # plt.xlabel('Retornos MSFT', fontsize=16)
    # plt.ylabel('Retornos AAPL', fontsize=16)
    # plt.grid(True)
    # resultado = plt.show()
    # st.set_option('deprecation.showPyplotGlobalUse', False)
    # st.pyplot(resultado)
    

    #Grafico 10 - Funcionando (Histograma)
    # df = baseDadosData.DadosFinanceirosBancoDeDados.obterDadosAcoesGetDataYahoo(acaoEscolhida, data_inicial, data_final)
    # returns = df['Close'].pct_change().dropna()
    # plt.figure(figsize=(14,7))
    # plt.hist(returns, bins=50, color='blue', alpha=0.7)
    # plt.title('Histograma de Retornos da - ' + acaoEscolhida, fontsize=20)
    # plt.xlabel('Retorno', fontsize=16)
    # plt.ylabel('Frequência', fontsize=16)
    # plt.grid(True)
    # resultado = plt.show()
    # st.set_option('deprecation.showPyplotGlobalUse', False)
    # st.pyplot(resultado)
     

    #Grafico 11 - Funcionando (Gráfico de barras)
    # df = baseDadosData.DadosFinanceirosBancoDeDados.obterDadosAcoesGetDataYahoo(acaoEscolhida, data_inicial, data_final)
    # plt.figure(figsize=(14,7))
    # plt.bar(df.index, df['Volume'], color='grey')
    # plt.title('Volume Negociado da - ' + acaoEscolhida, fontsize=15)
    # plt.xlabel('Data', fontsize=16)
    # plt.ylabel('Volume', fontsize=16)
    # plt.grid(True)
    # resultado = plt.show()
    # st.set_option('deprecation.showPyplotGlobalUse', False)
    # st.pyplot(resultado)
     

    #Grafico 12 - Funcionando (Gráfico Preço de Fechamento)
    # df = baseDadosData.DadosFinanceirosBancoDeDados.obterDadosAcoesGetDataYahoo(acaoEscolhida, data_inicial, data_final)
    # plt.figure(figsize=(14,7))
    # plt.plot(df['Close'], color='green')
    # plt.title('Preço de fechamento da - ' + acaoEscolhida, fontsize=20)
    # plt.xlabel('Data', fontsize=16)
    # plt.ylabel('Preço de Fechamento (R$)', fontsize=15)
    # plt.grid(True)
    # resultado = plt.show()
    # st.set_option('deprecation.showPyplotGlobalUse', False)
    # st.pyplot(resultado)


    #Grafico 13 - Funcionando (Gráfico de Linha)
    df = baseDadosData.DadosFinanceirosBancoDeDados.obterDadosAcoesGetDataYahoo(acaoEscolhida, data_inicial, data_final)
    plt.figure(figsize=(14,7))
    plt.plot(df['Close'])
    plt.title('Preço de fechamento da - ' + acaoEscolhida)
    plt.xlabel('Data')
    plt.ylabel('Preço de Fechamento (R$)')
    plt.grid(False)
    resultado = plt.show()
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(resultado)
    
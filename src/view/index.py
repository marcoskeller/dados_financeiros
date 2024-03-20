import streamlit as st
import pandas as pd
import datetime as dt
import plotly.graph_objs as go
import investpy as ip
from investiny import historical_data, search_assets

import yfinance as yf
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import pandas_datareader.data as web


paises = ['','Brasil', 'Estados Unidos da América']
intervalo = ['Daily', 'Weekly', 'Monthly']
acoes_yFinace = ['','EMBR3.SA','CTIP3.SA','ENBR3.SA','CESP6.SA','CSAN3.SA','BRFS3.SA','CCRO3.SA','ESTC3.SA','BRAP4.SA','BBDC4.SA','BBDC3.SA','ECOR3.SA','CSNA3.SA',
'CPLE6.SA','EQTL3.SA','CMIG4.SA','CYRE3.SA','CPFE3.SA','BVMF3.SA','656690','CIEL3.SA','BRML3.SA','GGBR4.SA','BRKM5.SA','BBAS3.SA','ABEV3.SA','BRPR3.SA',
'BBSE3.SA','FIBR3.SA','ELET3.SA']

#Definicao das Datas
data_inicial = dt.datetime.now() + dt.timedelta(days=-30)
data_final = dt.datetime.today()

#@st.cache
# def consultar_acoes(acao, pais,inicio_data, fim_data, intervalo):
# 	df = ip.get_stock_historical_data(stock=acao, country=pais,from_date=inicio_data, to_date=fim_data, interval=intervalo)
# 	return df

# def consultar_acoes(acao, pais,inicio_data, fim_data, intervalo):
# 	df = ip.get_stock_historical_data(stock=acao, country=pais,from_date=inicio_data, to_date=fim_data, interval=intervalo)
# 	return df

#data = historical_data(investing_id=6408, from_date="09/01/2022", to_date="10/01/2022")

#df = consultar_acoes('ENGI4','Brazil','17/03/2024','18/03/2024','Daily')
#st.dataframe(data)

def format_date(dt, format='%d/%m/%Y'):
	return dt.strftime(format)



def exibiGraficoCandle(df):
    fig = go.Figure(data=[go.Candlestick(
                x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

    fig.show()

def exibiGraficoCandleSemRodape(df, acao):
    fig = go.Figure(
        data=[go.Candlestick(
            x=df.index,
            open=df['Open'], 
            high=df['High'],
            low=df['Low'], 
            close=df['Close'],
            increasing_line_color= 'green', decreasing_line_color= 'red')
        ])

    fig.update_layout(
    title='Análise Gráfica Simples',
    yaxis_title=acao
)
    fig.update_layout(xaxis_rangeslider_visible=False)
    fig.show()


def inicio_view():
    try:                   

        selecionando_pais = st.sidebar.selectbox("Selecione o País: ", paises)

        if selecionando_pais == 'Brasil':
             
            #Selecao do Periodo Desejado
            inicio_data = st.sidebar.date_input('De: ', data_inicial)
            fim_data = st.sidebar.date_input('Até: ', data_final)

            if inicio_data > fim_data:
                st.sidebar.error('Data de ínicio maior que data final')
            else:
                #Mostrar ou Ocultar os Dados
                if not inicio_data == '' or fim_data == '':
                    
                    #Selecao do Ativo Desejado
                    selecionando_acao = st.sidebar.selectbox("Selecione o Ativo Desejado: ", acoes_yFinace)
                    
                    try:
                        if selecionando_acao == '':
                            st.write('Você não preencheu os campos necessários!')
                        else:
                            
                            #Condicao para exibir os dados
                            carregadar_dados = st.sidebar.checkbox('Carregar Dados')
                            
                            if carregadar_dados:
                                #Elementos Centrais da Pagina
                                st.title('Monitor do Mercado de Ações')
                                
                                #Ramo de Investimento
                                st.header('Ação')
                                #Qual ação foi escolhida
                                st.write(selecionando_acao)
                                
                                #Titulo do Menu
                                st.subheader('Dados')
                                
                                #Definindo o ticker da ação desejada
                                #ticker = selecionando_acao

                                # Obtendo os dados da ação
                                df = yf.download(selecionando_acao, start=inicio_data, end=fim_data, progress=False)
                                
                                
                                #ticker = yf.Ticker('^BVSP')
                                #df = ticker.history(interval='1d',start=inicio_data, end=fim_data)

                                #Exibindo os Graficos
                                #grafico_candle = st.empty()
                                #grafico_line = st.empty()

                                # Exibindo as informações obtidas
                                st.dataframe(df, use_container_width=True)
                                #decomposicao = seasonal_decompose(df[['Close']], model='additive', period=30, extrapolate_trend=30)
                                #decomposicao
                    

                                yf.pdr_override()
                                ibov = web.get_data_yahoo('^BVSP')
                                st.dataframe(ibov, use_container_width=True)

                                google = web.get_data_yahoo('GOOG')
                                
                                
                    
                                #Funcionando
                                exibiGraficoCandleSemRodape(google,'GOOGLE ($)')
                                exibiGraficoCandleSemRodape(df,selecionando_acao)
                                exibiGraficoCandleSemRodape(ibov, 'AÇÕES (R$)')
                                
                                
                    except Exception as e:
                        st.error(e)    
                else:
                    st.write('Você não preencheu os campos necessários!')
        #Escolhendo Outro Pais
        elif selecionando_pais == 'Estados Unidos da América':

            #Selecao do Periodo Desejado
            inicio_data = st.sidebar.date_input('De: ', data_inicial)
            fim_data = st.sidebar.date_input('Até: ', data_final)
             
            if inicio_data > fim_data:
                st.sidebar.error('Data de ínicio maior que data final')
            else:

                #Selecao do Ativo Desejado
                acoes = ip.get_stocks_list(country='united states')
                selecionando_acao = st.sidebar.selectbox("Selecione o Ativo Desejado: ", acoes, None)

                #Mostrar ou Ocultar os Dados
                if not inicio_data == '' or fim_data == '':
                    
                    try:
                        if selecionando_acao == None:
                            st.write('Você não preencheu os campos necessários!')
                        else:
                            carregadar_dados = st.sidebar.checkbox('Carregar Dados')
                            if carregadar_dados:
                                #Elementos Centrais da Pagina
                                st.title('Monitor do Mercado de Ações Internacionais')
                                
                                #Ramo de Investimento
                                st.header('Ação')
                                #Qual ação foi escolhida
                                st.write(selecionando_acao)
                                
                                #Titulo do Menu
                                st.subheader('Dados')
                                
                                #Definindo o ticker da ação desejada
                                ticker = selecionando_acao

                                # Obtendo os dados da ação
                                data= yf.download(ticker, start=inicio_data, end=fim_data, progress=False)

                                #Exibindo os Graficos
                                grafico_candle = st.empty()
                                grafico_line = st.empty()
                                
                                # Exibindo as informações obtidas
                                st.dataframe(data, use_container_width=True)
                    except Exception as e:
                        st.error(e)
                    
                else:
                    st.write('Você não preencheu as datas!')
        else:
             print()
    except Exception as e:
        st.error(e)
        print(e)




def pagina_View():
    inicio_view()
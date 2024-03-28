import data.dadosBolsaValores as baseDados
import streamlit as st
import datetime as dt
from datetime import date, timedelta
import numpy as np
from streamlit_extras.grid import grid
from streamlit_extras.metric_cards import style_metric_cards
import plotly.express as px
import pandas as pd
from streamlit_option_menu import option_menu



#Formatando as Datas
def format_date_model(dt, format='%d/%m/%Y'):
	return dt.strftime(format)


#Busca os Ativos da Bolsa
def obter_ativos_bolsaValores_model():
    resultado = baseDados.DadosFinanceirosBancoDeDados.ativosBolsaValores()
    return resultado


#Busca Informacoes dos Ativos Selecionados
def obter_dados_ativos_model(tickers, data_inicial, data_final):
    resultado = baseDados.DadosFinanceirosBancoDeDados.obterDadosAcoesDownloadDataYahoo(tickers, data_inicial, data_final)
    return resultado


#Função Principal onde realiza todo o programa
def analise_financeira_principal(tickers, prices):
    #Definindo um peso para os elementos do Array
    weights = np.ones(len(tickers))/len(tickers)
    #Criando um nova coluna com os pesos
    prices['PORTFOLIO'] = prices.drop("IBOV", axis=1) @ weights
    #Criando a Parte Financeira
    norm_prices = (100 * prices) / prices.iloc[0]
    retornos = prices.pct_change()[1:]
    vols = retornos.std() * (np.sqrt(252))
    rets = (norm_prices.iloc[-1] - 100) /100
    
    
    #Definição da Estrutura dos Elementos
    mygrid =  grid(5, 5, 5, 5, 5, 5, vertical_align="top")
        
    for t in prices.columns:
        c = mygrid.container(border=True)
        c.subheader(t, divider="red")
        colA, colB, colC = c.columns(3)
        if t == 'PORTFOLIO':
            colA.image("images\pie-chart-dollar-svgrepo-com.svg")
        elif t == "IBOV":
            colA.image("images/pie-chart-svgrepo-com.svg")
        else:
            colA.image(f'https://raw.githubusercontent.com/thefintz/icones-b3/main/icones/{t}.png', width=85)
        colB.metric(label="retorno", value=f"{rets[t]:.0%}")
        colC.metric(label="volatilidade", value=f"{vols[t]:.0%}")
        style_metric_cards(background_color='rgba(255,255,255,0')
    
    
    #Normalizando a coluna data
    df = prices
   
    #Filtrando a Data
    df = pd.DataFrame(df)
    df['Date'] = pd.to_datetime(df.index)
    df['Date'] = df['Date'].dt.strftime('%d/%m/%Y')
    

    #Imprimiendo DataFrame Final
    st.dataframe(df, use_container_width=True, hide_index=True) 
    
    #Contruindo os Graficos
    col1, col2 = st.columns(2, gap='large')
    with col1:
        st.subheader("Desempenho Relativo")
        st.line_chart(norm_prices, height=600)
    with col2:
        st.subheader("Risco Retorno")
        fig = px.scatter(
            x=vols,
            y=rets,
            text=vols.index,
            color=rets/vols,
            color_continuous_scale=px.colors.sequential.Bluered_r
        )
        fig.update_traces(
			textfont_color='white',
			marker=dict(size=45),
			textfont_size=10,
		)
        fig.layout.yaxis.title = 'Retorno Total'
        fig.layout.xaxis.title = 'Volatilidade (anualizada)'
        fig.layout.height = 600
        fig.layout.xaxis.tickformat = ".0%"
        fig.layout.yaxis.tickformat = ".0%"        
        fig.layout.coloraxis.colorbar.title = 'Sharpe'
        st.plotly_chart(fig, use_container_width=True)
            

#Funçao que monta o grid os dados
def pagina_sidebar_model():
    st.sidebar.image("./images/bolsa_valores_sidebar.png")
    
    #ticker_list = st.sidebar.selectbox('Selecione o Ativo Desejado', pagina_analise_financeira_controller.FinanceiroAnaliseFinanceiraController.obterAtivosFinanceiros(), None)
    
    #Buscando os Nome das Ações
    ticker_list = obter_ativos_bolsaValores_model()
    tickers = st.sidebar.multiselect(label="Selecione as Empresas", options=ticker_list, placeholder="Ações")
    
    #Adcionando o Sufixo SA para usarmos a API do yahoo
    tickers = [t+".SA" for t in tickers]
    
    #Selecionando as Datas
    #Adcionando mais dias na data atual
    td = timedelta(-7)
    data_inicial = st.sidebar.date_input("De", format="DD/MM/YYYY", value=date.today() + td)
    
    data_final = st.sidebar.date_input("Até", format="DD/MM/YYYY",value=dt.datetime.now())
    #Buscando as Informacaoes dos Ativos Selecionandos
    if tickers:
        prices = obter_dados_ativos_model(tickers, data_inicial, data_final)
        if len(tickers) == 1:
            prices = prices.to_frame()
            prices.columns = [tickers[0].rstrip(".SA")]
        
        prices.columns = prices.columns.str.rstrip(".SA")
        prices['IBOV'] = obter_dados_ativos_model("^BVSP", data_inicial, data_final)
        return tickers, prices
    return None,None

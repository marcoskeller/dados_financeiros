import streamlit as st
import data.dadosBolsaValores as baseDados
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns




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


def plotagem_grafico_media_geral_model(total_dias, dias, tickers, data_inicial, data_final):
    
    prices = baseDados.DadosFinanceirosBancoDeDados.obterDadosAcoesYahooMediaGeral(tickers, data_inicial, data_final)
    # prices = pd.DataFrame()
    # st.dataframe(prices)
    # glue = sns.load_dataset("glue").pivot(index="Model", columns="Task", values="Score")
    # sns.heatmap(glue, vmin=50, vmax=100)
    # #sns.heatmap(prices, vmin=50, vmax=100)
    # st.pyplot(plt.show())
    st.markdown('Em construção!')
    #resultado = st.dataframe(prices.head(), use_container_width=True)
    #resultado = st.dataframe(prices.tail(), use_container_width=True)
    prices["Close"].plot(figsize=(22,8), label=tickers[0])
    prices["Close"].rolling(dias).mean().plot(label="Média Móvel de "+ str(dias) + " dias")
    prices["Close"].rolling(total_dias).mean().plot(label="Média Móvel Período Total "+ str(total_dias) + " dias")
    plt.legend()
    return st.pyplot(plt.show())
    #return prices


def plotagem_grafico_retorno_diario_model(tickers, data_inicial, data_final):

    if len(tickers) > 1:
        prices = baseDados.DadosFinanceirosBancoDeDados.obterDadosAcoesYahooCotacaoTempo(tickers, data_inicial, data_final)
        descritivo = prices.describe()
        #st.dataframe(prices)
        #st.write(tickers)
        #st.dataframe(descritivo)

        sns.pairplot(descritivo)
        plt.show()
        st.pyplot(plt.show())    
    else:
        st.write('Voce Precisa selecionar mais um ativo para exibir o gráfico de Retorno Diário')
    
    
def  plotagem_grafico_distribuicao_diario_ibovespa_model(tickers, data_inicial, data_final):
    tickers = "^BVSP"
    prices = pd.DataFrame()    
    prices = baseDados.DadosFinanceirosBancoDeDados.obterDadosAcoesYahooCotacaoIbovespaTempo(tickers, data_inicial, data_final)
    descritivo = prices.describe()
    sns.distplot(descritivo.dropna())
    st.pyplot(plt.show())

    
def plotagem_grafico_retorno_acumulado_model(tickers, data_inicial, data_final):
    st.write('Em Construção...')

    


    
 


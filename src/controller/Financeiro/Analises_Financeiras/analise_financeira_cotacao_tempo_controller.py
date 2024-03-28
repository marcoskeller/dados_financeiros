import streamlit as st
import src.model.pages.Analises_Financeiras.analise_financeira_cotacao_tempo_model as analise_financeira_cotacao_tempo_model



try:
    #Busca os Dados das Acoes Selecionadas
    def pagina_analise_financeira_cotacao_tempo_obter_dados_ativos_controller(tickers, data_inicial, data_final):
        opcao = analise_financeira_cotacao_tempo_model.obter_nome_ativos_cotacao_tempo_model(tickers, data_inicial, data_final)
        return opcao
    

    #Busca os Nomes dos Ativos na Classe Model
    def obter_ativos_bolsaValores_controller():
        resultado = analise_financeira_cotacao_tempo_model.obter_ativos_bolsaValores_cotacao_tempo_model()
        return resultado


    #Plota o Graficos das Acoes Selecionadas
    def plotagem_grafico_obter_dados_ativos_cotacao_tempo_controller(tickers, data_inicial, data_final):
        resultado = analise_financeira_cotacao_tempo_model.plotagem_grafico_obter_dados_ativos_cotacao_tempo_model(tickers, data_inicial, data_final)
        return resultado


    #Plota o Grafico Somente do Ibovespa
    def pagina_analise_financeira_cotacao_tempo_obter_dados_ativo_ibovespa_controller(tickers, data_inicial, data_final):
        resultado = analise_financeira_cotacao_tempo_model.plotagem_grafico_obter_dados_ativo_ibovespa_cotacao_tempo_model(tickers, data_inicial, data_final)
        return resultado
    
except Exception as error:
    print(error)
    #Apagar essa linha quando subir para PRD
    st.write(error + st.write('Erro na Chamada da Funcao'))
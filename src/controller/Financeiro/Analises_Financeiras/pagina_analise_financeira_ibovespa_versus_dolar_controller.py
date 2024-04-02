import streamlit as st
import src.model.pages.Analises_Financeiras.pagina_analise_financeira_ibovespa_versus_dolar_model as analise_financeira_ibovespa_versus_dolar_model


try:
    #Busca os Dados das Acoes Selecionadas
    def pagina_analise_financeira_ibovespa_versus_dolar_obter_dados_ativos_controller(tickers, data_inicial, data_final):
        opcao = analise_financeira_ibovespa_versus_dolar_model.obter_dados_ativos_ibovespa_versus_dolar_model(tickers, data_inicial, data_final)
        return opcao

    #Busca os Dados das Acoes Selecionadas
    def pagina_plotar_grafico_ibovespa_versus_dolar_controller(tickers, data_inicial, data_final):
        opcao = analise_financeira_ibovespa_versus_dolar_model.plotar_grafico_ibovespa_versus_dolar_model(tickers, data_inicial, data_final)
        return opcao

except Exception as error:
    print(error)
    #Apagar essa linha quando subir para PRD
    st.write(error + st.write('Erro na Chamada da Funcao'))
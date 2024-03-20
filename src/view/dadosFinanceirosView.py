import streamlit as st
import datetime as dt
import src.controller.dadosFinanceirosController as dadosController





def inicio_view():
    
    #Selecao do Pais
    selecionando_pais = st.sidebar.selectbox("Selecione o País: ", dadosController.DadosFinanceirosController.selecionaPais())
    
    #Selecao do Ativo Desejado
    selecionando_acao = st.sidebar.selectbox("Selecione o Ativo Desejado: ", dadosController.DadosFinanceirosController.acoesBrasileirasYahooFinance())
    
    #Selecao do Intervalo
    #selecionando_intervalo = st.sidebar.selectbox("Selecione o Intervalo Desejado: ", dadosController.selecionaIntervalo())

    #Definicao das Datas
    data_inicial = dt.datetime.now() + dt.timedelta(days=-30)
    data_final = dt.datetime.today()
    
    #Selecao das Datas
    inicio_data = st.sidebar.date_input('De: ', data_inicial)
    fim_data = st.sidebar.date_input('Até: ', data_final)
    
    
    
import streamlit as st
import datetime as dt
from datetime import date, timedelta
import src.controller.Financeiro.Analises_Financeiras.pagina_analise_financeira_ibovespa_versus_dolar_controller as analise_financeira_ibovespa_versus_dolar_controller



try:
        
    def pagina_analise_financeira_ibovespa_versus_dolar_view():
                
        #Selecionando as Datas
        #Adcionando mais dias na data atual
        td = timedelta(-7)
        data_inicial = st.sidebar.date_input("De", format="DD/MM/YYYY", value=date.today() + td)
        
        data_final = st.sidebar.date_input("Até", format="DD/MM/YYYY",value=dt.datetime.now())
        
        #Buscando os Nome das Ações
        tickers = "^BVSP USDBRL=X"
        mostrarDataframe = st.sidebar.checkbox('Tabela')
        plotar_grafico_ibovespa_dolar =st.sidebar.checkbox('Plotar Gráfico Ibovespa X Dólar')

        if mostrarDataframe:
            df = analise_financeira_ibovespa_versus_dolar_controller.pagina_analise_financeira_ibovespa_versus_dolar_obter_dados_ativos_controller(tickers, data_inicial, data_final)
            st.dataframe(df, use_container_width=True)
        

        if plotar_grafico_ibovespa_dolar:
            df = analise_financeira_ibovespa_versus_dolar_controller.pagina_plotar_grafico_ibovespa_versus_dolar_controller(tickers, data_inicial, data_final)
           

except Exception as error:
    print(error)
    #Apagar essa linha quando subir para PRD
    st.write(error + st.write('Erro na Chamada da Funcao'))
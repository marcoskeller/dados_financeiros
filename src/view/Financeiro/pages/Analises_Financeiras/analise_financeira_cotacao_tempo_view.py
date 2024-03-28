import streamlit as st
import datetime as dt
from datetime import date, timedelta
import src.controller.Financeiro.Analises_Financeiras.analise_financeira_cotacao_tempo_controller as analise_financeira_cotacao_tempo_controller


try:   
    def pagina_analise_financeira_cotacao_tempo_view():
             
        #Selecionando as Datas
        #Adcionando mais dias na data atual
        td = timedelta(-7)
        data_inicial = st.sidebar.date_input("De", format="DD/MM/YYYY", value=date.today() + td)
        
        data_final = st.sidebar.date_input("Até", format="DD/MM/YYYY",value=dt.datetime.now())
        
        #Buscando os Nome das Ações
        ticker_list = analise_financeira_cotacao_tempo_controller.obter_ativos_bolsaValores_controller()
        tickers = st.sidebar.multiselect(label="Selecione as Ações", options=ticker_list, placeholder="Ações")

        
        
        #Buscando as Informacoes dos Ativos
        if tickers:

            df2 = analise_financeira_cotacao_tempo_controller.plotagem_grafico_obter_dados_ativos_cotacao_tempo_controller(tickers, data_inicial, data_final)
            
            mostrarDataframe = st.sidebar.checkbox('Exibir Tabela')
            grafico_comparaco_ibovespa = st.sidebar.checkbox('Exibir Gráfico IBOVESPA')
            
            if mostrarDataframe:
                df = analise_financeira_cotacao_tempo_controller.pagina_analise_financeira_cotacao_tempo_obter_dados_ativos_controller(tickers, data_inicial, data_final)
                st.dataframe(df, use_container_width=True)

            if grafico_comparaco_ibovespa:
                grafico_ibovespa = analise_financeira_cotacao_tempo_controller.pagina_analise_financeira_cotacao_tempo_obter_dados_ativo_ibovespa_controller(tickers, data_inicial, data_final)
      
        else:
            pass
    
except Exception as error:
    print(error)
    #Apagar essa linha quando subir para PRD
    st.write(error + st.write('Erro na Chamada da Funcao'))
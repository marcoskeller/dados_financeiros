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
   
            exibirDetalhePorAcao = st.sidebar.checkbox('Detalhe Por Ação')
            exibirCotacaoTempo = st.sidebar.checkbox('Cotação X Tempo')
            mostrarDataframe = st.sidebar.checkbox('Tabela')
            grafico_comparaco_ibovespa = st.sidebar.checkbox('Gráfico IBOVESPA')
            media_geral = st.sidebar.checkbox('Médias Móveis, Trimestrais e Anuais')
            retorno_diario = st.sidebar.checkbox('Retorno Diário')
            distribuicao_ibovespa = st.sidebar.checkbox('Distribuição Ibovespa')
            retorno_acumulado = st.sidebar.checkbox('Retorno Acumulado')
            
            
            if exibirDetalhePorAcao:
                df = analise_financeira_cotacao_tempo_controller.pagina_analise_financeira_cotacao_tempo_obter_dados_ativos_controller(tickers, data_inicial, data_final)
                with st.expander("Detalhes da Ação"):
                    showData=st.multiselect('Filtros: ',df.columns,default=[])
                    st.dataframe(df[showData],  use_container_width=True)          


            if exibirCotacaoTempo:
                 df2 = analise_financeira_cotacao_tempo_controller.plotagem_grafico_obter_dados_ativos_cotacao_tempo_controller(tickers, data_inicial, data_final)

   
            if mostrarDataframe:
                df = analise_financeira_cotacao_tempo_controller.pagina_analise_financeira_cotacao_tempo_obter_dados_ativos_controller(tickers, data_inicial, data_final)
                st.dataframe(df, use_container_width=True)


            if grafico_comparaco_ibovespa:
                grafico_ibovespa = analise_financeira_cotacao_tempo_controller.pagina_analise_financeira_cotacao_tempo_obter_dados_ativo_ibovespa_controller(tickers, data_inicial, data_final)


            if media_geral:

                diferenca = data_final - data_inicial
                total_dias = diferenca.days
       
                dias = st.selectbox('Informe quantidade de dias para cáclculo da Média Móvel - Período 1', options=range(0,total_dias))
                total_dias = st.selectbox('Informe quantidade de dias para cáclculo da Média Móvel Príodo 2', options=range(0,total_dias))
                media_movel_anual_trimestral_ = analise_financeira_cotacao_tempo_controller.plotagem_grafico_media_geral_controller(total_dias, dias, tickers, data_inicial, data_final)


            if retorno_diario:
                media_movel_anual_trimestral_ = analise_financeira_cotacao_tempo_controller.plotagem_grafico_retorno_diario_controller(tickers, data_inicial, data_final)
            
            if distribuicao_ibovespa:
                media_movel_anual_trimestral_ = analise_financeira_cotacao_tempo_controller.plotagem_grafico_distribuicao_diario_ibovespa_controller(tickers, data_inicial, data_final)
            

            if retorno_acumulado:
                media_movel_anual_trimestral_ = analise_financeira_cotacao_tempo_controller.plotagem_grafico_retorno_acumulado_controller(tickers, data_inicial, data_final)
            

        else:
            pass
    
except Exception as error:
    print(error)
    #Apagar essa linha quando subir para PRD
    st.write(error + st.write('Erro na Chamada da Funcao'))
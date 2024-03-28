import streamlit as st
import src.view.Financeiro.pages.Analises_Financeiras.paginaListaObservacaoView as pagina_lista_observacao_view
import src.model.pages.Analises_Financeiras.paginaListaObservacaoModel as pagina_lista_observacao_model
import pandas as pd




class FinanceiroListaObservacaoController():
    try:
        #Funcao que chama a pagina inicial View
        def inicio_pagina_calendario_controller():
            opcao = pagina_lista_observacao_view.pagina_lista_observacao_view()

        #Busca os Nomes dos Ativos na Classe Model
        def obter_ativos_bolsaValores_controller():
            resultado = pagina_lista_observacao_model.obter_ativos_bolsaValores_model()
            return resultado
        
        #Busca os Nomes dos Ativos na Classe Model
        def obter_dados_ativos_controller(tickers, data_inicial, data_final):
            #Adcionando o Sufixo SA para usarmos a API do yahoo
            #tickers = [t+".SA" for t in tickers]
            resultado = pagina_lista_observacao_model.obter_dados_ativos_model(tickers, data_inicial, data_final)
            return resultado
        
            
        #Exibi o DataFrame
        def exibiDataFrame(tickers, data_inicial, data_final):
            resultado = pagina_lista_observacao_model.exibi_data_frame_model(tickers, data_inicial, data_final)
            #Buscando as Informacaoes dos Ativos Selecionandos
            # if tickers:
            #     tabelaAcoes = FinanceiroListaObservacaoController.obter_dados_ativos_controller(tickers, data_inicial, data_final)
            
            #     if len(tickers) == 1:
            #         #tabelaAcoes = pd.DataFrame()
            #         #tabelaAcoes = tabelaAcoes.to_frame()
            #         #tabelaAcoes.columns = [tickers[0].rstrip(".SA")]
            #         #Imprimi o DataFrame
            #         resultado = st.dataframe(tabelaAcoes, use_container_width=True)
            #         return resultado
            #     else:
            #         print()
            # else:
            #     print()
            #return resultado

        
    except Exception as error:
        print(error)
        #Apagar essa linha quando subir para PRD
        st.write(error)
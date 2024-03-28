import streamlit as st
import src.view.Financeiro.pages.Mercado.paginaAnaliseFinanceiraView as pagina_analise_financeira_view
import src.model.pages.Mercado.paginaAnaliseFinanceiraModel as pagina_analise_financeira_model




class FinanceiroAnaliseFinanceiraController():
    try:
        #Funcao que chama a pagina inicial View
        def inicio_pagina_analise_financeira_controller():
            opcao = pagina_analise_financeira_view.pagina_analise_financeira_view()

        #Funco Formata Data
        def formata_data_controller(dataInformada):
            resultado = pagina_analise_financeira_model.format_date_model(dataInformada)
            return resultado

        #Funcao Inicializa Pagina Sidebar
        def pagina_sidebar_controller():
            resultado = pagina_analise_financeira_model.pagina_sidebar_model()
            return resultado

        #Funcao Inicializa Pagina Sidebar
        def pagina_resultado_analise_financeira__controller(tickers, prices):
            resultado = pagina_analise_financeira_model.analise_financeira_principal(tickers, prices)
            return resultado

    except Exception as error:
        print(error)
        #Apagar essa linha quando subir para PRD
        st.write(error)
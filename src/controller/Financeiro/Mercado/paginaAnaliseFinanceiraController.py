import streamlit as st
import src.view.Financeiro.pages.Mercado.paginaAnaliseFinanceiraView as pagina_analise_financeira_view
import src.model.pages.Mercado.paginaAnaliseFinanceiraModel as pagina_analise_financeira_model
import data.dadosBolsaValores as baseDados




class FinanceiroAnaliseFinanceiraController():
    try:
        #Funcao que chama a pagina inicial View
        def inicio_pagina_analise_financeira_controller():
            opcao = pagina_analise_financeira_view.pagina_analise_financeira_view()

        #Funco Formata Data
        def formata_data(dataInformada):
            resultado = pagina_analise_financeira_model.format_date(dataInformada)
            return resultado

        #Funcao Obtem Acoes
        def obterAtivosFinanceiros():
            resultado = pagina_analise_financeira_model.obterAtivosBolsaValores()
            return resultado

    except Exception as error:
        print(error)
        #Apagar essa linha quando subir para PRD
        st.write(error)
import streamlit as st
import src.view.Financeiro.pages.paginaListaObservacaoView as pagina_lista_observacao_view




class FinanceiroListaObservacaoController():
    try:
        #Funcao que chama a pagina inicial View
        def inicio_pagina_calendario_controller():
            opcao = pagina_lista_observacao_view.pagina_lista_observacao_view()
    except Exception as error:
        print(error)
        #Apagar essa linha quando subir para PRD
        st.write(error)
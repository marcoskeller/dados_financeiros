import streamlit as st
import src.view.Financeiro.pages.Mercado.paginaMercadoView as pagina_mercado_view





class FinanceiroMercadoController():
    try:
        #Funcao que chama a pagina inicial View
        def inicio_pagina_mercado_controller():
            opcao = pagina_mercado_view.pagina_mercado_view()
    except Exception as error:
        print(error)
        #Apagar essa linha quando subir para PRD
        st.write(error)
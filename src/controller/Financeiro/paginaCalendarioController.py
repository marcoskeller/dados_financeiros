import streamlit as st
import src.view.Financeiro.pages.paginaCalendarioView as pagina_calendario_view
import src.model.pages.paginaCalendarioModel as pagina_calendario_model




class FinanceiroCalendarioController():
    try:
        #Funcao que chama a pagina inicial View
        def inicio_pagina_calendario_controller():
            opcao = pagina_calendario_view.pagina_calendario_view()
        
        #Funcao que chama o modulo Calendario do Model
        def exibi_modelo_calendario_controller():
            opcao = pagina_calendario_model.gera_calendario_model()

    except Exception as error:
        print(error)
        #Apagar essa linha quando subir para PRD
        st.write(error)
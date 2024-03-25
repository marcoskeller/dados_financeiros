import streamlit as st
import src.controller.Financeiro.Mercado.paginaMercadoController as pagina_mercado_controller


try:
    def pagina_mercado_view():
        
        #Configuraca do Estilo CSS da Pagina
        with open('./styles/paginaMercadoCSS.css') as f:
          css = f.read()

        st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
        
        #Chamada do Controller da Pagina
        #pagina_mercado_controller.FinanceiroMercadoController.inicio_pagina_mercado_controller()
except Exception as error:
    print(error)
    #Apagar essa linha quando subir para PRD
    st.write(error)
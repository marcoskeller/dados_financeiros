import streamlit as st
import src.controller.Financeiro.Mercado.paginaAnaliseFinanceiraController as pagina_analise_financeira_controller



try:
    def pagina_analise_financeira_view():
       
        #Configuraca do Estilo CSS da Pagina
        with open('./styles/paginaMercadoCSS.css') as f:
          css = f.read()
       
        
        st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
        
        #Estilizando o Texto Central da Pagina
        st.markdown("<div id=titulo_pagina><h1 style='text-align: center; color: #ffffff;font-size: 60px;'>Análise Financeira</h1></div>", unsafe_allow_html=True)
   

        def pagina_sidebar():
            tickers, prices = pagina_analise_financeira_controller.FinanceiroAnaliseFinanceiraController.pagina_sidebar_controller()
            if tickers:
                pagina_analise_financeira_controller.FinanceiroAnaliseFinanceiraController.pagina_resultado_analise_financeira__controller(tickers, prices)
       

        #Inicializando a Analise dos Ativos Financeiros
        pagina_sidebar()
       
        

except Exception as error:
    print(error)
    #Apagar essa linha quando subir para PRD
    st.write(error)
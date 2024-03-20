import streamlit as st
import src.view.dadosFinanceirosView as inicializandoPagina
import src.controller.dadosFinanceirosController as dadosController
import src.view.index as Pagina_Visualizacao


def inicio():
    try:
        #Configuracao do Nome do Site
        st.set_page_config(
            page_title="Dados Financeiros",
            layout="wide"
        )
        Pagina_Visualizacao.pagina_View()
        #inicializandoPagina.inicio_view()
        #dadosController.DadosFinanceirosController.start()
    except:
        print("Erro ao Inicializar")

inicio()
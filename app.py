import streamlit as st
import src.controller.Inicio.paginaInicioController as dadosController


#Inicializa o Programa
def inicio():
    try:
        dadosController.DadosFinanceirosController.pagina_inicial_controller()    
    except Exception as error:
        print(error)
        #Apagar essa linha quando subir para PRD
        st.write(error)
        

inicio()
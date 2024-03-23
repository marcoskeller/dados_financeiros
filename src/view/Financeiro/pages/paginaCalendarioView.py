import streamlit as st
from streamlit_elements import elements, mui, html
import src.model.pages.paginaCalendarioModel as pagina_calendario_model
import src.controller.Financeiro.paginaCalendarioController as pagina_calendario_controller


try:
    def pagina_calendario_view():
        pagina_calendario_controller.FinanceiroCalendarioController.exibi_modelo_calendario_controller()
        #st.write('Este é um teste para validar a chamada de página')
        # with elements("new_element"):

        #     # Let's create a Typography element with "Hello world" as children.
        #     # The first step is to check Typography's documentation on MUI:
        #     # https://mui.com/components/typography/
        #     #
        #     # Here is how you would write it in React JSX:
        #     #
        #     # <Typography>
        #     #   Hello world
        #     # </Typography>
             
        #     mui.Typography("Hello world")
        
    
except Exception as error:
    print(error)
    #Apagar essa linha quando subir para PRD
    st.write(error)
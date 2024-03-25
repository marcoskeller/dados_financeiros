import streamlit as st
import src.controller.Financeiro.Mercado.paginaAnaliseFinanceiraController as pagina_analise_financeira_controller
import datetime as dt



try:
    def pagina_analise_financeira_view():
        
        #Configuraca do Estilo CSS da Pagina
        with open('./styles/paginaMercadoCSS.css') as f:
          css = f.read()

        st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
        st.markdown('Bem Vindo a Pagina Análise Financeira')

      
        if st.sidebar.button('Click Aqui Também'):
            st.info('Você clicou em: {}'.format(pagina_analise_financeira_controller.FinanceiroAnaliseFinanceiraController.formata_data(dt.datetime.now())))

        opcao = st.sidebar.selectbox('Selecione o Ativo Desejado', pagina_analise_financeira_controller.FinanceiroAnaliseFinanceiraController.obterAtivosFinanceiros(), None)
            
except Exception as error:
    print(error)
    #Apagar essa linha quando subir para PRD
    st.write(error)
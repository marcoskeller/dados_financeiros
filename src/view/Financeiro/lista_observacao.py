import streamlit as st
import datetime


#Formatando as Datas
def format_date(dt, format='%d/%m/%Y'):
	return dt.strftime(format)

def pagina_lista_obervcacao():
    st.title('Teste de Pagina')
    st.write('Este é um teste para validar a chamada de página')

    with open('./styles/styles.css') as f:
        css = f.read()

    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

    if st.button('Click Aqui'):
      st.info('Você clicou em:  {}'.format(format_date(datetime.datetime.now())))


    if st.sidebar.button('Click Aqui Também'):
      st.info('Você clicou em: {}'.format(format_date(datetime.datetime.now())))
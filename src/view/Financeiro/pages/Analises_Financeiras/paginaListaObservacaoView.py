import streamlit as st
import datetime as dt
from datetime import date, timedelta
import src.controller.Financeiro.Analises_Financeiras.paginaListaObervacaoController as pagina_lista_observacao_controller
import src.view.Financeiro.pages.Analises_Financeiras.analise_financeira_cotacao_tempo_view as cotacao_tempo_view
import pandas as pd
import pandas_datareader.data as pdr
from streamlit_option_menu import option_menu


#Formatando as Datas
def format_date(dt, format='%d/%m/%Y'):
	return dt.strftime(format)

try:
  def pagina_lista_observacao_view():

    with open('./styles/styles.css') as f:
      css = f.read()

    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


    st.sidebar.image("./images/bolsa_valores_sidebar.png")
    with st.sidebar:
        selected = option_menu("Análises Financeiras", ["Início", 'Cotação x Tempo','Retorno Diário', 'Retorno Acumulado', 'Analise 5'], 
            icons=['house', 'gear'], 
            menu_icon="cast", 
            default_index=1)
        selected


    if selected == "Início":
      st.title('Titulo da Pagina')
      st.subheader('Sub Titulo da Pagina')
      st.write("""Esta é uma introdução de como analisar dados históricos de ações, índices e câmbios 
                    utilizando Python. A fonte utilizada foi o finance.yahoo.com, por onde é possível 
                    obter os dados de forma muito simples usando o Pandas. Este estudo não tem como 
                    finalidade a recomendação de compra de nenhum ativo, é somente uma demonstração de como 
                    utilizar a linguagem Python para começar uma análise de ativos na bolsa, 
                    sendo possível, a partir disso, analisar de forma mais profunda 
                    e implementar modelos preditivos de machine learning.""")
    
    if selected == "Cotação x Tempo":
      resultado = cotacao_tempo_view.pagina_analise_financeira_cotacao_tempo_view()
  
     
    if selected == "Retorno Diário":
      st.write('Pagina 2')

    if selected == "Retorno Acumulado":
      st.write('Pagina 2')
    
    if selected == "Retorno Acumulado":
      st.write('Pagina 2')
    
    if selected == "Retorno Acumulado":
      st.write('Pagina 2')
    
    #Buscando os Nome das Ações
    # ticker_list = pagina_lista_observacao_controller.FinanceiroListaObservacaoController.obter_ativos_bolsaValores_controller()
    # tickers = st.sidebar.multiselect(label="Selecione as Empresas", options=ticker_list, placeholder="Ações")

    
    #Selecionando as Datas
    #Adcionando mais dias na data atual
    # td = timedelta(-7)
    # data_inicial = st.sidebar.date_input("De", format="DD/MM/YYYY", value=date.today() + td)
    
    # data_final = st.sidebar.date_input("Até", format="DD/MM/YYYY",value=dt.datetime.now())
    
    # #Estrutura Principal
    # opcao = ['NÃO','SIM']
    # exibiDataFrame = st.sidebar.selectbox("Deseja Mostrar o DataFrame", options=opcao)

    # if exibiDataFrame == 'SIM':
    #   df = pagina_lista_observacao_controller.FinanceiroListaObservacaoController.obter_dados_ativos_controller(tickers, data_inicial, data_final)
      
    #   #Normalizando a coluna data
    #   #Filtrando a Data
    #   df = pd.DataFrame(df)
    #   df['Data'] = pd.to_datetime(df.index)
    #   df['Data'] = df['Data'].dt.strftime('%d/%m/%Y')
      
    #   df2 = pd.DataFrame(df)

    #   resultado = pd.DataFrame(df2)
    #   st.dataframe(resultado, use_container_width=True)
      
      

        
      
      
    # if st.button('Click Aqui'):
    #   st.info('Você clicou em:  {}'.format(format_date(dt.datetime.now())))


    #   if st.sidebar.button('Click Aqui Também'):
    #     st.info('Você clicou em: {}'.format(format_date(dt.datetime.now())))
except Exception as error:
    print(error)
    #Apagar essa linha quando subir para PRD
    st.write(error + st.write('Erro na Chamada da Funcao Exibir DataFrame do Controller'))










# #Formatando as Datas
# def format_date(dt, format='%d/%m/%Y'):
# 	return dt.strftime(format)

# def pagina_lista_observacao_view():
#     st.title('Teste de Pagina')
#     st.write('Este é um teste para validar a chamada de página')

#     with open('./styles/styles.css') as f:
#         css = f.read()

#     st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

#     if st.button('Click Aqui'):
#       st.info('Você clicou em:  {}'.format(format_date(datetime.datetime.now())))


#     if st.sidebar.button('Click Aqui Também'):
#       st.info('Você clicou em: {}'.format(format_date(datetime.datetime.now())))

import streamlit as st
import datetime as dt
import src.controller.dadosFinanceirosController as dadosController





def inicio_view():
    
    try:

        #Elementos Centrais da Pagina
        st.title('Monitor do Mercado de Ações')

	    #Selecao do Pais
        selecionando_pais = st.sidebar.selectbox("Selecione o País: ", dadosController.DadosFinanceirosController.selecionaPais())

        #Selecao do Ativo Desejado
        selecionando_acao = st.sidebar.selectbox("Selecione o Ativo Desejado: ", dadosController.DadosFinanceirosController.obterNomeAtivos(selecionando_pais))
        
        #Selecao do Intervalo
        #selecionando_intervalo = st.sidebar.selectbox("Selecione o Intervalo Desejado: ", dadosController.selecionaIntervalo())

        #Definicao das Datas
        inicio_data = dt.datetime.now() + dt.timedelta(days=-30)
        fim_data = dt.datetime.today()
        
        #Selecao das Datas
        data_inicial = st.sidebar.date_input('De: ', inicio_data)
        data_final = st.sidebar.date_input('Até: ', fim_data)

        #Obten Dados da Ação Escolhida
        dadosController.DadosFinanceirosController.exibiDadosAcaoSelecionada(selecionando_acao, data_inicial, data_final)

        #Exibicao do Grafico
        opcao = ['SIM', 'NÃO']
        exibiGraficoSimples = st.sidebar.selectbox("Deseja Exibir o Gráfico: ", opcao, None)
        dadosController.DadosFinanceirosController.exibiGraficoSimplesController(exibiGraficoSimples,selecionando_acao, data_inicial, data_final)
        
    except Exception as error:
        st.write(error)
        print(error)
		
    
    
    
    
import streamlit as st
import datetime as dt
import hydralit_components as hc
import datetime
import src.controller.Financeiro.paginaListaObervacaoController as lista_observacao_controller
import src.controller.Financeiro.paginaCalendarioController as pagina_calendario_controller
import src.controller.Financeiro.Mercado.paginaAnaliseFinanceiraController as pagina_analise_financeira_controller



    
try:
    def inicio_view():
        #Configuracao Geral da Pagina 
        st.set_page_config(
            page_title="Dados Financeiros",
            layout='wide',
            initial_sidebar_state='collapsed',
        )


        #Definindo o Menu Principal
        menu_data = [
            {'icon': "far fa-copy", 'label':"Listas de observação"},
            {'id':'Copy','icon':"bi bi-collection",'label':"Meu Portfolio"},
            {'id':'Mercados','icon':"fa-solid fa-radar",'label':"Mercados", 'submenu':[
            {'id':'AnaliseFinanceira','icon': "fa fa-paperclip", 'label':"Análise Financeira"},
            {'id':'AcoesMaioresGanhos','icon': "bi bi-graph-up-arrow", 'label':"Ações: Maiores Ganhos"},
            {'id':'AcoesManioresPerdas','icon': "bi bi-graph-down-arrow", 'label':"Ações: Maiores Perdas"}]},
            {'icon': "far fa-chart-bar", 'label':"Gráficos"},#no tooltip message
            {'id':'Calendario','icon': "bi bi-calendar2-date", 'label':"Calendário"},
            {'icon': "fas fa-tachometer-alt", 'label':"Dashboard",'ttip':"I'm the Dashboard tooltip!"}, #can add a tooltip message
            {'icon': "bi bi-google", 'label':"Notícias"},
            {'icon': "fa-solid fa-radar",'label':"Finanças Pessoais", 'submenu':[
            {'label':"Análise de Patrimônio", 'icon': "bi bi-cash-stack"},
            {'icon':'bi bi-currency-dollar','label':"Análise de ETF"},
            {'icon':'bi bi-currency-exchange','label':"Análise de Futuros",}]},
        ]

        over_theme = {'txc_inactive': '#FFFFFF'}
        menu_id = hc.nav_bar(
            menu_definition=menu_data,
            override_theme=over_theme,
            home_name='Inicio',
            login_name='Sair',
            hide_streamlit_markers=True, #will show the st hamburger as well as the navbar now!
            sticky_nav=True, #at the top or not
            sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
        )

        #Selecionando uma Pagina
        if menu_id == "Listas de observação":
            lista_observacao_controller.FinanceiroListaObservacaoController.inicio_pagina_calendario_controller()
            
        if menu_id == "Calendario":           
            pagina_calendario_controller.FinanceiroCalendarioController.inicio_pagina_calendario_controller()
        
        if menu_id == "Mercados":           
            pagina_calendario_controller.FinanceiroCalendarioController.inicio_pagina_calendario_controller()
        
        if menu_id == "AnaliseFinanceira":           
            pagina_analise_financeira_controller.FinanceiroAnaliseFinanceiraController.inicio_pagina_analise_financeira_controller()
        
        if menu_id == "AcoesMaioresGanhos":           
            pagina_calendario_controller.FinanceiroCalendarioController.inicio_pagina_calendario_controller()
        
        if menu_id == "AcoesManioresPerdas":           
            pagina_calendario_controller.FinanceiroCalendarioController.inicio_pagina_calendario_controller()
        
        # if st.button('Click Aqui'):
        #   st.info('You clicked at: {}'.format(datetime.datetime.now()))


        # if st.sidebar.button('Click Aqui Também'):
        #   st.info('You clicked at: {}'.format(datetime.datetime.now()))

        #get the id of the menu item clicked
        #st.info(f"{menu_id}")

except Exception as error:
    print(error)
    #Apagar essa linha quando subir para PRD
    st.write(error)
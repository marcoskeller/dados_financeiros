import streamlit as st
import datetime as dt
import hydralit_components as hc
import datetime
import src.view.Financeiro.pages.lista_observacao as listaObervacao

    
 
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
        {'icon': "fa-solid fa-radar",'label':"Mercados", 'submenu':[
           {'id':' subid11','icon': "fa fa-paperclip", 'label':"Ações: Mais Ativas"},
           {'id':'subid12','icon': "bi bi-graph-up-arrow", 'label':"Ações: Maiores Ganhos"},
           {'id':'subid13','icon': "bi bi-graph-down-arrow", 'label':"Ações: Maiores Perdas"}]},
        {'icon': "far fa-chart-bar", 'label':"Gráficos"},#no tooltip message
        {'id':' Crazy return value 💀','icon': "bi bi-calendar2-date", 'label':"Calendário"},
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
        #listaObervacao.pagina_lista_obervcacao()
        listaObervacao.pagina_lista_obervcacao()
        
    
    # if st.button('Click Aqui'):
    #   st.info('You clicked at: {}'.format(datetime.datetime.now()))


    # if st.sidebar.button('Click Aqui Também'):
    #   st.info('You clicked at: {}'.format(datetime.datetime.now()))

    #get the id of the menu item clicked
    #st.info(f"{menu_id}")
import streamlit as st
import src.controller.Financeiro.Analises_Financeiras.pagina_analise_economica_da_empresa_controller as analise_financeira_da_empresa_controller

try:
        
    def pagina_analise_economica_da_empresa_view():
        
        mostrarDataframe = st.sidebar.checkbox('Informações Econômicas das Empresas')
        exibir_analise_por_papel = st.sidebar.checkbox('Análise - EV/EBIT e ROIC')
        show_rendimento_liquido = st.sidebar.checkbox('Análise - Liquidez Média Diária')
        exibir_analise_formula_magica = st.sidebar.checkbox('Fórmula Mágica de Joel Greenblatt')
        
        if mostrarDataframe:
            df = analise_financeira_da_empresa_controller.pagina_analise_economica_da_empresa_obter_informaces_economicas_controller()


        if exibir_analise_por_papel:
            
            df = analise_financeira_da_empresa_controller.pagina_analise_economica_da_empresa_obter_informacoes_economicas_empresa_ranking_controller()
            show_posicao = st.selectbox('Filtros Por Posição ', options=range(0, 151), placeholder='Papéis')
            if show_posicao:
                exibi_posicao = analise_financeira_da_empresa_controller.pagina_analise_economica_da_empresa_obter_informacoes_economicas_empresa_exibir_posicao_ranking_controller(show_posicao)
            
        
        if show_rendimento_liquido:
            t = [0, 1000000, 5000000, 10000000, 100000000, 500000000, 1000000000]
            show_rendimento_liquido = st.selectbox('Liquidez Média Diária em 2 Meses ', options=t, placeholder='Liquidez Média')
            if show_rendimento_liquido > 0:
                df = analise_financeira_da_empresa_controller.pagina_analise_economica_da_empresa_obter_rendimento_liquido_empresa_controller(show_rendimento_liquido)
            else:
                st.write('Selecione um valor para o Filtro')
         
         
        if exibir_analise_formula_magica:
            df = analise_financeira_da_empresa_controller.pagina_analise_economica_da_empresa_obter_informacoes_economicas_empresa_exibir_posicao_formula_magica_conotroller()
            
            exibir_as_empresas_tops = st.checkbox('Exibir às 10 Melhores Empresas Listadas no Ranking')
  
            if exibir_as_empresas_tops:
                empresas_top = analise_financeira_da_empresa_controller.pagina_analise_economica_da_empresa_obter_informacoes_economicas_exibir_melhores_empresas_ranking_controller()
                return empresas_top
        

except Exception as error:
    print(error)
    #Apagar essa linha quando subir para PRD
    st.write(error + st.write('Erro na Chamada da Funcao'))
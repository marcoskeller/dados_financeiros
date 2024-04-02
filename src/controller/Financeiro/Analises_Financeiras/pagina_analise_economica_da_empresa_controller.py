import streamlit as st
import src.model.pages.Analises_Financeiras.pagina_analise_economica_da_empresa_model as analise_economica_da_empresa



try:
    def pagina_analise_economica_da_empresa_obter_informaces_economicas_controller():
        resultado = analise_economica_da_empresa.pagina_analise_economica_da_empresa_obter_informacoes_economicas_empresa_model()
        return st.dataframe(resultado)


    def pagina_analise_economica_da_empresa_obter_nomes_ativos_bolsaValores_controller():
        resultado = analise_economica_da_empresa.pagina_analise_economica_da_empresa_obter_nomes_ativos_bolsaValores_model()
        return resultado
    

    def pagina_analise_economica_da_empresa_obter_rendimento_liquido_empresa_controller(valor_rendimento):
        resultado = analise_economica_da_empresa.pagina_analise_economica_da_empresa_obter_rendimento_liquido_empresa_model(valor_rendimento) 
        return st.dataframe(resultado, use_container_width=True, hide_index=True)
    

    def pagina_analise_economica_da_empresa_obter_informacoes_economicas_empresa_ranking_controller():
        resultado = analise_economica_da_empresa.pagina_analise_economica_da_empresa_obter_informacoes_economicas_empresa_ranking_model()
        return st.dataframe(resultado, use_container_width=True, hide_index=True)
    

    def pagina_analise_economica_da_empresa_obter_informacoes_economicas_empresa_exibir_posicao_ranking_controller(posicao):
        resultado = analise_economica_da_empresa.pagina_analise_economica_da_empresa_obter_informacoes_economicas_empresa_exibir_posicao_ranking_model(posicao)
        return st.dataframe(resultado)
    

    def pagina_analise_economica_da_empresa_obter_informacoes_economicas_empresa_exibir_posicao_formula_magica_conotroller():
        resultado = analise_economica_da_empresa.pagina_analise_economica_da_empresa_obter_informacoes_economicas_empresa_exibir_posicao_formula_magica_model()
        return st.dataframe(resultado, use_container_width=True)
    

    def pagina_analise_economica_da_empresa_obter_informacoes_economicas_exibir_melhores_empresas_ranking_controller():
        resultado = analise_economica_da_empresa.pagina_analise_economica_da_empresa_obter_informacoes_economicas_exibir_melhores_empresas_ranking_model()
        return st.dataframe(resultado)


except Exception as error:
    print(error)
    #Apagar essa linha quando subir para PRD
    st.write(error + st.write('Erro na Chamada da Funcao'))
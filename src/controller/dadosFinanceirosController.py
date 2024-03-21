import streamlit as st
import src.model.dadosFinanceirosModel as baseDadosModel
import src.view.dadosFinanceirosView as paginaView



class DadosFinanceirosController():
    
    #Funcao que chama a pagina inicial View
    def start():
        opcao = paginaView.inicio_view()
        

    def selecionaPais():
        resultado = baseDadosModel.paises()
        return resultado

    def obterNomeAtivos(nomeNacao):
        if nomeNacao == '':
            resultado = st.write('Selecione um País')
            return resultado
        elif nomeNacao == 'Brasil':
            resultado = baseDadosModel.acoesYahooFinance()
            return resultado
        elif nomeNacao == 'Estados Unidos da América':
            resultado = baseDadosModel.solicitarNomeAtivosBolsaAmericana()
            return resultado
        else:
            st.write('Você não selecionou um país.')

    def selecionaIntervalo():
        resultado = baseDadosModel.intervalo()
        return resultado
    
    #Obtendo os Dados da Acao Escolhida
    def exibiDadosAcaoSelecionada(acaoEscolhida, data_inicial, data_final):   
        if acaoEscolhida != '':
            #Qual ação foi escolhida
            st.subheader(acaoEscolhida)
            resultado = baseDadosModel.solicitarDadosAcoesBrasileira(acaoEscolhida, data_inicial, data_final)
            return st.dataframe(resultado, use_container_width=True)
        else:
            st.write('Escolha um Ativo')

    #Plotando o Grafico Simples
    def exibiGraficoSimplesController(opcao, acaoEscolhida, data_inicial, data_final):
        if opcao == 'SIM':
            resultado = baseDadosModel.plotaGraficoSimplesModel(acaoEscolhida, data_inicial, data_final)
            return resultado
        else:
            print()
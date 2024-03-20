import src.model.dadosFinanceirosModel as baseDadosModel
import src.view.dadosFinanceirosView as paginaView



class DadosFinanceirosController():
    
    #Funcao que chama a pagina inicial View
    def start():
        opcao = paginaView.inicio_view()
        

    def acoesBrasileirasYahooFinance():
        resultado = baseDadosModel.acoesYahooFinance()
        return resultado


    def selecionaPais():
        resultado = baseDadosModel.paises()
        return resultado


    def selecionaIntervalo():
        resultado = baseDadosModel.intervalo()
        return resultado
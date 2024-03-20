


class DadosFinanceirosBancoDeDados():
    
    #Paises Para Consulta  
    def  paises():
        paises = ['','Brasil', 'Estados Unidos da América']
        return paises

    #Acoes Disponiveis no Yahoo Finance        
    def  acoesYahooFinance():
        acoes_yFinace = ['','EMBR3.SA','CTIP3.SA','ENBR3.SA','CESP6.SA','CSAN3.SA','BRFS3.SA','CCRO3.SA','ESTC3.SA','BRAP4.SA','BBDC4.SA','BBDC3.SA','ECOR3.SA','CSNA3.SA',
        'CPLE6.SA','EQTL3.SA','CMIG4.SA','CYRE3.SA','CPFE3.SA','BVMF3.SA','656690','CIEL3.SA','BRML3.SA','GGBR4.SA','BRKM5.SA','BBAS3.SA','ABEV3.SA','BRPR3.SA',
        'BBSE3.SA','FIBR3.SA','ELET3.SA']
        return acoes_yFinace
        
    #Intervalo da Consulta
    def intervalo(): 
        intervalo = ['','Daily', 'Weekly', 'Monthly']
        return intervalo
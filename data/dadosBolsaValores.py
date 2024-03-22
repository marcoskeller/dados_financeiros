import yfinance as yf
import investpy as ip
import pandas_datareader.data as web
import streamlit as st
import matplotlib.pyplot as plt


class DadosFinanceirosBancoDeDados():
    
    #Paises Para Consulta  
    def  paises():
        paises = ['Brasil', 'Estados Unidos da América']
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
    

    #Obtendo os Nomes das Acoes Americanas
    def obterNomeAcoesAmericana():
        nomeAcoesAmericana = ip.get_stocks_list(country='united states')
        return nomeAcoesAmericana
    

    #Obtendo os dados da ação Brasileira no Yahoo Finance
    def obterDadosAcoesBrasileira(acaoEscolhida, data_inicial, data_final):
        df = yf.download(acaoEscolhida, start=data_inicial, end=data_final, progress=False)
        return df
    

    #Obtendo os dados da ação Brasileira no Yahoo Finance Get
    def obterDadosAcoesGetDataYahoo(acaoEscolhida, data_inicial, data_final):
        yf.pdr_override()
        resultado = web.get_data_yahoo((acaoEscolhida), start=data_inicial, end=data_final)
        return resultado
    

    #Obtendo os dados da ação Brasileira no Yahoo Finance Dowload
    def obterDadosAcoesDownloadDataYahoo(acaoEscolhida, data_inicial, data_final):
        yf.pdr_override()
        #resultado = web.get_data_yahoo((acaoEscolhida), start=data_inicial, end=data_final)
        resultado = yf.download((acaoEscolhida), start=data_inicial, end=data_final, period='id')
        return resultado
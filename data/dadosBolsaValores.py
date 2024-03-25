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


    def ativosBolsaValores():
        ativosFinanceiros = ['AALR3','ABCB4','ABEV3','AESB3','AGRO3','ALPA4','ALUP11','AMAR3','AMBP3','ANIM3','ARML3','ARZZ3',
                            'ASAI3','AURE3','AZUL4','B3SA3','BBAS3','BBDC3','BBDC4','BBSE3','BEEF3','BHIA3','BLAU3','BMOB3',
                            'BPAC11','BPAN4','BRAP4','BRFS3','BRKM5','BRSR6','CAML3','CASH3','CBAV3','CCRO3','CEAB3','CIEL3','CMIG3',
                            'CMIG4','CMIN3','COGN3','CPFE3','CPLE6','CRFB3','CSAN3','CSMG3','CSNA3','CURY3','CVCB3','CXSE3','CYRE3',
                            'DASA3','DIRR3','DXCO3','ECOR3','EGIE3','ELET3','ELET6','EMBR3','ENAT3','ENEV3','ENGI11','EQTL3','ESPA3',
                            'EVEN3','EZTC3','FESA4','FLRY3','FRAS3','GFSA3','GGBR4','GGPS3','GMAT3','GOAU4','GRND3','GUAR3','HAPV3',
                            'HBSA3','HYPE3','IFCM3','IGTI11','INTB3','IRBR3','ITSA4','ITUB3','ITUB4','JALL3','JBSS3','JHSF3','KEPL3',
                            'KLBN11','LAVV3','LEVE3','LJQQ3','LOGG3','LREN3','LUPA3','LWSA3','MATD3','MBLY3','MDIA3','MGLU3','MILS3',
                            'MLAS3','MOVI3','MRFG3','MRVE3','MTRE3','MULT3','MYPK3','NEOE3','NTCO3','ODPV3','ONCO3','ORVR3','PCAR3',
                            'PETR3','PETR4','PETZ3','PGMN3','PLPL3','PNVL3','POMO4','POSI3','PRIO3','PSSA3','PTBL3','QUAL3','RADL3',
                            'RAIL3','RAIZ4','RANI3','RAPT4','RCSL3','RDOR3','RECV3','RENT3','ROMI3','RRRP3','SANB11','SAPR11','SBFG3',
                            'SBSP3','SEER3','SIMH3','SLCE3','SMFT3','SMTO3','SOMA3','SRNA3','STBP3','SUZB3','TAEE11','TASA4','TEND3',
                            'TGMA3','TIMS3','TOTS3','TRIS3','TRPL4','TTEN3','TUPY3','UGPA3','UNIP6','USIM5','VALE3','VAMO3','VBBR3',
                            'VIVA3','VIVT3','VLID3','VULC3','VVEO3','WEGE3','WIZC3','YDUQ3','ZAMP3']
        return ativosFinanceiros
     
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
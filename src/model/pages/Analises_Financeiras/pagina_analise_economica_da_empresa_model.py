import data.dadosBolsaValores as baseDados
import pandas as pd



#Busca os Ativos da Bolsa
def pagina_analise_economica_da_empresa_obter_nomes_ativos_bolsaValores_model():
    resultado = baseDados.DadosFinanceirosBancoDeDados.ativosBolsaValores()
    return resultado


def pagina_analise_economica_da_empresa_obter_informacoes_economicas_empresa_modeladas_model():
    resultado = baseDados.DadosFinanceirosBancoDeDados.obterInformacoesEconomicasEmpresas()
    return resultado


def pagina_analise_economica_da_empresa_obter_informacoes_economicas_empresa_model():
    df = baseDados.DadosFinanceirosBancoDeDados.obterInformacoesEconomicasEmpresas()

    
    for coluna in ['Div.Yield', 'Mrg Ebit', 'Mrg. Líq.', 'ROIC', 'ROE', 'Cresc. Rec.5a']:
        df[coluna] = df[coluna].str.replace('.', '')
        df[coluna] = df[coluna].str.replace(',', '.')
        df[coluna] = df[coluna].str.rstrip('%').astype('float') / 100

    #Filtro 1
    #df = df[df['Liq.2meses'] > 1000000]
        
    #Filtro 2
    ranking = pd.DataFrame()
    ranking['Posicao'] = range(1,151)
    ranking['EV/EBIT'] = df[ df['EV/EBIT'] > 0 ].sort_values(by=['EV/EBIT'])['Papel'][:150].values
    ranking['ROIC'] = df.sort_values(by=['ROIC'], ascending=False)['Papel'][:150].values

    #Filtro 3
    a = ranking.pivot_table(columns='EV/EBIT', values='Posicao')
     
    b = ranking.pivot_table(columns='ROIC', values='Posicao')
 
    t = pd.concat([a,b])

    rank = t.dropna(axis=1).sum()

    return t


def pagina_analise_economica_da_empresa_obter_rendimento_liquido_empresa_model(valor_rendimento):
    df = baseDados.DadosFinanceirosBancoDeDados.obterInformacoesEconomicasEmpresas()

    
    for coluna in ['Div.Yield', 'Mrg Ebit', 'Mrg. Líq.', 'ROIC', 'ROE', 'Cresc. Rec.5a']:
        df[coluna] = df[coluna].str.replace('.', '')
        df[coluna] = df[coluna].str.replace(',', '.')
        df[coluna] = df[coluna].str.rstrip('%').astype('float') / 100

    #Filtro 1
    df = df[df['Liq.2meses'] >= valor_rendimento]
        
    return df


def pagina_analise_economica_da_empresa_obter_informacoes_economicas_empresa_ranking_model():
    df = baseDados.DadosFinanceirosBancoDeDados.obterInformacoesEconomicasEmpresas()

    
    for coluna in ['Div.Yield', 'Mrg Ebit', 'Mrg. Líq.', 'ROIC', 'ROE', 'Cresc. Rec.5a']:
        df[coluna] = df[coluna].str.replace('.', '')
        df[coluna] = df[coluna].str.replace(',', '.')
        df[coluna] = df[coluna].str.rstrip('%').astype('float') / 100

     
    #Filtro Ranking
    ranking = pd.DataFrame()
    ranking['Posicao'] = range(1,151)
    ranking['EV/EBIT'] = df[ df['EV/EBIT'] > 0 ].sort_values(by=['EV/EBIT'])['Papel'][:150].values
    ranking['ROIC'] = df.sort_values(by=['ROIC'], ascending=False)['Papel'][:150].values

    return ranking


def pagina_analise_economica_da_empresa_obter_informacoes_economicas_empresa_exibir_posicao_ranking_model(posicao):
    ranking_empresas = pagina_analise_economica_da_empresa_obter_informacoes_economicas_empresa_ranking_model()

    for item in ranking_empresas['Posicao']:
        if item == posicao:
            lin = ranking_empresas.loc[posicao-1]
            return lin

  
def pagina_analise_economica_da_empresa_obter_informacoes_economicas_empresa_exibir_posicao_formula_magica_model():
    ranking_formula_magica = pagina_analise_economica_da_empresa_obter_informacoes_economicas_empresa_ranking_model()

    a = ranking_formula_magica.pivot_table(columns='EV/EBIT', values='Posicao')
    b = ranking_formula_magica.pivot_table(columns='ROIC', values='Posicao')
    rank = pd.concat([a,b])
    resultado = rank.dropna(axis=1).sum()
    resultado_ordenado =  resultado.sort_values()
    return resultado_ordenado


def pagina_analise_economica_da_empresa_obter_informacoes_economicas_exibir_melhores_empresas_ranking_model():
    ranking_formula_magica = pagina_analise_economica_da_empresa_obter_informacoes_economicas_empresa_ranking_model()

    a = ranking_formula_magica.pivot_table(columns='EV/EBIT', values='Posicao')
    b = ranking_formula_magica.pivot_table(columns='ROIC', values='Posicao')
    rank = pd.concat([a,b])
    resultado = rank.dropna(axis=1).sum()
    resultado_ordenado =  resultado.sort_values()
    resultado_ordenado = resultado_ordenado.sort_values()[:10]
    return resultado_ordenado



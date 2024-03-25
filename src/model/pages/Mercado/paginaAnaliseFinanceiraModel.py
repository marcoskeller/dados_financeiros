import data.dadosBolsaValores as baseDados



#Formatando as Datas
def format_date(dt, format='%d/%m/%Y'):
	return dt.strftime(format)


#Busca os Ativos da Bolsa
def obterAtivosBolsaValores():
    resultado = baseDados.DadosFinanceirosBancoDeDados.ativosBolsaValores()
    return resultado
# Passo a passo de solução

# Abrir os 6 arquivos em Excel

# Para cada arquivo:

# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000

# Se for maior do que  55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor

# Caso não seja maior do que 55.000 não quero fazer nada

import pandas as pd
from twilio.rest import Client


#Leitura pra enviar SMS
# Your Account SID from twilio.com/console
account_sid = "AC62647b690e545181ee9af63254b3d71f"
# Your Auth Token from twilio.com/console
auth_token  = "ce832912aae7ac7be5ba003d63c933c7"
client = Client(account_sid, auth_token)

#Todas lista no Python fica entre []
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

#Para cada mes dentro da lista de meses, eu quero executar o codigo
for mes in lista_meses:
#Ler arquivo em Excel
    #"f" serve para formatar o cógido em python
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    #Selecionando uma coluna especifica a qual foi declarada na lista, any()caso "algum" valor for maior a tabela vendas
    if (tabela_vendas['Vendas'] > 55000).any():
        #Dentro da lista passa primeiro a Linha e depois Coluna.

        #Loc ele gera uma tabela referente a informação solicitada, já o .values ele retira a tabela e trás apenas o valor
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5511948587017",
            from_="+17753824602",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)






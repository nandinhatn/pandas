import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt


df= pd.read_csv("caso_full.csv", on_bad_lines='skip', sep=",")

df.columns.values[0]="Cidade"
df.columns.values[1] ="Cd Cidade IBGE"
df.columns.values[2] ="Data"
df.columns.values[3]= "Semana Epimemiologica"
df.columns.values[4]= "População Estimada"
df.columns.values[5] = "População estimada em 2019"
df.columns.values[6]= "è ultimo"
df.columns.values[7] = 'é repetido'
df.columns.values[8] = "Confirmado acumulado"
df.columns.values[9] = "Confirmado acumulado por 100k habitantes"
df.columns.values[10] = "Ultima Data Disponível"
df.columns.values[11] = "Ultima Taxa de Mortalidade Disponível"
df.columns.values[12]= "Últimas mortes disponíveis"
df.columns.values[13]= "Ordem por lugar"
df.columns.values[14] = "Tipo de Lugar"
df.columns.values[15] = "Estado"
df.columns.values[16] = "Novos Confirmados"
df.columns.values[17] = "Novas Mortes"
df= df.dropna()
print(df.columns.tolist())
cidade= df.get('city', default="no_cidade")
estado = df['Estado'].unique()

df['Data']= pd.to_datetime(df['Data'])
def search_cidade():
    cidade = input("Qual a cidade ")
    resposta = df.loc[df['Cidade'] == cidade]


    print(f""" A população estimada de {cidade} é {resposta['População Estimada'].mean()} habitantes
                Total de mortes = {resposta['Novas Mortes'].sum()}
                Contagem iniciada em :{(resposta['Data'].min()).day}/{(resposta['Data'].min()).month}/{(resposta['Data'].min()).year} e
                encerrrada em {(resposta['Data'].max()).day}/{((resposta['Data'].max()).month)}/{(resposta['Data'].max()).year}
                Tempo de Contagem ={(resposta['Data'].max() - resposta['Data'].min()).days} dias 

                """)

def total_cases():
    print(f"""
        O numero total de casos confirmados de mortos é de {df['Novas Mortes'].sum()} pessoas
        Em uma população total de {df['População estimada em 2019'].sum()} habitantes
        Essa contagem ocorreu entre os dias {(df['Data'].min()).day}/{(df['Data'].min()).month}/{(df['Data'].min()).year} e {(df['Data'].max()).day}/{(df['Data'].max()).month}/{(df['Data'].max()).year}
        """)

def search_by():
    # search =(df.groupby('Cidade')['Novas Mortes'].sum())
     print("As dez cidades com maiores números de mortes")
     print(df.sort_values('Novas Mortes', ascending=False).head(10))

def graphic():
    #total_produtos_venda= df.groupby("Produto")['Quantidade'].sum().sort_values(ascending= False).plot.barh(title= "Total produtos vendidos")
    df.groupby("Cidade")['Novas Mortes'].sum().sort_values(ascending=False).head(10).plot.barh(title="Total Mortes")
    plt.xlabel("Numero de Mortes")
    plt.ylabel("Cidade")
    plt.show()
def menu():
    texto_menu = """ Menu : 
                **** Bem vindo à pesquisa sobre COVID Brasil*** 
                    Os dados capturados são de 27 de março de 2022
                    #1 para Pesquise por sua cidade Informe o nome da cidade
                    #2 totalização dos casos
                    #3 Consulta / Cidade por Maíores Índices
                    #4 Graficos
                    #9 para sair
                    

                             """
    input_options=0
    print(texto_menu)
    while input_options !="9":
        input_options= input("Digite a opcão desejada")
        if input_options =="1":
             search_cidade()
        elif input_options=="2":
             total_cases()
        elif input_options=='3':
            search_by()
        elif input_options=='4':
            graphic()
        elif input_options=='9':
            return
        else:
            print("Opção Invalida")





menu()














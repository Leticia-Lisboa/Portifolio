import pandas as pd
# trabalhando dados usando pandas
df = pd.DataFrame(
    [
        ['PE', 'Pernambuco', 'Recife'], ['RJ', 'Rio de Janeiro', 'Rio de Janeiro'],
        ['PB', 'Paraíba', 'João Pessoa'], ['SP', 'São Paulo', 'São Paulo'],
        ['MG', 'Minas Gerais', 'Belo Horizonte'], ['CE', 'Ceará', 'Fortaleza'],
        ['AC', 'Acre', 'Rio Branco'], ['MA', 'Maranhão', 'São Luís'], ['RN', 'Rio Grande do Norte', 'Natal'],
        ['PR', 'Paraná', 'Curitiba'], ['RS', 'Rio Grande do Sul', 'Porto Alegre']
    ], columns=['Sigla', 'Nome', 'Capital']
)

df.index = df['Sigla']
print(df.index)
del df['Sigla']
print(df)
print(df['Nome'])


import pandas as pd

# Criando um DataFrame simples
dados = {
    'Nome': ['João', 'Maria', 'Pedro'],
    'Idade': [25, 30, 35],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
}

df = pd.DataFrame(dados)

# Mostrando o DataFrame
print("DataFrame criado com sucesso:")
print(df) 
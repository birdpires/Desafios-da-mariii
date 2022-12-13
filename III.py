# LISTA -
# Lista é uma coleção de valores indexada, pois aqui, um índice é identificado por um valor, sendo 0 o primeiro valor e segue respectivamente pela quantidade de itens que tiverem.
# Exemplo:

professoras = ['Tais', 'Mari', 'Karlla']
print(type(professoras)) # type ‘list’
print(professoras)

# TUPLAS -
# Tupla se parece com as listas mas diverge pela característica de ser imutável, ou seja, após uma tupla ser criada, ela não pode mais ser alterada.
# Exemplo:
Equipe_nove = ('Rodrygo', 'Caique', 'Erick', 'Pablo', 'Manoel', 'Diogo')
print(type(Equipe_nove)) # class=’tuple’
print(Equipe_nove)

# DICIONARIOS -
# Os dicionários são como coleções de dados que contém na sua estrutura um conjunto de pares de uma chave e um valor. Eles funcionam como um mapa que mostra as variações das informções de maneira mais completa.
# Exemplo:
dados = {
    'Nome': 'Rodrygo',
    'Idade': 18,
    'signo': 'Aries'
}
print(dados['Nome']) # Rodrygo
"""Questão 2

Faça um programa que leia os dados e preencha uma lista cujo conteúdo é a população dos 3 municípios mais populosos
de cada um dos 26 estados brasileiros.

 A) Imprima a média da população dos 3 municipios de cada estado.
 B) Considerando que a Segunda coluna contém sempre a população da capital
    do estado, calcular a média da população das capitais dos 26 estados.
 C) O número do município mais populoso e o numero do estado a que ele pertence, considerando que não houve empate."""

estados = [['Acre'],['Alagoas'],['Amapá'],['Amazonas'],
['Bahia'],['Ceará'],['Distrito Federal'],['Espirito Santo'],
['Goiás'],['Maranhão'],['Mato Grosso'],['Mato Grosso do Sul'],
['Minas Gerais'],['Pará'],['Paraíba'],['Paraná'],['Pernambuco'],
['Rio de Janeiro'],['Rio Grande do Norte'],['Rio Grande do Sul'],
['Rondônia'],['Roraima'],['Santa Catarina'],['São Paulo'],['Sergipe'],
['Tocantins']]

medias = []
media = 0
maior = 0
maior_municipio = 0
maior_estado = 0
media_capital = 0
continuar = 's'
i = 0

while continuar == 'S' or continuar == 's' or continuar == 'Sim' or continuar == 'sim':
    print(estados[i][0])
    pop1 = int(input('Quantidade de pessoas: '))
    estados[i].append(pop1)
    media = media + pop1
    media_capital = media_capital + pop1
    if pop1 > maior:
        municipio = input('Digite o nome do municipio: ')
        maior = pop1
        maior_municipio = municipio
        maior_estado = estados[i][0]
    pop2 = int(input('Quantidade de pessoas: '))
    estados[i].append(pop2)
    media = media + pop2
    pop3 = int(input('Quantidade de pessoas: '))
    estados[i].append(pop3)
    media = media + pop3
    media = media / 3
    medias.append(media)

    i = i + 1
    continuar = input('Deseja continuar?: ')

media_das_capitais = media_capital / i

print(estados)
print('Médias de cada estado:',medias)
print('Estado com o municipio com mais Habitantes:',maior_estado)
print('Municipio com mais Habitantes:',maior_municipio)
print('Habitantes:',maior)
print('A média dos municipios com mais habitantes de cada estado do Brasil:',media_das_capitais)

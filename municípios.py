"""Faça um programa que leia os dados e preencha uma lista cujo conteúdo é a população dos 3 municípios
mais populosos de cada um dos 26 estados brasileiros.
    Determine e imprima:
        a. imprima a média da população dos 3 municípios de cada estado.
        b. considerando que a 2ª coluna (1) contém sempre a população da capital do estado, calcular a média da
        população das capitais dos 26 estados;
        c. o número do município (coluna) mais populoso e o nome do estado a que ele pertence, considerando que
        não houve empate."""

estados = []
media = []
populacao=[]
municipio=[]

i = 0

while i < 27:
    AC=[(int(input('RIO BRANCO:')))
        (int(input('CRUZEIRO DO SUL:')))
        (int(input('SENA MADUREIRA:')))]

    AL=[(int(input('MACEIÓ:')))
        (int(input('ARAPIRACA')))
        (int(input('RIO LARGO')))]

    AP=[(int(input('MACAPÁ:')))
        (int(input('SANTANA:')))
        (int(input('LARANJAL DO JARI:')))]

    AM=[(int(input('MANAUS:')))
        (int(input('PARITINS:')))
        (int(input('ITACOATIARA:')))]

    BA=[(int(input('SALVADOR:')))
        (int(input('FEIRA DE SANTANA:')))
        (int(input('VITÓRIA DA CONQUISTA:')))]

    CE=[(int(input('FORTALEZA:')))
        (int(input('CAUACAIA:')))
        (int(input('JUAZEIRO DO NORTE:')))]

    DF=[(int(input('BRASÍLIA')))]

    ES=[(int(input('SERRA:')))
        (int(input('VILA VELHA:')))
        (int(input('CARIACICA:')))]

    GO=[(int(input('GOIÂNIA:')))
        (int(input('APARECIDA DE GOIÂNIA:')))
        (int(input('ANÁPOLIS:')))]

    MA=[(int(input('SÃO LUÍS:')))
        (int(input('IMPERATRIZ:')))
        (int(input('S. JOSÉ DO RIBAMAR:')))]

    MT=[(int(input('CUIABÁ:')))
        (int(input('VÁRZEA GRANDE:')))
        (int(input('RONDONÓPOLIS:')))]

    MS=[(int(input('CAMPO GRANDE:')))
        (int(input('DOURADOS:')))
        (int(input('TRÊS LAGOAS:')))]

    MG=[(int(input('BELO HORIZONTE:')))
        (int(input('UBERLÂNDIA:')))
        (int(input('CONTAGEM:')))]

    PA=[(int(input('BELÉM:')))
        (int(input('ANANINDEUA:')))
        (int(input('SANTARÉM:')))]

    PB=[(int(input('JOÃO PESSOA:')))
        (int(input('CAMPINA GRANDE:')))
        (int(input('SANTA RITA:')))]

    PR=[(int(input('CURITIBA:')))
        (int(input('LONDRINA:')))
        (int(input('MARINGÁ:')))]

    PE=[(int(input('RECIFE:')))
        (int(input('JABOATÃO:')))
        (int(input('OLINDA:')))]

    PI=[(int(input('TERESINA:')))
        (int(input('PARNAÍBA:')))
        (int(input('PICOS:')))]

    RJ=[(int(input('RIO DE JANEIRO:')))
        (int(input('SÃO GONÇALO:')))
        (int(input('DUQUE DE CAXIAS:')))]

    RN=[(int(input('NATAL:')))
        (int(input('MOSSORÓ:')))
        (int(input('PARNAMIRIM:')))]

    RS=[(int(input('PORTO ALEGRE:')))
        (int(input('CAXIAS DO SUL:')))
        (int(input('PELOTAS:')))]

    RO=[(int(input('PORTO VELHO:')))
        (int(input('JI-PARANÁ:')))
        (int(input('ARIQUEMES:')))]

    RR=[(int(input('BOA VISTA:')))
        (int(input('RORAINÓPOLIS:')))
        (int(input('CARACARAÍ:')))]

    SC=[(int(input('JOINVILLE:')))
        (int(input('FLORIANÓPOLIS:')))
        (int(input('BLUMENAU:')))]

    SP=[(int(input('SÃO PAULO:')))
        (int(input('GUARULHOS:')))
        (int(input('CAMPINAS:')))]

    SE=[(int(input('ARACAJU:')))
        (int(input('NOSSA S.ª DO SOCORRO:')))
        (int(input('LAGARTO:')))]

    TO=[(int(input('PALMAS:')))
        (int(input('ARAGUAÍNA:')))
        (int(input('GURUPI:')))]

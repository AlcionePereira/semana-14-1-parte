#Leia um dia e um mês como números inteiros distintos e informe as cidades
# que fazem aniversário nessa data. Veja o exemplo para o dia 9 e mês 2: CIDADES
# QUE FAZEM ANIVERSÁRIO EM 9 DE FEVEREIRO: São Miguel do Passa Quatro(GO)
# Centralina(MG) Itaporanga(PB) ...






def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado


cidades = carrega_cidades()

dia = int(input('Digite um dia: ').strip())
mes = int(input('Digite um número para o mês: ').strip())
meses=('JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL',
       'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO',
       'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO')


print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE {meses[mes-1]}:')
for c in cidades:
    if c[3]==dia and c[4]==mes:
        print(f'{c[2]}({c[0]})')

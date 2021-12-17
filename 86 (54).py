# Leia um mês e uma população. Mostre as cidades com população maior que o
# valor lido fazem aniversário no mês informado. Veja o exemplo para o mês com
# valor 4 e 50000 para a população: CIDADES COM MAIS DE 50000 HABITANTES E
# ANIVERSÁRIO EM ABRIL: Penedo(AL) tem 59020 habitantes e faz aniversário em 12 de abril.
# Itacoatiara(AM) tem 84676 habitantes e faz aniversário em 25 de abril. Araci(BA)
# tem 51912 habitantes e faz aniversário em 7 de abril. Fortaleza(CE) tem 2431415
# habitantes e faz aniversário em 13 de abril. ...
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
mes = int(input().strip())
populacao = int(input().strip())

mess = ('JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO',
       'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO')
meses=('janeiro', 'fevereiro', 'março', 'abril',
       'maio', 'junho', 'julho', 'agosto', 'setembro',
       'outubro', 'novembro', 'dezembro')

print(f'CIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM {mess[mes-1]}:')

for i in cidades:
    if populacao < i[5] and mes == i[4]:
        print(f'{i[2]}({i[0]}) tem {i[5]} habitantes e faz aniversário em {i[3]} de {meses[mes-1]}.')






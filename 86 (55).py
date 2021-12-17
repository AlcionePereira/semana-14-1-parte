# Leia uma população e informe as cidades com população maior que o valor lido.
#Veja o exemplo: Veja o exemplo para a leitura de 50000 para a população:
#CIDADES COM MAIS DE 50000 HABITANTES: IBGE: 120040 - Rio Branco(AC) -
#POPULAÇÃO: 290639 IBGE: 270030 - Arapiraca(AL) - POPULAÇÃO: 202398
#IBGE: 270040 - Atalaia(AL) - POPULAÇÃO: 50323 ...

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
maior = int(input('Digite um valor: ').strip())
print(f'CIDADES COM MAIS DE {maior} HABITANTES:')

# se a população da cidade for maior que o número digitado mostrar na tela.
for i in cidades:
    if i[5] > maior:
        print(f'IBGE: {i[1]} - {i[2]}({i[0]}) - POPULAÇÃO: {i[5]}')

# Considere uma tupla que guarde temperaturas em Celsius (C) ou Fahrenheit (F)
# como um valor em duas partes: temperatura e escala. Por exemplo:
# 32,5 graus Celsius é representado como (32.5, ‘C’) e 45,2 graus Fahrenheit
# é representado como (45.2, ‘F’). Crie uma função que recebe duas temperaturas
# e retorna a mais alta. Caso as temperaturas sejam de escalas diferentes,
# a função deve fazer a conversão antes de compará-las. Faça a leitura de duas
# temperaturas, com (temperatura, escala), e mostre qual é a maior.
# Use upper() e colchetes [] para garantir a leitura correta, por exemplo:
# escala = input('Escala : ').upper()[0]

t = (float(input()),
     str(input()).upper().strip())

     
t2 = (float(input()),
      str(input()).upper().strip())

if t[1] == t2[1] and t > t2:
    print(t)
elif t[1] == t2[1] and t < t2:
    print(t2)
else:
    if t[1] != t2[1] and t[1] == 'C':
        F =  9 * t[0] / 5 + 32
        if F > t2[0]:
            print(t)
        else:
                print(t2)
    if t[1] != t2 and t[1] == 'F':
        C = (t[0] - 32) * (5/9)
        if C > t2[0]:
            print(t)
        else:
            print(t2)
        


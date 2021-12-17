#Considere uma tupla que guarde temperaturas em Celsius (C) ou Fahrenheit (F)
# como um valor em duas partes: temperatura e escala. Por exemplo:
# 32,5 graus Celsius é representado como (32.5, ‘C’) e 45,2 graus Fahrenheit
# é representado como (45.2, ‘F’). Desenvolva uma função que soma duas
# temperaturas que podem estar em Celsius ou em Fahrenheit. Se as duas
# temperaturas estiverem na mesma escala, a resposta deve estar na mesma escala.
# Se as temperaturas estiverem em escalas diferentes, a resposta deve ser dada na
# escala da segunda temperatura. Considere até 4 (quatro) casas decimais).







soma = ()

t = (float(input()),
     str(input()).upper().strip())

t2 = (float(input()),
      str(input()).upper().strip())

if t[1] == t2 [1]:
    soma = t[0] + t2[0]
    print(f"({soma}, '{t[1]}')")
    
elif t[1] != t2[1] and t[1] == 'C':
    F =  9 * t[0] / 5 + 32
    soma = F + t2[0]
    print(f"({soma}, '{t2[1]}')")
elif t[1] != t2 and t[1] == 'F':
    C = (t[0] - 32) * (5/9)
    soma = C + t2[0]
    print(f"({soma:.4f}, '{t2[1]}')")
    

//1 Menor de dois pares: Escreva uma função que retorne o menor de dois números dados se 
//ambos os números forem pares, mas retorna o maior se um dos dois for ímpar. Exemplo:

menor_de_dois_pares(2,4) --> 2
menor_de_dois_pares (2,5) --> 5

num1 = int(input('Insira um numero:'))
num2 = int(input('Insira outro numero:'))
def menor_de_dois_pares(num1,num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        if num1 < num2:
            return num1
        else:
            return num2
    else:
        if num1 > num2:
            return num1
        else:
            return num2

print(f'menor_de_dois_pares({num1}, {num2}) --> {menor_de_dois_pares(num1,num2)}')
menor_de_dois_pares(4, 7) --> 7

-------------------------------------------------------------------------------------------------------------------
//2 Mesma letra: Escreva uma função que receba uma string com duas palavras e retorne 
//True se ambas palavras começarem com a mesma letra. Exemplo:

mesma_letra('Cão covarde') -> True
mesma_letra('Vira Lata') -> False

p1 = input('Insira uma palavra:')
p2 = input('Insira outra palavra:')

l1 = list(p1)
l2 = list(p2)

def mesma_letra(l1,l2):
    if l1[0]== l2[0]:
        return True
    else:
        return False

print(f"mesma_letra('{p1} {p2}') --> {mesma_letra(l1,l2)}")
mesma_letra('murilo o muito legal') --> True

-------------------------------------------------------------------------------------------------------------------
//3 Mestre Yoda: Dada uma sentença, a função deve retornar a sentença com as palavras na 
//ordem reversa. Exemplo:

mestre_yoda('Eu estou em casa') --> 'casa em estou Eu'
mestre_yoda('Estamos prontos') --> 'prontos Estamos'

string = input('Insira uma frase:')

def mestre_yoda(string):
    palavras = string.split()
    palavras.reverse()
    yoda = ""
    for i in range(0, len(palavras) - 1):
        palavras[i] = palavras[i] + " "
    for palavra in palavras:
        yoda += palavra
    return yoda

print(f"mestre_yoda('{string}') --> '{mestre_yoda(string)}'")
mestre_yoda('que a força esteja com vc') --> 'vc com esteja força a que'

-------------------------------------------------------------------------------------------------------------------
//4 Tem 33: Faça uma função que retorne True se, dada uma lista de inteiros, houver 
//em alguma posição da lista um 3 do lado de outro 3. Exemplo:

tem_33([1,3,3]) --> True
tem_33([1,3,1,3]) --> False
tem_33([3,1,3]) --> False

lista = list()
while True:
    n = lista.append(int(input('Insira um numero:')))
    r = str(input('Quer continuar? [S/N]:'))
    if r in 'Nn':
        break

def tem_33(lista):
    for i in range(0, len(lista)):
        if lista[i] == 3:
            if i + 1 < len(lista):
                if lista[i+1] == 3:
                    return True
    return False

print(f'tem_33({lista}) --> {tem_33(lista)}')
tem_33([2, 6, 8, 0, 3, 3]) --> True

-------------------------------------------------------------------------------------------------------------------
//5 Blackjack: Faça uma função que receba 3 inteiros entre 1 e 11. Se a soma deles for menor 
//que 21, retorne o valor da soma. Se for mair do que 21 e houver um 11, subtraia 10 da soma antes de 
//apresentar o resultado. Se o valor da soma passar de 21, retorne ‘ESTOUROU’. Exemplo:

blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'ESTOUROU'
blackjack(9,9,11) --> 19

n1 = int(input('Insira um numero:'))
n2 = int(input('Insira outro numero:'))
n3 = int(input('Insira mais um numero:'))

def blackjack(n1, n2, n3):
    if (1 <= n1 <= 11) and (1 <= n2 <= 11) and (1 <= n3 <= 11):
        if n1 + n2 + n3 <= 21:
            return n1 + n2 + n3
        else:
            if n1 == 11 or n2 == 11 or n3 == 11:
                return n1 + n2 + n3 - 10
            else:
                return "ESTOUROU"
    else:
        return "Os números não estão entre 1 e 11."
    
print(f'blackjack({n1},{n2},{n3}) --> {blackjack(n1, n2, n3)}')
blackjack(1,2,3) --> 6

-------------------------------------------------------------------------------------------------------------------
//6 Espião: Escreva uma função que receba uma lista de inteiros e retorne True se 
//contém um 007 em ordem, mesmo que não contínuo. Exemplo:

espiao([1,2,4,0,0,7,5]) --> True
espiao([1,0,2,4,0,5,7]) --> True
espiao([1,7,2,4,0,5,0]) --> False

l = []
for c in range (0, 7):
    l.append(int(input('Insira um numero:')))
    
def espiao(l):
    for x in range(0, len(l)):
        if l[x] == 0 and x + 1 < len(l):
            y = x + 1
            for y in range(y, len(l)):
                if l[y] == 0 and y + 1 < len(l):
                    z = y + 1
                    for z in range(z, len(l)):
                        if l[z] == 7:
                            return True
    return False

print(f'espiao({l}) --> {espiao(l)}')
espiao([5, 0, 2, 9, 0, 5, 7]) --> True
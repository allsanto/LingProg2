//1 Defina a função soma_nat que recebe como argumento um número natural n e devolve a soma de todos os números naturais até n.
//Ex: soma_nat(5) = 15

def soma_nat(n):
    return n + soma_nat(n-1) if n > 1 else 1

print('soma_nat(5) =',soma_nat(5))
print('soma_nat(4) =',soma_nat(4))
print('soma_nat(3) =',soma_nat(3))

assert(soma_nat(5) == 15)
assert(soma_nat(4) == 10)
assert(soma_nat(3) == 8)

------------------------------------------------------------------------------------------------------------------------------------------------------
soma_nat(5) = 15
soma_nat(4) = 10
soma_nat(3) = 6
------------------------------------------------------------------------------------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-2-54bfb1292d08> in <module>
      8 assert(soma_nat(5) == 15)
      9 assert(soma_nat(4) == 10)
---> 10 assert(soma_nat(3) == 8)

AssertionError:

------------------------------------------------------------------------------------------------------------------------------------------------------
//2 Defina a função div que recebe como argumentos dois números naturais m e n e devolve o resultado da 
//divisão inteira de m por n. Neste exercício você não pode recorrer às operações aritméticas de multiplicação, 
//divisão e resto da divisão inteira.

Ex: div(7,2) = 3


def div(m, n):
    return 1 + div(m - n, n) if m >= n else 0

print('div(7,2) =',div(7,2))
print('div(12,3) =',div(12,3))
print('div(2,1) =',div(2,1))

assert(div(7,2) == 3)
assert(div(12,3) == 4)
assert(div(2,1) == 0)
div(7,2) = 3
div(12,3) = 4
div(2,1) = 2


------------------------------------------------------------------------------------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-17-e8ca27d99a30> in <module>
      8 assert(div(7,2) == 3)
      9 assert(div(12,3) == 4)
---> 10 assert(div(2,1) == 0)
     11 
     12 

AssertionError: 

------------------------------------------------------------------------------------------------------------------------------------------------------
//3 Defina a função prim_alg que recebe como argumento um número natural e devolve o primeiro algarismo (o mais significativo) na representação decimal de n.
//Ex: prim_alg(5649) = 5
//Ex: prim_alg(7) = 7


def prim_alg(n):
    return int(n) if n < 10 else prim_alg(n/10)

print('prim_alg(5649) =',prim_alg(5649))
print('prim_alg(7) =',prim_alg(7))
print('prim_alg(100) =',prim_alg(100))
print('prim_alg(23) =',prim_alg(23))

assert(prim_alg(5649) == 5)
assert(prim_alg(7) == 7)
assert(prim_alg(100) == 1)
assert(prim_alg(23) == 3)
prim_alg(5649) = 5
prim_alg(7) = 7
prim_alg(100) = 1
prim_alg(23) = 2

AssertionError                            Traceback (most recent call last)
<ipython-input-25-76a5387e2205> in <module>
     10 assert(prim_alg(7) == 7)
     11 assert(prim_alg(100) == 1)
---> 12 assert(prim_alg(23) == 3)

AssertionError: 

------------------------------------------------------------------------------------------------------------------------------------------------------
//4 Defina a função prod_lista que recebe como argumento uma lista de inteiros e devolve o produto dos seus elementos.
//Ex: prod_lista([1,2,3,4,5,6]) = 720


def prod_lista(lista):
    return lista[len(lista) - 1] * prod_lista(lista[:-1]) if len(lista) > 0 else 1

print('prod_lista([1,2,3,4,5,6]) =',prod_lista([1,2,3,4,5,6]))
print('prod_lista([1,2,3,]) =',prod_lista([1,2,3]))
print('prod_lista([4,5,6]) =',prod_lista([4,5,6]))

assert(prod_lista([1,2,3,4,5,6]) == 720)
assert(prod_lista([1,2,3,]) == 6)
assert(prod_lista([4,5,6]) == 714)
prod_lista([1,2,3,4,5,6]) = 720
prod_lista([1,2,3,]) = 6
prod_lista([4,5,6]) = 120

AssertionError                            Traceback (most recent call last)
<ipython-input-28-fe7a1678cd71> in <module>
      8 assert(prod_lista([1,2,3,4,5,6]) == 720)
      9 assert(prod_lista([1,2,3,]) == 6)
---> 10 assert(prod_lista([4,5,6]) == 714)

AssertionError: 

------------------------------------------------------------------------------------------------------------------------------------------------------
//5 Defina a função contem_parQ que recebe como argumento uma lista de números inteiros w e devolve True se w contém um número par e False em caso contrário.
//Ex: contem_parQ([2,3,1,2,3,4]) = True
//Ex: contem_parQ([1,3,5,7]) = False


def contem_parQ(w):
    return False if len(w) == 0 or (w[len(w) - 1] % 2 != 0 and not contem_parQ(w[:-1])) else True

print('contem_parQ([2,3,1,2,3,4]) =',contem_parQ([2,3,1,2,3,4]))
print('contem_parQ([1,3,5,7]) =',contem_parQ([1,3,5,7]))
print('contem_parQ([1,3,5,7,2]) =',contem_parQ([1,3,5,7,2]))
print('contem_parQ([2,4,6,8]) =',contem_parQ([2,4,6,8]))

assert(contem_parQ([2,3,1,2,3,4]) == True)
assert(contem_parQ([1,3,5,7]) == False)
assert(contem_parQ([1,3,5,7,2]) == True)
assert(contem_parQ([2,4,6,8]) == False)
contem_parQ([2,3,1,2,3,4]) = True
contem_parQ([1,3,5,7]) = False
contem_parQ([1,3,5,7,2]) = True
contem_parQ([2,4,6,8]) = True

AssertionError                            Traceback (most recent call last)
<ipython-input-9-9a7ab5299767> in <module>
     10 assert(contem_parQ([1,3,5,7]) == False)
     11 assert(contem_parQ([1,3,5,7,2]) == True)
---> 12 assert(contem_parQ([2,4,6,8]) == False)

AssertionError: 

------------------------------------------------------------------------------------------------------------------------------------------------------
//6 Defina a função todos_imparesQ que recebe como argumento uma lista de números inteiros w e devolve True se w contém apenas números ímpares e False em caso contrário.
//Ex: todos_imparesQ([1,3,5,7]) = True
//Ex: todos_imparesQ([]) = True
//Ex: todos_imparesQ([1,2,3,4,5]) = False


def todos_imparesQ(w):
    return True if len(w) == 0 or (w[len(w) - 1] % 2 != 0 and todos_imparesQ(w[:-1])) else False

print('todos_imparesQ([1,3,5,7]) =',todos_imparesQ([1,3,5,7]))
print('todos_imparesQ([]) =',todos_imparesQ([]))
print('todos_imparesQ([1,2,3,4,5]) =',todos_imparesQ([1,2,3,4,5]))
print('todos_imparesQ([1,3,5,7,9,11,13]) =',todos_imparesQ([1,3,5,7,9,11,13]))
print('todos_imparesQ([0,1,3,5,7]) =',todos_imparesQ([0,1,3,5,7]))

assert(todos_imparesQ([1,3,5,7]) == True)
assert(todos_imparesQ([]) == True)
assert(todos_imparesQ([1,2,3,4,5]) == False)
assert(todos_imparesQ([1,3,5,7,9,11,13]) == True)
assert(todos_imparesQ([0,1,3,5,7]) == True)
todos_imparesQ([1,3,5,7]) = True
todos_imparesQ([]) = True
todos_imparesQ([1,2,3,4,5]) = False
todos_imparesQ([1,3,5,7,9,11,13]) = True
todos_imparesQ([0,1,3,5,7]) = False

AssertionError                            Traceback (most recent call last)
<ipython-input-10-680839da412e> in <module>
     12 assert(todos_imparesQ([1,2,3,4,5]) == False)
     13 assert(todos_imparesQ([1,3,5,7,9,11,13]) == True)
---> 14 assert(todos_imparesQ([0,1,3,5,7]) == True)

AssertionError: 

------------------------------------------------------------------------------------------------------------------------------------------------------
//7 Defina a função pertenceQ que recebe como argumentos uma lista de números inteiros w e um número inteiro n e devolve True se n ocorre em w e False em caso contrário.
//Ex: pertenceQ([1,2,3],1) = True
//Ex: pertenceQ([1,2,3],2) = True
//Ex: pertenceQ([1,2,3],3) = True
//Ex: pertenceQ([1,2,3],4) = False


def pertenceQ(w, n):
    return not(len(w) == 0 or (w.pop() != n and not pertenceQ(w, n)))

print('pertenceQ([1,2,3],1) =',pertenceQ([1,2,3],1))
print('pertenceQ([1,2,3],2) =',pertenceQ([1,2,3],2))
print('pertenceQ([1,2,3],3) =',pertenceQ([1,2,3],3))
print('pertenceQ([1,2,3],4) =',pertenceQ([1,2,3],4))
print('pertenceQ([4,5,6],4) =',pertenceQ([4,5,6],4))
print('pertenceQ([8,9,10],4) =',pertenceQ([8,9,10],4))



assert(pertenceQ([1,2,3],1) == True)
assert(pertenceQ([1,2,3],2) == True)
assert(pertenceQ([1,2,3],3) == True)
assert(pertenceQ([1,2,3],4) == False)
assert(pertenceQ([4,5,6],4) == True)
assert(pertenceQ([8,9,10],4) == True)
pertenceQ([1,2,3],1) = True
pertenceQ([1,2,3],2) = True
pertenceQ([1,2,3],3) = True
pertenceQ([1,2,3],4) = False
pertenceQ([4,5,6],4) = True
pertenceQ([8,9,10],4) = False

AssertionError                            Traceback (most recent call last)
<ipython-input-13-a64635ed4f2a> in <module>
     16 assert(pertenceQ([1,2,3],4) == False)
     17 assert(pertenceQ([4,5,6],4) == True)
---> 18 assert(pertenceQ([8,9,10],4) == True)

AssertionError: 

------------------------------------------------------------------------------------------------------------------------------------------------------
//8 Defina a função junta que recebe como argumentos duas listas de números inteiros w1 e w2 e devolve a concatenação de w1 com w2 .
//Ex: junta([1,2,3],[4,5,6]) = [1, 2, 3, 4, 5, 6]
//Ex: junta([],[4,5,6]) = [4, 5, 6]
//Ex: junta([1,2,3],[]) = [1, 2, 3]


def junta(w1, w2):
    return w1 + junta(w2[0:1], w2[1:]) if len(w2) > 0 else w1 + w2

print('junta([1,2,3],[4,5,6]) =',junta([1,2,3],[4,5,6]))
print('junta([],[4,5,6]) =',junta([],[4,5,6]) )
print('junta([1,2,3],[]) =',junta([1,2,3],[]) )
print('junta([14,15,16],[4,5,6]) =',junta([14,15,16],[4,5,6]) )
print('junta([1,2,3],[1,2,3]) =',junta([1,2,3],[1,2,3]) )

assert(junta([1,2,3],[4,5,6]) == [1, 2, 3, 4, 5, 6])
assert(junta([],[4,5,6]) == [4, 5, 6])
assert(junta([1,2,3],[]) == [1, 2, 3])
assert(junta([14,15,16],[4,5,6]) == [14, 15, 16,4, 5, 6])
assert(junta([1,2,3],[1,2,3]) == [1, 2, 3])
junta([1,2,3],[4,5,6]) = [1, 2, 3, 4, 5, 6]
junta([],[4,5,6]) = [4, 5, 6]
junta([1,2,3],[]) = [1, 2, 3]
junta([14,15,16],[4,5,6]) = [14, 15, 16, 4, 5, 6]
junta([1,2,3],[1,2,3]) = [1, 2, 3, 1, 2, 3]

AssertionError                            Traceback (most recent call last)
<ipython-input-18-680315c3d392> in <module>
     12 assert(junta([1,2,3],[]) == [1, 2, 3])
     13 assert(junta([14,15,16],[4,5,6]) == [14, 15, 16,4, 5, 6])
---> 14 assert(junta([1,2,3],[1,2,3]) == [1, 2, 3])

AssertionError:

------------------------------------------------------------------------------------------------------------------------------------------------------
//9 Defina a função temPrimoQ que recebe como argumento uma lista de listas de números inteiros w e devolve True se alguma das sublistas w tem um número primo e False em caso contrário.
//Ex: temPrimoQ([[4,4,4,4],[5,4,6,7],[2,4,3]]) = True
//Ex: temPrimoQ([[4,4,4,4],[4,4,4],[],[4]]) = False


def auxTemPrimoQ(w):
    return not(len(w) == 0 or(not(( w[0] % 2 != 0 and
                                    w[0] % 3 != 0 and
                                    w[0] % 5 != 0 and
                                    w[0] % 7 != 0 and
                                    w[0] % 11 != 0) or w.pop() in [2,3,5,7,11]) and not auxTemPrimoQ(w)))

def temPrimoQ(w):    
    return not(len(w) == 0 or (not(auxTemPrimoQ(w.pop())) and not temPrimoQ(w)))

print('temPrimoQ([[4,4,4,4],[5,4,6,7],[2,4,3]]) =',temPrimoQ([[4,4,4,4],[5,4,6,7],[2,4,3]]))
print('temPrimoQ([[4,4,4,4],[4,4,4],[],[4]]) =',temPrimoQ([[4,4,4,4],[4,4,4],[],[4]]))
print('temPrimoQ([[4,4,4,4],[6,7,5,7],[1,1,1]]) =',temPrimoQ([[4,4,4,4],[6,7,5,7],[1,1,1]]))
print('temPrimoQ([[4,4,4,4],[4,4,4],[],[4]]) =',temPrimoQ([[4,4,4,4],[4,4,4],[4,4],[4]]))

assert(temPrimoQ([[4,4,4,4],[5,4,6,7],[2,4,3]]) == True)
assert(temPrimoQ([[4,4,4,4],[4,4,4],[],[4]]) == False)
assert(temPrimoQ([[4,4,4,4],[6,7,5,7],[1,1,1]]) == True)
assert(temPrimoQ([[4,4,4,4],[4,4,4],[4,4],[4]]) == True)
temPrimoQ([[4,4,4,4],[5,4,6,7],[2,4,3]]) = True
temPrimoQ([[4,4,4,4],[4,4,4],[],[4]]) = False
temPrimoQ([[4,4,4,4],[6,7,5,7],[1,1,1]]) = True
temPrimoQ([[4,4,4,4],[4,4,4],[],[4]]) = False

AssertionError                            Traceback (most recent call last)
<ipython-input-21-1a8855f6277f> in <module>
     17 assert(temPrimoQ([[4,4,4,4],[4,4,4],[],[4]]) == False)
     18 assert(temPrimoQ([[4,4,4,4],[6,7,5,7],[1,1,1]]) == True)
---> 19 assert(temPrimoQ([[4,4,4,4],[4,4,4],[4,4],[4]]) == True)

AssertionError: 

------------------------------------------------------------------------------------------------------------------------------------------------------
//10 Defina a função inverteLista que recebe como argumento uma lista w e devolve a mesma lista mas invertida.
//Ex: inverteLista([1,2,3,4,5]) = [5, 4, 3, 2, 1]
//Ex: inverteLista([])


def inverteLista(w):
    return [w[len(w) - 1]] + (inverteLista(w[:-1])) if len(w) > 0 else []

print('inverteLista([1,2,3,4,5]) =',inverteLista([1,2,3,4,5]))
print('inverteLista([]) =',inverteLista([]))
print('inverteLista([5,4,3,2,1]) =',inverteLista([5,4,3,2,1]))
print('inverteLista([73,146,219]) =',inverteLista([73,146,219]))


assert(inverteLista([1,2,3,4,5]) == [5, 4, 3, 2, 1])
assert(inverteLista([]) == [])
assert(inverteLista([5,4,3,2,1]) == [1, 2, 3, 4, 5])
assert(inverteLista([73,146,219]) == [912, 641, 37])
inverteLista([1,2,3,4,5]) = [5, 4, 3, 2, 1]
inverteLista([]) = []
inverteLista([5,4,3,2,1]) = [1, 2, 3, 4, 5]
inverteLista([73,146,219]) = [219, 146, 73]

AssertionError                            Traceback (most recent call last)
<ipython-input-24-8e2ad2bd73c1> in <module>
     11 assert(inverteLista([]) == [])
     12 assert(inverteLista([5,4,3,2,1]) == [1, 2, 3, 4, 5])
---> 13 assert(inverteLista([73,146,219]) == [912, 641, 37])

AssertionError: 
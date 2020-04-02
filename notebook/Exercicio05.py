//1 Linha: Crie a classe Linha que tem dois atributos, coordenada1 e coordenada2. Cada coordenada � 
//uma tupla que carrega duas coordenadas cartesianas (x,y) que denotam pontos do segmento de reta. 
//Fa�a m�todos que calculem o comprimento do segmento de reta e sua inclina��o.

from math import sqrt as m

p1 = int(input('Coloque o x da coordenada 1:'))
p2 = int(input('Coloque o y da coordenada 1:'))
P1 = int(input('Coloque o x da coordenada 2:'))
P2 = int(input('Coloque o y da coordenada 2:'))

class Linha:
    def __init__(self,cord1,cord2):
        self.cord1 = cord1
        self.cord2 = cord2
    
    def calculaComprimento(self,cord1,cord2):
        a,b = cord1
        c,d = cord2
        return m(((b - a)**2) + ((d - c)**2))
    
    def calculaInclinacao(self,cord1,cord2):
        a,b = cord1
        c,d = cord2
        return ((d - c)/(b - a))
    
t1 = (p1, p2)
t2 = (P1, P2)
l = Linha(t1,t2)
print('=-' * 30)
print(f'Coordenada 1 (x = {p1}) e (y = {p2})')
print(f'Coordenada 2 (x = {P1}) e (y = {P2})')
print('=-' * 30)
print(f'comprimento = ({p1} - {p2})*2 + ({P1} - {P2})*2 / 2' )
print('comprimento �: ' + str(l.calculaComprimento(t1,t2)))
print('=-' * 30)
print(f'inclinacao = ({P1} - {P2})/({p1} - {p2})')
print('inclinacao �: ' + str(l.calculaInclinacao(t1,t2)))

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Coordenada 1 (x = 2) e (y = 4)
Coordenada 2 (x = 2) e (y = 6)
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
comprimento = (2 - 4)*2 + (2 - 6)*2 / 2
comprimento �: 4.47213595499958
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
inclinacao = (2 - 6)/(2 - 4)
inclinacao �: 2.0


-------------------------------------------------------------------------------------------------------------
//2 Figuras: Crie a seguinte hierarquia de classes de figuras geom�tricas.

//a. A classe abstrata Figura deve ter o m�todo abstrato area.
//b. A classe concreta Circulo � subclasse de Figura.
//c. A classe abstrata Poligono � subclasse de Figura e deve ter os atributos base e altura .
//d. As classes concretas Triangulo, Losango, Retangulo e Quadrado s�o subclasses de Poligono. Tente criar mais uma generaliza��o aqui olhando as f�rmulas da �rea.
//e. Os pol�gonos Retangulo e Quadrado devem implementar a interface Diagonal, que deve ter um m�todo que calcula a diagonal.
//f. Crie uma classe Geometria com uma lista de Figuras com pelo menos uma figura de cada e imprima suas �reas, per�metros e diagonais.

import math

class Figura:
    
    def area(self):
        raise NotImplementedError("M�todo abstrato que deve ser implementado por uma classe filha")
        
class Circulo(Figura):
    
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return math.pi * (self.raio**2)
    
class Poligono(Figura):
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura        
    
        
class Triangulo(Poligono):
    
    def area(self):
        return (self.base * self.altura) / 2

class Losango(Poligono):
    
    def area(self):
        return (self.base * self.altura) / 2
    
class Diagonal:
    
    def diagonal(self, base, altura):
        return (base**2 + altura**2)**(1/2)
    

class Retangulo(Poligono):
    
    diagonal = Diagonal()
        
    def diagonal(self):
        return self.diagonal.diagonal(self.base, self.altura)
    
    def area(self):
        return self.base * self.altura

class Quadrado(Retangulo):
    def __init__(self, lado):
        Retangulo.__init__(self, lado, lado)

raioC = float(input('Coloque o raio do circulo:'))
baseT = float(input('Coloque a base do triangulo:'))
alturaT = float(input('Coloque a altura do triangulo:'))
baseL = float(input('Coloque a base do losango:'))
alturaL = float(input('Coloque a altura do losango:'))
baseR = float(input('Coloque a base do retangulo:'))
alturaR = float(input('Coloque a altura do retangulo:'))
ladoQ = float(input('Coloque o lado do quadrado:'))
print('=-' * 30)
        
class Geometria:
    
    def __init__(self, figuras):
        self.lista = [x for x in figuras]
        
geometria = Geometria([    
    Circulo(raioC),
    Triangulo(baseT, alturaT),
    Losango(baseL, alturaL),
    Retangulo(baseR, alturaR),
    Quadrado(ladoQ)
])


for x in geometria.lista:
    print(f'Figura: {type(x).__name__} \nArea: {x.area()}\n')


=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


Figura: Circulo 
Area: 50.26548245743669

Figura: Triangulo 
Area: 20.0

Figura: Losango 
Area: 15.0

Figura: Retangulo 
Area: 35.0

Figura: Quadrado 
Area: 4.0


-------------------------------------------------------------------------------------------------------------
//3 Jogo de Blackjack: Fa�a um joguinho simples em Python. Aqui est�o os requisitos:

//Voc� precisa criar um jogo de BlackJack (21) baseado em texto simples
//O jogo precisa ter um jogador contra um croupier automatizado.
//O jogador pode desistir ou bater.
//O jogador deve ser capaz de escolher o seu valor de aposta.
//Voc� precisa acompanhar o dinheiro total do jogador.
//Voc� precisa alertar o jogador de vit�rias, derrotas ou estouros, etc ... E o mais importante: 
//Voc� deve usar OOP e classes em alguma parte do seu jogo. Voc� n�o pode simplesmente usar fun��es no seu 
//jogo. Use classes para ajud�-lo a definir o deck e a m�o do jogador. H� muitas maneiras certas de fazer isso, 
//ent�o explore bem!

//In [2]:
//import random

class Deck:
    
    def __init__(self):
        valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        naipes = ['paus', 'copas', 'ouros', 'espadas']
        self.cartas = [[y, x] for x in naipes for y in valores]
        random.shuffle(self.cartas) 
        
    def pop_carta(self):
        return self.cartas.pop()

class MaoJogador:
    
    def __init__(self):
        self.cartas = []
        
    def adicionar_carta(self, carta):
        return self.cartas.append(carta)
    
    def get_cartas(self):
        return self.cartas
    
    def calcular_pontos(self):
        valor_das_cartas_da_mao = []
        for i, carta in enumerate(self.cartas):
            valor = carta[0]
            if valor == 'A':
                valor = 11
            elif valor in 'JQK':
                valor = 10
            valor_das_cartas_da_mao.append(int(valor))
        valor_total = sum(valor_das_cartas_da_mao)
        if valor_total > 21:
            for i, carta in enumerate(self.cartas):
                if carta == 'A':
                    valor_das_cartas_da_mao[i] = 1
        return sum(valor_das_cartas_da_mao)
            

resposta = -1
dinheiro = float(input('Digite a quantidade total de dinheiro: '))
dinheiro_inicial = dinheiro
opcao = 1
while opcao != 0 and dinheiro > 0:
    if opcao == 1:
        aposta = float(input('Digite o valor da aposta: '))
        while aposta > dinheiro:
            aposta = float(input('Digite um valor de aposta menor ou igual ao seu dinheiro: '))
            
        deck = Deck()
        dealer_hand = MaoJogador()
        mao_jogador = MaoJogador()
        
        for i in range(2):
            dealer_hand.adicionar_carta(deck.pop_carta())
            mao_jogador.adicionar_carta(deck.pop_carta())
            
        print(f'O Coupier tem a seguinte carta: {dealer_hand.get_cartas()[0]}')
        print(f'Suas cartas s�o: {mao_jogador.get_cartas()}')
        while opcao == 1:            
            opcao = int(input('\nO que deseja fazer?,\n0 - Permanecer do modo que est�,\n1 - Pedir mais uma carta\n2 - Desistir\n'))
            if opcao == 0:
                print(f'\nM�o completa do Coupier: {dealer_hand.get_cartas()}')
                dealer_hand_pontos = dealer_hand.calcular_pontos()
                mao_jogador_pontos = mao_jogador.calcular_pontos()
                if mao_jogador_pontos < dealer_hand_pontos:
                    mensagem = 'Voc� perdeu, o'
                    dinheiro -= aposta
                elif mao_jogador_pontos > dealer_hand_pontos:
                    mensagem = 'Voc� ganhou! O'
                    dinheiro += aposta
                else:
                    mensagem = 'Empate. O'
                print(mensagem, f'dealer tinha {dealer_hand_pontos} pontos e voc� tinha {mao_jogador_pontos} pontos')
            elif opcao == 1:
              mao_jogador.adicionar_carta(deck.pop_carta())
              pontuacao = mao_jogador.calcular_pontos()
              print(f'\nSua m�o: {mao_jogador.get_cartas()}')
              print(f'Pontua��o: {pontuacao}')
              if pontuacao > 21:
                print(f'Voce estourou com {pontuacao} pontos')
                dinheiro -= aposta
                opcao = 0
            elif opcao == 2:
              dinheiro -= aposta/2         
    elif opcao == 2:
        dinheiro += float(input('Digite o valor que deseja acrescentar: '))
        
    print(f'\nDinheiro atual: R${dinheiro}')
    opcao = int(input('\nO que deseja fazer?\n1 - Jogar mais uma\n2- Colocar mais dinheiro\n0 - Sair\n'))
    
                  
                  
                  
print(f'Voc� come�ou com R${dinheiro_inicial} e terminou com R${dinheiro}, sendo assim seu lucro foi de R${dinheiro - dinheiro_inicial}')


O Coupier tem a seguinte carta: ['10', 'espadas']
Suas cartas s�o: [['K', 'copas'], ['2', 'copas']]
M�o completa do Coupier: [['10', 'espadas'], ['6', 'copas']]
Voc� perdeu, o dealer tinha 16 pontos e voc� tinha 12 pontos

Dinheiro atual: R$240.0
Dinheiro atual: R$340.0
O Coupier tem a seguinte carta: ['3', 'paus']
Suas cartas s�o: [['6', 'ouros'], ['Q', 'paus']]
Sua m�o: [['6', 'ouros'], ['Q', 'paus'], ['5', 'espadas']]
Pontua��o: 21
M�o completa do Coupier: [['3', 'paus'], ['10', 'espadas']]
Voc� ganhou! O dealer tinha 13 pontos e voc� tinha 21 pontos

Dinheiro atual: R$440.0
Voc� come�ou com R$250.0 e terminou com R$440.0, sendo assim seu lucro foi de R$190.0
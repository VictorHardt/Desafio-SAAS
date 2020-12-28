class Operacoes:  
    def __init__(self, valor_100, valor_50, valor_20, valor_10):
        self.valor_100 = valor_100
        self.valor_50 = valor_50
        self.valor_20 = valor_20
        self.valor_10 = valor_10
        
    def saldo(self):
        print("Número de notas de 100:", self.valor_100)
        print("Número de notas de 50:", self.valor_50)
        print("Número de notas de 20:", self.valor_20)
        print("Número de notas de 10:", self.valor_10)
        print("Valor total no caixa:", 100*self.valor_100 + 50*self.valor_50 + 20*self.valor_20 + 10*self.valor_10)
    
    def deposito(self):
        self.valor_100 += int(input("Quantidade notas 100: "))
        self.valor_50 += int(input("Quantidade notas 50: "))
        self.valor_20 += int(input("Quantidade notas 20: "))
        self.valor_10 += int(input("Quantidade notas 10: "))
        
    def saque(self):        
        lista_cedulas = []
        lista_cedulas_atual = []
        
        lista_cedulas_atual.append(100)
        lista_cedulas_atual.append(self.valor_100)
        lista_cedulas.append(lista_cedulas_atual)
        lista_cedulas_atual = []
        
        lista_cedulas_atual.append(50)
        lista_cedulas_atual.append(self.valor_50)
        lista_cedulas.append(lista_cedulas_atual)
        lista_cedulas_atual = []
        
        lista_cedulas_atual.append(20)
        lista_cedulas_atual.append(self.valor_20)
        lista_cedulas.append(lista_cedulas_atual)
        lista_cedulas_atual = []
        
        lista_cedulas_atual.append(10)
        lista_cedulas_atual.append(self.valor_10)
        lista_cedulas.append(lista_cedulas_atual)
        lista_cedulas_atual = []
        
        valor_saque = int(input("Insira o valor do saque: R$"))
        valor_total_caixa = 100*self.valor_100 + 50*self.valor_50 + 20*self.valor_20 + 10*self.valor_10
        
        if valor_saque > valor_total_caixa:
            print("O valor de saque solicitado não está disponível no caixa. Valor total disponível no caixa: R$", valor_total_caixa)
        
        else:
            for i in lista_cedulas:
                notas_usadas = 0
                while valor_saque >= i[0] and notas_usadas < i[1]:
                    notas_usadas += 1
                    valor_saque = valor_saque - i[0]
                    
                if i[0] == 100:
                    notas_100_usadas = notas_usadas
                    
                if i[0] == 50:
                    notas_50_usadas = notas_usadas
                    
                if i[0] == 20:
                    notas_20_usadas = notas_usadas
                    
                if i[0] == 10:
                    notas_10_usadas = notas_usadas
                    
            if valor_saque != 0:
                print("Não existem notas suficientes em caixa para realizar este saque. Operação rejeitada")
                
            else:
                self.valor_100 -= notas_100_usadas
                self.valor_50 -= notas_50_usadas
                self.valor_20 -= notas_20_usadas
                self.valor_10 -= notas_10_usadas
                print("Quantidade de notas de 100 sacadas:", notas_100_usadas)
                print("Quantidade de notas de 50 sacadas:", notas_50_usadas)
                print("Quantidade de notas de 20 sacadas:", notas_20_usadas)
                print("Quantidade de notas de 10 sacadas:", notas_10_usadas)
                print("Valor total sacado: R$", 100*notas_100_usadas + 50*notas_50_usadas + 20*notas_20_usadas + 10*notas_10_usadas)
                print("Operação realizada com sucesso")
class Carteira:
    def __init__(self):
        self.saldo = 0
    
    def verificar_saldo(self):
        return self.saldo
    
    def adicionar_dinheiro(self):
        quantidade = float(input("Digite a quantidade de dinheiro que deseja adicionar: "))
        self.saldo += quantidade
        return f"Adicionado {quantidade} à carteira. Saldo atual: {self.saldo}"

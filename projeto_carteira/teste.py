from carteira.carteira import Carteira
from interface.interface import exibir_menu_principal, exibir_saldo

if __name__ == "__main__":
    carteira_usuario = Carteira()
    
    while True:
        exibir_menu_principal()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            saldo_atual = carteira_usuario.verificar_saldo()
            exibir_saldo(saldo_atual)
        elif escolha == "2":
            carteira_usuario.adicionar_dinheiro()
        elif escolha == "3":
            print("Obrigado por usar a carteira!")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

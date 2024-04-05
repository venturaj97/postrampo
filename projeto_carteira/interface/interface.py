import tkinter as tk
from tkinter import messagebox, simpledialog
from carteira.carteira import Carteira

# Criar instância da carteira fora das funções para manter os dados
carteira = Carteira()

def exibir_saldo():
    saldo_atual = carteira.verificar_saldo()
    messagebox.showinfo("Saldo", f"Seu saldo atual é: {saldo_atual}")

def adicionar_dinheiro():
    try:
        quantidade = float(simpledialog.askstring("Adicionar Dinheiro", "Digite a quantidade de dinheiro que deseja adicionar:"))
        carteira.adicionar_dinheiro(quantidade)  # Adicionar dinheiro à instância da carteira
        exibir_saldo()
    except ValueError:
        messagebox.showerror("Erro", "Valor inválido.")

def tela_de_entrada():
    def verificar_saldo():
        exibir_saldo()

    def abrir_adicionar_dinheiro():
        adicionar_dinheiro()

    def sair():
        janela.destroy()

    janela = tk.Tk()
    janela.title("Bem-vindo!")

    # Texto de boas-vindas
    boas_vindas_texto = """
    Bem-vindo ao Sistema de Carteira!

    Escolha uma das opções abaixo:
    """

    label_boas_vindas = tk.Label(janela, text=boas_vindas_texto)
    label_boas_vindas.pack()

    # Botões de opção
    btn_verificar_saldo = tk.Button(janela, text="Verificar Saldo", command=verificar_saldo)
    btn_verificar_saldo.pack()

    btn_adicionar_dinheiro = tk.Button(janela, text="Adicionar Dinheiro", command=abrir_adicionar_dinheiro)
    btn_adicionar_dinheiro.pack()

    btn_sair = tk.Button(janela, text="Sair", command=sair)
    btn_sair.pack()

    janela.mainloop()
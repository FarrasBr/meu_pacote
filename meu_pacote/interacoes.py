# Importações:
import tkinter as tk
from tkinter import simpledialog, filedialog
import os

# Terminal

def texto_terminal(mensagem="Digite algo: "):
    # Caixa de texto
    resposta = input(mensagem)
    return resposta

# Tkinter:

def texto_tkinter(titulo="Entrada", mensagem="Digite algo:"):
    # abre uma janela de texto
    root = tk.Tk()
    root.withdraw()
    return simpledialog.askstring(titulo, mensagem)

def selecionar_arquivo(titulo="Escolha um arquivo"):
    # seleciona um arquivo qualquer
    root = tk.Tk()
    root.withdraw()
    caminho_arquivo = filedialog.askopenfilename(title=titulo)
    nome_arquivo = os.path.basename(caminho_arquivo)
    # Mostra o caminho do arquivo selecionado
    if caminho_arquivo:
        print(f"Arquivo selecionado: {nome_arquivo}")
        print(f"Arquivo selecionado: {caminho_arquivo}")
    else:
        print("Nenhum arquivo foi selecionado.")
    return caminho_arquivo, nome_arquivo
# Como utilizar:

1. Importe os arquivos de "meu_pacote":
    from meu_pacote
2. Importe as funções
    import texto_terminal, etc ...
3. Final:
    from meu_pacote import texto_terminal (EXEMPLO)


# Funções em cada arquivo:

interações.py:
    texto_terminal-> Possibilita escrever no terminal.
    texto_tkinter-> Possibilita escrever em uma janela separada (nova)
    selecionar_arquivo-> Permite a seleção de arquvos (grava o caminho e abre uma janela)

geral.py:
    esperar_tecla-> Espera que uma tecla seja pressiona (Padrão=num lock)
    verificar_janela-> Verifica se uma janela ainda está aberta
    contar_arquivos-> Conta a quantidade de arquivos em uma pasta qualquer
    comandos_cmd-> Roda comandos diretamente no cmd
    executavel-> Cria arquivos executaveis

selenium.py:
    digitar-> Digita qualquer texto no selenium (informar: xpaht ou classe, texto e enter)
    esperar-> Espera que algo seja visivel  (informar: xpaht ou classe)
    clikar-> Clika em um botão (informar: xpaht ou classe ou movex)

# Alterações: 

Caso nescessario, é possivel add ou retirar funções

add-> adicione a função ao arquivo desejado, e inclua a mesma em "__init__.py" 
    exemplo: from .selenium import digitar, esperar, clikar, NOVA_FUNÇÃO

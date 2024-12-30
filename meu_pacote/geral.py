# Importações:
import keyboard as kb
import pygetwindow as gw
import time
import os
import subprocess
import shutil

# funções:

def esperar_tecla(tecla="num lock"):
    # Espera um clique, ou finaliza por padrão
    print(f"Esperando o clique ({tecla})")
    while True:
        if kb.read_key() == tecla:
            print(f"A tecla: {tecla} foi pressionada!")
            print("Encerrando espera!")
            break
        else:
            print(kb.read_key())

def verificar_janela(Titulo):
    # Espera uma janela se fechar
    try:
        while True:
            # Verificar se a janela do prompt está aberta
            janela_prompt = gw.getWindowsWithTitle(Titulo)
            
            if janela_prompt:
                print("Em andamento.")
            else:
                print("concluído.")
                break
            time.sleep(1)
        return True

    except Exception as e:
        # Lidar com possíveis erros durante a execução
        print(f"Erro ao verificar conclusão da digitalização: {e}")
        return False

def contar_arquivos(pasta):
    # Lista todos os itens na pasta
    itens = os.listdir(pasta)

    # Filtra apenas os arquivos (exclui diretórios)
    arquivos = [item for item in itens if os.path.isfile(os.path.join(pasta, item))]
    
    # Conta os arquivos
    quantidade = len(arquivos)
    
    return quantidade

def comandos_cmd(comandos):

    # Abrir um processo CMD
    process = subprocess.Popen("cmd", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

    # Enviar os comandos ao CMD
    for comando in comandos:
        process.stdin.write(comando + "\n")

    # Finalizar a interação com o CMD
    process.stdin.write("exit\n")
    process.stdin.close()

    # Capturar a saída
    output, errors = process.communicate()

    # Exibir resultados
    print("Saída do CMD:")
    print(output)

    if errors:
        print("Erros:")
        print(errors)

def executavel(nome, janela):

    janela = None
    nome = "instalador"

    os.system("python -m venv ambiente_v")
    os.system(".\ambiente_v\Scripts\activate")

    # Bibliotecas:
    os.system("pip install pipreqs")
    os.system(f"pipreqs .")
    os.system("pip install -r requirements.txt")
    os.system("pip install pyinstaller")
    if janela == "yes" or "y" or "Y":
        os.system(f"pyinstaller --onefile -w {nome}.py")
    else:
        os.system(f"pyinstaller --onefile {nome}.py")

    #excluindo pasta
    os.system("deactivate")
    shutil.rmtree("build")
    shutil.rmtree("ambiente_v")
    os.remove(f"{nome}.spec")

    print("Arquivo executável criado com sucesso" * 10)
# import random
from time import sleep
import sqlite3
import sys

loginn = ''

# Estabelecer conexão com o banco de dados
conexao = sqlite3.connect("cadastros.db")

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

# Cria tabela cadastros
cursor.execute("""
CREATE TABLE IF NOT EXISTS cadastros (
    login TEXT NOT NULL,
    senha TEXT NOT NULL
)
""")

# Salvar as alterações no banco de dados
conexao.commit()

def validar_login(c_login):
    conexao = sqlite3.connect('cadastros.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM cadastros WHERE login = ?
    """, (c_login,))

    resultado = cursor.fetchone()
    conexao.close()

    return resultado is not None  # Retorna True se login for encontrado

def validar_senha(c_login, c_senha):
    conexao = sqlite3.connect('cadastros.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM cadastros WHERE login = ? AND senha = ?
    """, (c_login, c_senha))

    resultado = cursor.fetchone()
    conexao.close()

    return resultado is not None  # Retorna True se login e senha forem encontrados

def deletaLogin(c_login):
    conexao = sqlite3.connect('cadastros.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM cadastros WHERE login = ?", (c_login,))
    resultado = cursor.fetchone()

    if resultado:
        cursor.execute("DELETE FROM cadastros WHERE login = ?", (c_login,))
        conexao.commit()  # Salvar as alterações
        print(f"Usuário '{c_login}' deletado com sucesso.")
    else:
        print(f"Usuário '{c_login}' não encontrado.")

    conexao.close()

def opSair():
    return 

def esp():
    print('\n')

while True:
    sleep(1)
    print('-/'*10, " Menu Inicial ", '-/'*10, f"\n |*||*| Bem-vindo {loginn} |*||*| \n 1- Cadastrar no sistema \n 2- Logar no sistema \n 3- Deletar cadastro \n 4- Ver usuarios cadastrados\n 5- Sair do sistema")

    p1 = input('Digite a opção selecionada:')

    while not p1.isdigit():
        print('A opção digitada não é um número.')
        p1 = input('Digite a opção selecionada:')

    p1 = int(p1)

    esp()
    print("Digite 0 ou ç para sair de qualquer opção e voltar para o MENU")
    esp()
    sleep(2)

    if p1 == 1:
        sleep(1.5)
        print("Bem-vindo ao cadastro do sistema\n")

        while True:
            c_login = input("Digite seu nome de login: ").upper().strip()

            if c_login == 'Ç':
                break

            if validar_login(c_login):
                print("Login já existente, tente novamente.")
            else:
                while True:
                    c_senha = input('Digite sua senha de login (Apenas números): ')
                    if c_senha == 0:
                        break

                    if c_senha.isdigit():
                        sn = input(f'Sua senha é {c_senha}\nDeseja confirmá-la?\n1-Sim\n2-Não\n')

                        if sn.isdigit() and int(sn) == 1:
                            print("Cadastro feito com sucesso!")
                            break
                    else:
                        print("Senha deve ser numérica.")

                # Inserir o novo usuário na tabela após confirmação
                conexao = sqlite3.connect('cadastros.db')
                cursor = conexao.cursor()

                cursor.execute("""
                INSERT INTO cadastros (login, senha)
                VALUES (?, ?)
                """, (c_login, c_senha))

                conexao.commit()
                conexao.close()

                print(f' Login: {c_login}\n Senha: {c_senha}')

                break

    elif p1 == 2:
        while True:
            c_login = input("Digite seu login: ").upper().strip()

            if c_login == 'Ç':
                break

            if validar_login(c_login):
                while True:
                    c_senha = input("Digite sua senha: ").strip()

                    if int(c_senha) == 0:
                        break

                    if validar_senha(c_login, c_senha):
                        print("Login realizado com sucesso!")
                        loginn = c_login

                        #COLOCAR O SISTEMA DE PRODUTOS
                        ##
                        #
                        #
                        #
                        #
                        #
                        #
                        #
                        #
                        break
                    else:
                        print("Senha incorreta, tente novamente.")
                        sleep(1)
                break
            else:
                print("Login incorreto, tente novamente.")
                sleep(1)

    elif p1 == 3:
        try:
            conexao = sqlite3.connect('cadastros.db')
            cursor = conexao.cursor()

            cursor.execute("SELECT * FROM cadastros WHERE login = ?", (c_login,))
            loginadm = cursor.fetchone()

            if loginadm and loginadm[0] == 'ADMIN':
                cursor.execute("SELECT * FROM cadastros;")

                usuarios = cursor.fetchall()

                for usuario in usuarios:
                    print(usuario)

                lDeletar = input('Qual login você deseja deletar? ').upper().strip()

                if lDeletar == 'Ç':
                    break

                simNao = input(f'Deseja mesmo deletar o usuário {lDeletar}? \n 1 - SIM \n 2 - NÃO\n')

                if int(simNao) == 0:
                    break

                if simNao.isdigit() and int(simNao) == 1:
                    deletaLogin(lDeletar)
                else:
                    print("Operação cancelada!")
            else:
                print("Você não tem permissão para deletar usuarios.")
        except NameError:
            print("Você deve logar primeiro para poder acessar essa opção")

    elif p1 == 4:
        conexao = sqlite3.connect('cadastros.db')
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM cadastros;")

        usuarios = cursor.fetchall()

        for usuario in usuarios:
            login, senha = usuario
            senha_mascarada = '*' * len(senha)  # Substitui a senha por asteriscos
            print(f"Login: {login}, Senha: {senha_mascarada}")
            sleep(3)
        conexao.close()

    elif p1 == 5:
        sys.exit()

    elif p1 > 5 or p1 < 1:
        print("Opção Invalida!")
    

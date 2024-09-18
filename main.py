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

def deletaProduto(p_id):
    conexao = sqlite3.connect('cadastros.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produtos WHERE id = ?", (p_id,))
    resultado = cursor.fetchone()

    if resultado:
        cursor.execute("DELETE FROM produtos WHERE id = ?", (p_id,))
        conexao.commit()  
        print(f"Produto '{p_id}' deletado com sucesso.")
    else:
        print(f"Produto '{p_id}' não encontrado.")

    conexao.close()

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

                        sleep(1.5)

                        # Estabelecer conexão com o banco de dados
                        conexao = sqlite3.connect("cadastros.db")

                        # Criar um cursor para executar comandos SQL
                        cursor = conexao.cursor()

                        # Cria tabela cadastros
                        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS produtos (
                            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                            nome TEXT NOT NULL,
                            preco FLOAT NOT NULL,
                            qtd INT DEFAULT 0 NOT NULL
                        )
                        """)

                        # Salvar as alterações no banco de dados
                        conexao.commit()

                        while True:
                            print('-/'*10, " Menu de Produtos ", '-/'*10, "\n 1- Cadastrar produto \n 2- Modificar produtos \n 3- Deletar Produtos \n 4- Ver produtos\n 5- Sair do sistema")
                            
                            p2 = input('Digite a opção selecionada:')

                            while not p2.isdigit():
                                print('A opção digitada não é um número.')
                                p2 = input('Digite a opção selecionada:')

                            p2 = int(p2)

                            esp()
                            print("Digite 0 ou ç para sair de qualquer opção e voltar para o MENU")
                            esp()
                            sleep(2)

                            if p2 == 1:
                                conexao = sqlite3.connect('cadastros.db')
                                cursor = conexao.cursor()

                                p_nome = str(input('Digite o nome do produto a ser inserido:')).upper().strip()

                                if p_nome == 'Ç':
                                    break

                                while True:
                                    if p_nome.isalpha():
                                        break
                                    else:
                                        print('Nome invalido!')
                                        sleep(1)
                                        p_nome = str(input('Digite o nome do produto a ser inserido:')).upper().strip()

                                p_preco = float(input('Digite o preço do produto:'))

                                if p_preco == '0':
                                    break

                                p_qtd= input('Digite a quantidade inserida no estoque:')

                                if p_qtd == '0':
                                    break

                                while True:
                                    if p_qtd.isdigit():
                                        p_qtd = int(p_qtd)
                                        break
                                    else: 
                                        print('Numero invalido')
                                        sleep(1)
                                        p_qtd= input('Digite a quantidade inserida no estoque:')

                                cursor.execute("""
                                INSERT INTO produtos (nome, preco,qtd)
                                VALUES (?, ?,?)
                                """, (p_nome, p_preco,p_qtd))

                                conexao.commit()
                                
                                print(f' O produto inserido foi {p_nome}, com o preço {p_preco} e na quantidade {p_qtd} ')  

                                conexao.close()

                            elif p2 == 2:
                                # MODIFICAR PRODUTOS 
                                conexao = sqlite3.connect('cadastros.db')
                                cursor = conexao.cursor()
                                p_id = input('Digite o id do produto a ser modificado: ').strip()

                                if p_id == '0':
                                    break

                                if not p_id.isdigit():
                                    print("ID inválido!")
                                else:
                                    p_id = int(p_id)
                                    

                                p_nomen = str(input('Digite o novo nome do produto:')).upper().strip()

                                if p_nomen == 'Ç':
                                    break

                                while not p_nomen.isalpha():
                                    print('Nome inválido!')
                                    p_nomen = input('Digite o nome do produto a ser modificado: ').upper().strip()
                                
                                try:
                                    p_precon = float(input('Digite o novo preço do produto(COM . AO INVÉS DE ,): ').strip())
                                except ValueError:
                                    print("Preço inválido!")
                                    p_precon = 0.0  # Valor padrão em caso de erro

                                if p_precon == 0:
                                    break

                                p_qtdn = input('Digite a nova quantidade inserida no estoque: ').strip()

                                if p_qtdn == '0':
                                    break

                                while not p_qtdn.isdigit():
                                    print('Quantidade inválida!')
                                    p_qtdn = input('Digite a nova quantidade inserida no estoque: ').strip()

                                p_qtdn = int(p_qtdn)  

                                cursor.execute("SELECT * FROM produtos WHERE id = ?", (p_id,))

                                id_prod = cursor.fetchone()

                                if id_prod:
                                    cursor.execute("UPDATE produtos SET nome = ?, preco = ?,qtd = ? WHERE id = ?",(p_nomen,p_precon,p_qtdn,p_id))
                                    conexao.commit()
                                    print("Produto atualizado")
                                else:
                                    print('Produto não encontrado')

                                conexao.close()
                                
                            elif p2 == 3:
                                conexao = sqlite3.connect('cadastros.db')
                                cursor = conexao.cursor()

                                cursor.execute("SELECT * FROM produtos;")

                                produ = cursor.fetchall()

                                for prods in produ:
                                    print(prods)

                                pDeletar = input('Qual produto você deseja deletar?(Digite o ID) ').strip()

                                if pDeletar == '0':
                                    break

                                simNao = input(f'Deseja mesmo deletar o produto de ID {pDeletar}? \n 1 - SIM \n 2 - NÃO\n').strip()

                                if int(simNao) == 0:
                                    break

                                if simNao.isdigit() and int(simNao) == 1:
                                    deletaProduto(pDeletar)
                                    print("Produto deletado com Sucesso!")
                                else:
                                    print("Operação cancelada!")


                            elif p2 == 4:
                                conexao = sqlite3.connect("cadastros.db")

                                cursor = conexao.cursor()

                                cursor.execute("SELECT * FROM produtos;")

                                produ = cursor.fetchall()

                                for prods in produ:
                                    print(prods)

                                sleep(2.5)

                                conexao.close()

                            elif p2 == 5:
                                sys.exit()

                            elif p1 > 5 or p1 < 1:
                                print("Opção Invalida!")        
                        
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
    
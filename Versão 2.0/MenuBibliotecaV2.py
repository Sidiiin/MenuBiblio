#MenuBiblio_2.0
#I'm giving you a night call to tell you how i feel

import mysql.connector

# Conexão com o banco de dados
def conectar_banco():
    """Função para criar a conexão com o banco de dados e o cursor."""
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="biblioteca"
    )
    cursor = conexao.cursor()
    return conexao, cursor

# /\ Não precisa ir pro GIT /\

# Criar tabelas
def criar_tabelas():
    conexao, cursor = conectar_banco()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS LivrosCadastrados (
        idLivro INT AUTO_INCREMENT PRIMARY KEY,
        titulo VARCHAR(255) NOT NULL,
        autor VARCHAR(255) NOT NULL,
        disponibilidade BOOL NOT NULL
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS AlunosCadastrados (
        matricula INT AUTO_INCREMENT PRIMARY KEY,
        nomeAluno VARCHAR(255) NOT NULL
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS StatusEmprestimo (
        idEmprestimo VARCHAR(6) PRIMARY KEY,
        devolucaoEmp DATETIME
    );
    """)
    
    cursor.close()
    conexao.close()

# Agora vamos as funções

#Função para cadastrar um aluno
def cadastrar_aluno():
    """Função para cadastrar um novo aluno."""
    conexao, cursor = conectar_banco()
    
    aluno_temporario = input('Insira o nome do aluno a ser cadastrado: ')
    sql = "INSERT INTO AlunosCadastrados (nomeAluno) VALUES (%s)"
    valores = (aluno_temporario,)
    
    cursor.execute(sql, valores)
    conexao.commit()

#Função para cadastrar um livro
def cadastrar_livro():
    """Função para cadastrar um novo livro."""
    conexao, cursor = conectar_banco()
    
    livro_temporario = input('Insira o nome do livro a ser cadastrado: ')
    autor_temporario = input('Insira o nome do autor do livro a ser cadastrado: ')
    sql = "INSERT INTO livroscadastrados (titulo, autor, disponibilidade) VALUES (%s,%s,1);"
    valores = (livro_temporario,autor_temporario)
    
    cursor.execute(sql, valores)
    conexao.commit()

#Função para listar os livros
def listar_livros():
    """Função para cadastrar um novo aluno."""
    conexao, cursor = conectar_banco()
    
    sql = "SELECT * FROM livroscadastrados WHERE disponibilidade = 1"
    
    cursor.execute(sql)
    livros = cursor.fetchall()
    if livros:
        print("Livros disponíveis:")
        for livro in livros:
            print(f"Título: {livro[1]}, Escrito por {livro[2]}")
    else:
        print("Nenhum livro disponível.")
    
    cursor.close()
    conexao.close()




# Criar as tabelas para o programa
criar_tabelas()

#Menu
while True:
    print('╔══════════════════════════════════════════╗')
    print('║       Seja bem-vindo à Biblioteca        ║')
    print('╠══════════════════════════════════════════╣')
    print('║   Qual dos nossos serviços deseja usar?  ║')
    print('╠══════════════════════════════════════════╣')
    print('║ 1 - Listar livros Disponiveis            ║')
    print('║ 1 - xxxxx                                ║')
    print('║ 1 - xxxxx                                ║')
    print('║ 1 - xxxxx                                ║')
    print('╠══════════════════════════════════════════╣')
    print('║           Apenas funcionários            ║')
    print('╠══════════════════════════════════════════╣')
    print('║ 2 - Cadastrar um Livro                   ║')
    print('║ 3 - Cadastrar um Aluno                   ║')
    print('╚══════════════════════════════════════════╝')

    try:
        controle_do_menu = int(input('Escolha uma opção: '))
    except ValueError:
        print("Opção inválida! Por favor, escolha um número.")
        continue
    print('═' * 44)
    
    # Chamada das funções
    if controle_do_menu == 2:
        cadastrar_livro()
    elif controle_do_menu == 3:
        cadastrar_aluno()
    elif controle_do_menu == 1:
        listar_livros()
    else:
        print("Opção não implementada ou inválida.")
    
    if input("Digite 'v' para voltar ao menu ou qualquer outra tecla para sair: ").lower() != 'v':
        break
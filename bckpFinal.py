# Go ahead and cry little boy <--- Letra da musica que eu estava escutando no momento 0 quando começei a programar)
#datetime serve para usar data e hora do sistema como referencia para os dias
from datetime import datetime
import csv

hoje = datetime.now()
anostr = hoje.strftime("%Y")
messtr = hoje.strftime("%m")
diastr = hoje.strftime("%d")
dia = int(diastr) # variaveis declaradas de dia mês e ano
mes = int(messtr) # variaveis declaradas de dia mês e ano
ano = int(anostr) # variaveis declaradas de dia mês e ano
data_dev = [dia + 7,mes,ano] #calculo da devolução dos livros

# Alunos cadastrados
#dicionarios com as chaves nome e matricula
aluno1 = {'nome':'Sidney Fernandes','matricula':160802}
alunos_cad = [aluno1]

# Livros cadastrados
#dicionarios com as chaves autor, titulo, disponibilidade, devolução, aluno e matricula
livro1 = {'autor':'Steve Hawkins','titulo':'Breves respostas para grandes questões','Disponibilidade':'Disponivel','Devolução':data_dev,'Aluno':'  ','Matricula':' '}
livro2 = {'autor':'Galapagos Jogos', 'titulo':'Dungeons & Dragons: Livro do mestre','Disponibilidade':'Disponivel','Devolução':data_dev,'Aluno':'  ','Matricula':' '}
livro3 = {'autor':'Harlan Ellison', 'titulo':'Não tenho boca mas preciso gritar','Disponibilidade':'Disponivel','Devolução':data_dev,'Aluno':'  ','Matricula':' '}
livro4 = {'autor':'Agatha Christie', 'titulo':'Os elefantes não esquecem','Disponibilidade':'Disponivel','Devolução':data_dev,'Aluno':'  ','Matricula':' '}
livro5 = {'autor':'H.P Lovecraft', 'titulo':'O chamado de Cthulhu e outros contos','Disponibilidade':'Disponivel','Devolução':data_dev,'Aluno':'  ','Matricula':' '}
livro6 = {'autor':'Hideaki Anno', 'titulo':'NEON GENESIS EVANGELION: Capitulo 1','Disponibilidade':'Disponivel','Devolução':data_dev,'Aluno':'  ','Matricula':' '}
livros_cad = [livro1, livro2, livro3, livro4, livro5, livro6]

#Regra pro livro ficar branco quando Disponivel ou sem alunos
for livro in livros_cad:
    if livro['Disponibilidade'] == 'Disponivel':
        livro['Devolução'] = ' '
    if livro['Disponibilidade'] == 'Emprestado':
        livro['Devolução'] = data_dev #codigo para atualizar a devolução caso o livro seja pego para emprestimo

# Os titulos do relatorio
dados_relatorio = ['Livro','Situação','Devolução','Aluno','Matricula']

# Funções do menu
controle_do_menu = 0

#Função usada para pesquisar os livros dentre os cadastrados
def pesquisar_livro(livros_cad):
    while True:
        print('═' * 44)
        pesquisa = input("Digite o título do livro que deseja procurar: ").lower()
        achado = False
        for livro in livros_cad:
            if pesquisa in livro['titulo'].lower():
                print(f"Livro encontrado: {livro['titulo']} por {livro['autor']}")
                achado = True
        if not achado:
            print('═' * 44)
            print("Ainda não temos esse livro em nossa biblioteca\ncaso deseje cadastrar esse livro em nossso sistema\nvolte ao menu e selecione 'Cadastrar um livro' e faça o cadastro do livro desejado.")
        print('═' * 44)
        if input("Digite 'v' para voltar ao menu: ").lower() == 'v':
            break

#Função usada para cadastrar novos alunos no sistema
def cadastrar_aluno(alunos_cad):
    while True:
        print('═' * 44)
        alunoadd = {'nome': input('Insira o nome do aluno que deseja cadastrar: '), 'matricula': int(input('Matricula do aluno que deseja cadastrar: '))}
        alunos_cad.append(alunoadd)
        print("Aluno cadastrado com sucesso!")
        print('═' * 44)
        if input("Digite 'v' para voltar ao menu: ").lower() == 'v':
            break

#função usada para mostrar os livros cadastrados no sistema
def listar_livros(livros_cad):
    while True:
        print('═' * 44)
        print("Livros disponíveis:")
        for livro in livros_cad:
            if livro['Disponibilidade'] == 'Disponivel':
                print(f"{livro['titulo']} de {livro['autor']}")
        print('═' * 44)
        if input("Digite 'v' para voltar ao menu: ").lower() == 'v':
            break

#função usada para mostrar os alunos cadastrados no sistema
def listar_alunos_cad(alunos_cad):
    while True:
        print('═' * 44)
        for aluno in alunos_cad:
            print(f"{aluno['nome']} \nMatricula: {aluno['matricula']}\n")
        print('═' * 44)
        if input("Digite 'v' para voltar ao menu: ").lower() == 'v':
            break

#função usada para cadastrar novos livros no sistema
def cadastrar_livros(livros_cad):
    while True:
        print('═' * 44)
        livroadd = {'autor': input('Autor do livro a qual deseja cadastrar: '),
            'titulo': input('Titulo do livro a qual deseja cadastrar: '),
            'Disponibilidade':'Disponivel',
            'Devolução':' ',
            'Aluno':' ',
            'Matricula':' '}
        livros_cad.append(livroadd)
        print("Livro cadastrado com sucesso!")
        print('═' * 44)
        if input("Digite 'v' para voltar ao menu: ").lower() == 'v':
            break

#função usada para verificar se o livro desejado está disponivel
def verificar_disponibilidade_livro(livros_cad):
    while True:
        print('═' * 44)
        pesquisa = input("Digite o título do livro que deseja pegar emprestado: ").lower()
        achado = False
        for livro in livros_cad:
            if pesquisa in livro['titulo'].lower():
                print(f"Livro encontrado: {livro['titulo']} (Status: {livro['Disponibilidade']})")
                achado = True
        if not achado:
            print('Ainda não temos esse livro em nossa biblioteca')
        print('═' * 44)
        if input("Digite 'v' para voltar ao menu: ").lower() == 'v':
            break

#função usada para mudar o status do emprestimo de livros
#Essa função de mudar o status do emprestimo foi a que mais me quebrou a cabeça
def status_do_emprestimo(livros_cad, alunos_cad):
    while True:
        status_emprestimo = int(input('Você deseja:\n 1 - Pegar um livro emprestado\n 2 - Devolver um livro\n'))
        print('═' * 44)
        if status_emprestimo == 1:
            matricula_pesquisa = int(input('Digite seu número de matrícula: ')) #verificador de matricula 
            aluno_matriculado = None
            for aluno in alunos_cad:
                if aluno['matricula'] == matricula_pesquisa:
                    aluno_matriculado = aluno
                    break  
            if aluno_matriculado:
                print('═' * 44)
                print(f"Matrícula encontrada: {aluno_matriculado['nome']}")#apenas alunos matriculados podem pegar livros
                livroemp = input('Qual livro deseja pegar emprestado?: ').lower()
                livro_encontrado = False
                for livro in livros_cad:
                    if livroemp in livro['titulo'].lower():
                        livro_encontrado = True
                        if livro['Disponibilidade'] == 'Disponivel':
                            print(f"Leve o livro '{livro['titulo']}' até o bibliotecário junto com o recibo para retirada.\nTenha uma boa leitura!")
                            print('═' * 44)
                            livro['Disponibilidade'] = 'Emprestado'
                            livro['Aluno'] = aluno_matriculado['nome']
                            livro['Devolução'] = data_dev
                            livro['Matricula'] = aluno_matriculado['matricula']
                        else:
                            print(f"O livro '{livro['titulo']}' já está emprestado.")
                    if not livro_encontrado:
                        print("Livro não encontrado.")
            else:
                print('═' * 44)
                print('Não encontramos essa matrícula em nosso sistema, apenas usuários cadastrados podem pegar livros emprestados.')
                print('═' * 44)

            if input("Digite 'v' para voltar ao menu: ").lower() == 'v':
                break

        elif status_emprestimo == 2:
            devolucao = input('Qual livro você está devolvendo?: ').lower()
            livro_encontrado = False
            for livro in livros_cad:
                if devolucao in livro['titulo'].lower():
                    livro_encontrado = True
                    if livro['Disponibilidade'] == 'Emprestado':
                        livro['Disponibilidade'] = 'Disponivel'
                        livro['Aluno'] = ' '
                        livro['Devolução'] = ' '
                        livro['Matricula'] = ' '
                        print(f"Agradecemos a sua devolução!\nQual será sua próxima leitura?!")
                    else:
                        print(f"O livro '{livro['titulo']}' não está emprestado.")
            if not livro_encontrado:
                print("Livro não encontrado.")

            print('═' * 44)
            if input("Digite 'v' para voltar ao menu: ").lower() == 'v':
                break


#Função usada para gerar os relatorios da biblioteca
#Essa função de gerar relatorio foi a segunda que mais me quebrou a cabeça
def gerar_relatorio(livros_cad, dados_relatorio):
    while True:
        print('═' * 44)
        print(f'\t\t {dados_relatorio[0].ljust(35)}\t  Situação\t\t\t{dados_relatorio[2].ljust(10)}\t\t\t{dados_relatorio[3].ljust(15)}\t\t\t\t{dados_relatorio[4].ljust(10)}')
        for livro in livros_cad:
            
                

            print(livro['titulo'].ljust(35),'\t║\t\t',livro['Disponibilidade'].ljust(10),'\t║ ',str(livro['Devolução']).ljust(12),'\t║\t',livro['Aluno'].ljust(20),'\t║\t',livro['Matricula'])



        if input("Digite 'v' para voltar ao menu: ").lower() == 'v':
            break

#Funçao usada para gerar e salvar o ultimo relatorio em um arquivo csv
#Fiz de ultima hora
def salvar_o_relatorio(livros_cad, dados_relatorio):
    with open('relatorio.csv', 'w', newline='', encoding='utf-8') as arq:
        writer = csv.writer(arq)
        writer.writerow(dados_relatorio) 
        for livro in livros_cad:
            writer.writerow([
                    livro['titulo'],
                    livro['Disponibilidade'],
                    livro['Devolução'],
                    livro['Aluno'],
                    livro['Matricula']
                ])
    print('Relatório salvo como "relatorio.csv".')

while True:
    print('╔══════════════════════════════════════════╗')
    print('║       Seja bem-vindo à Biblioteca        ║')
    print('╠══════════════════════════════════════════╣')
    print('║ Qual dos nossos serviços deseja usar?    ║')
    print('╠══════════════════════════════════════════╣')
    print('║ 1 - Procurar um livro                    ║')
    print('║ 2 - Verificar se um livro está disponível║')
    print('║ 3 - Alterar o status do seu empréstimo   ║')
    print('╠══════════════════════════════════════════╣')
    print('║           Apenas funcionários            ║')
    print('╠══════════════════════════════════════════╣')
    print('║ 4 - Cadastrar um livro                   ║')
    print('║ 5 - Cadastrar um aluno                   ║')
    print('║ 6 - Lista de livros disponíveis          ║')  # Criei para debug
    print('║ 7 - Lista de alunos cadastrados          ║')  # Criei para debug
    print('║ 8 - Gerar um relatorio                   ║') 
    print('║ 9 - Salvar o ultimo relatorio            ║') 
    print('╚══════════════════════════════════════════╝')

    controle_do_menu = int(input('Escolha uma opção: '))
    print('═' * 44)

    if controle_do_menu == 11:
        break

# Pesquisa de livro (Funcionando)
    if controle_do_menu == 1:
        pesquisar_livro(livros_cad)

# Cadastro de aluno (Funcionando)
    elif controle_do_menu == 5:
        cadastrar_aluno(alunos_cad)

# Lista de livros disponiveis(Funcionando)
    elif controle_do_menu == 6:
        listar_livros(livros_cad)

# Lista de alunos cadastrados(Funcionando)
    elif controle_do_menu == 7:
        listar_alunos_cad(alunos_cad)

# Cadastro de livros(Funcionando)
    elif controle_do_menu == 4:
        cadastrar_livros(livros_cad)

# Verificação de disponibilidade (Funcionando)
    elif controle_do_menu == 2:
        verificar_disponibilidade_livro(livros_cad)

# Alteração de Status do emprestimo(Funcionando)
    elif controle_do_menu == 3:
        status_do_emprestimo(livros_cad, alunos_cad)
# Gerar um relatorio(Funcionando)
    elif controle_do_menu == 8:
        gerar_relatorio(livros_cad, dados_relatorio)
# Salvar relatorio
    elif controle_do_menu == 9:
        salvar_o_relatorio(livros_cad, dados_relatorio)
# Go ahead and cry little boy

# Livros guardados
livro1 = {'autor':'Steve Hawkins','titulo':'Breves respostas para grandes questões','Disponibilidade':'Disponivel'}
livro2 = {'autor':'Galapagos Jogos', 'titulo':'Dungeons & Dragons: Livro do mestre','Disponibilidade':'Disponivel'}
livro3 = {'autor':'Harlan Ellison', 'titulo':'Não tenho boca mas preciso gritar','Disponibilidade':'Disponivel'}
livro4 = {'autor':'Agatha Christie', 'titulo':'Os elefantes não esquecem','Disponibilidade':'Disponivel'}
livro5 = {'autor':'H.P Lovecraft', 'titulo':'O chamado de Cthulhu e outros contos','Disponibilidade':'Disponivel'}
livro6 = {'autor':'Hideaki Anno', 'titulo':'NEON GENESIS EVANGELION: Capitulo 1','Disponibilidade':'Disponivel'}
livros_cad = [livro1, livro2, livro3, livro4, livro5]

# Alunos cadastrados
aluno1 = {'nome':'Sidney Fernandes','matricula':'123546'}
alunos_cad = [aluno1]

# Menu interativo
controle_do_menu = 0
while True:
    print('╔══════════════════════════════════════════╗')
    print('║      Seja bem-vindo à Biblioteca         ║')
    print('╠══════════════════════════════════════════╣')
    print('║ Qual dos nossos serviços deseja usar?    ║')
    print('╠══════════════════════════════════════════╣')
    print('║ 1 - Procurar um livro                    ║')
    print('║ 2 - Verificar se um livro está disponível║')
    print('║ 3 - Cadastrar um livro                   ║')
    print('╠══════════════════════════════════════════╣')
    print('║       Apenas funcionários                ║')
    print('╠══════════════════════════════════════════╣')
    print('║ 4 - Cadastrar um aluno                   ║')
    print('║ 5 - Lista de livros disponíveis          ║')  # Criei para debug
    print('║ 6 - Lista de alunos cadastrados          ║')  # Criei para debug
    print('║ 7 - Alterar o status do seu empréstimo   ║')
    print('╚══════════════════════════════════════════╝')

    controle_do_menu = int(input('Escolha uma opção: '))
    print('═' * 44)

    if controle_do_menu == 9:
        break
    #Funçoes

# Pesquisa de livro (Funcionando)
    if controle_do_menu == 1:
        print('═' * 44)
        pesquisa = input("Digite o título do livro que deseja procurar: ").lower()
        achado = False
        for livro in livros_cad:
            if pesquisa in livro['titulo'].lower():
                print(f"Livro encontrado: {livro['titulo']} por {livro['autor']} (Status: {livro['Disponibilidade']})")
                achado = True
        if not achado:
            print('═' * 44)
            print("Ainda não temos esse livro em nossa biblioteca\ncaso deseja cadastrar esse livro em nossso sistema\nvolte ao menu e selecione 'Cadastrar um livro' e faça o cadastro do livro desejado.")
            print('═' * 44)
# Cadastro de aluno (Funcionando)
    if controle_do_menu == 4:
        print('═' * 44)
        alunoadd = {'nome': input('Insira o nome do aluno que deseja cadastrar: '), 'matricula': int(input('Matricula do aluno que deseja cadastrar: '))}
        alunos_cad.append(alunoadd)
        print("Aluno cadastrado com sucesso!")
        print('═' * 44)

# Lista de livros disponiveis(Funcionando)
    if controle_do_menu == 5:
        print('═' * 44)
        print("Livros disponíveis:")
        for livro in livros_cad:
            if livro['Disponibilidade'] == 'Disponivel':
                print(f"{livro['titulo']} de {livro['autor']}")

# Lista de alunos cadastrados(Funcionando)
    if controle_do_menu == 6:
        print('═' * 44)
        for aluno in alunos_cad:
            print(f"{aluno['nome']} \nMatricula: {aluno['matricula']}\n")

    # Cadastro de livros(Funcionando)
    if controle_do_menu == 3:
        print('═' * 44)
        livroadd = {'autor': input('Autor do livro a qual deseja cadastrar: '), 'titulo': input('Titulo do livro a qual deseja cadastrar: '),'Disponibilidade':'Disponivel'}
        livros_cad.append(livroadd)
        print("Livro cadastrado com sucesso!")

# Verificação de disponibilidade (em andamento)
    if controle_do_menu == 2:
        print('═' * 44)
        pesquisa = input("Digite o título do livro que deseja pegar emprestado: ").lower()
        for livro in livros_cad:
            if pesquisa in livro['titulo'].lower():
                print(f"Livro encontrado: {livro['titulo']} (Status: {livro['Disponibilidade']})")




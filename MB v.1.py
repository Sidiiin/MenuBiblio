

# Livros guardados
livro1 = {'autor':'Steve Hawkins','titulo':'Breves respostas para grandes questões','Disponibilidade':'Disponivel'}
livro2 = {'autor':'Galapagos Jogos', 'titulo':'Dungeons & Dragons: Livro do mestre','Disponibilidade':'Disponivel'}
livro3 = {'autor':'Harlan Ellison', 'titulo':'Não tenho boca mas preciso gritar','Disponibilidade':'Disponivel'}
livro4 = {'autor':'Agatha Christie', 'titulo':'Os elefantes não esquecem','Disponibilidade':'Disponivel'}
livro5 = {'autor':'H.P Lovecraft', 'titulo':'O chamado de Cthulhu e outros contos','Disponibilidade':'Disponivel'}
livro6 = {'autor':'Hideaki Anno', 'titulo':'NEON GENESIS EVANGELION: Capitulo 1','Disponibilidade':'Disponivel'}
livros_cad = [livro1, livro2, livro3, livro4, livro5, livro6]

# Alunos cadastrados
aluno1 = {'nome':'Sidney Fernandes','matricula':'160802'}
alunos_cad = [aluno1]

# Menu interativo
controle_do_menu = 0
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
    print('╚══════════════════════════════════════════╝')

    controle_do_menu = int(input('Escolha uma opção: '))
    print('═' * 44)

    if controle_do_menu == 9:
        break
    #Funçoes

# Pesquisa de livro (Funcionando)
    if controle_do_menu == 1:
        while True:
            print('═' * 44)
            pesquisa = input("Digite o título do livro que deseja procurar: ").lower()
            achado = False
            for livro in livros_cad:
                if pesquisa in livro['titulo'].lower():
                    print(f"Livro encontrado: {livro['titulo']} por {livro['autor']} (Status: {livro['Disponibilidade']})")
                    achado = True
            if not achado:
                print('═' * 44)
                print("Ainda não temos esse livro em nossa biblioteca\ncaso deseje cadastrar esse livro em nossso sistema\nvolte ao menu e selecione 'Cadastrar um livro' e faça o cadastro do livro desejado.")
            print('═' * 44)
            if input("Digite 'v' para voltar ao menu: ").lower() == 'v':
                break

# Cadastro de aluno (Funcionando)
    if controle_do_menu == 5:
        while True:
            print('═' * 44)
            alunoadd = {'nome': input('Insira o nome do aluno que deseja cadastrar: '), 'matricula': int(input('Matricula do aluno que deseja cadastrar: '))}
            alunos_cad.append(alunoadd)
            print("Aluno cadastrado com sucesso!")
            print('═' * 44)
            if input("Digite 'v' para voltar ao menu: ").lower() == 'v':
                break

# Lista de livros disponiveis(Funcionando)
    if controle_do_menu == 6:
        while True:
            print('═' * 44)
            print("Livros disponíveis:")
            for livro in livros_cad:
                if livro['Disponibilidade'] == 'Disponivel':
                    print(f"{livro['titulo']} de {livro['autor']}")
            print('═' * 44)
            if input("Digite 'v' para voltar ao menu: ").lower() == 'v':
                break

# Lista de alunos cadastrados(Funcionando)
    if controle_do_menu == 7:
        while True:
            print('═' * 44)
            for aluno in alunos_cad:
                print(f"{aluno['nome']} \nMatricula: {aluno['matricula']}\n")
            print('═' * 44)
            if input("Digite 'v' para voltar ao menu: ").lower() == 'v':
                break

# Cadastro de livros(Funcionando)
    if controle_do_menu == 4:
        while True:
            print('═' * 44)
            livroadd = {'autor': input('Autor do livro a qual deseja cadastrar: '), 'titulo': input('Titulo do livro a qual deseja cadastrar: '),'Disponibilidade':'Disponivel'}
            livros_cad.append(livroadd)
            print("Livro cadastrado com sucesso!")
            print('═' * 44)
            if input("Digite 'v' para voltar ao menu: ").lower() == 'v':
                break

# Verificação de disponibilidade (Funcionando)
    if controle_do_menu == 2:
        while True:
            print('═' * 44)
            pesquisa = input("Digite o título do livro que deseja pegar emprestado: ").lower()
            for livro in livros_cad:
                if pesquisa in livro['titulo'].lower():
                    print(f"Livro encontrado: {livro['titulo']} (Status: {livro['Disponibilidade']})")
            else:
                print('Ainda não temos esse livro em nossa biblioteca')
            print('═' * 44)
            if input("Digite 'v' para voltar ao menu: ").lower() == 'v':
                break

# Alteração de Status do emprestimo(Funcionando)
    if controle_do_menu == 3:
        while True:
            status_emprestimo = int(input('Você deseja:\n 1 - Pegar um livro emprestado\n 2 - Devolver um livro\n'))
            print('═' * 44)
            if status_emprestimo == 1:
                matricula_pesquisa = input('Digite seu número de matrícula: ')
                aluno_matriculado = None
                for aluno in alunos_cad:
                    if aluno['matricula'] == matricula_pesquisa:
                        aluno_matriculado = aluno
                        break  # Interrompe o loop assim que encontrar a matrícula
                if aluno_matriculado:
                    print('═' * 44)
                    print(f"Matrícula encontrada: {aluno_matriculado['nome']}")
                    livroemp = input('Qual livro deseja pegar emprestado?: ')
                    for livro in livros_cad:
                        if livroemp in livro['titulo'].lower():
                            livro_encontrado = True
                            if livro['Disponibilidade'] == 'Disponivel':
                                print(f"Leve o livro {livro['titulo']} até o bibliotecario junto com o recibo para retirada.\nTenha uma boa leitura!")
                                print('═' * 44)
                                livro['Disponibilidade'] = 'Indisponivel'
                    if input("Digite 'v' para voltar ao menu: ").lower() == 'v':
                        break
                else:
                    print('═' * 44)
                    print('Não encontramos essa matrícula em nosso sistema, apenas usuarios cadastrados podem pegar livros emprestados.')
                    print('═' * 44)
                    if input("Digite 'v' para voltar ao menu: ").lower() == 'v':
                        break

            if status_emprestimo == 2:
                devolucao = input('Qual livro você está devolvendo?: ')
                for livro in livros_cad:
                    if devolucao in livro['titulo'].lower():
                        livro['Disponibilidade'] = 'Disponivel'
                print(f"Agradeçemos a sua devolução!\nqual será sua proxima leitura?!")
            print('═' * 44)
            print("Temos esses livros disponíveis:")
            for livro in livros_cad:
                if livro['Disponibilidade'] == 'Disponivel':
                    print(f"{livro['titulo']} de {livro['autor']}")
            print('═' * 44)
            if input("Digite 'v' para voltar ao menu: ").lower() == 'v':
                break
#Acabou as funçoes

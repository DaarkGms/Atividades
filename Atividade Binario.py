import pickle


def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone: ")
    email = input("Digite o e-mail: ")
    
    contato = {
        'nome': nome,
        'telefone': telefone,
        'email': email
    }
    
    with open('contatos.bin', 'ab') as arquivo:
        pickle.dump(contato, arquivo)
    
    print(f"Contato {nome} foi adicionado com sucesso.")


def listar_contatos():
    try:
        with open('contatos.bin', 'rb') as arquivo:
            while True:
                try:
                    contato = pickle.load(arquivo)
                    print("-" * 20)
                    print(f"Nome: {contato['nome']}")
                    print(f"Telefone: {contato['telefone']}")
                    print(f"E-mail: {contato['email']}")
                    print("-" * 20)
                except EOFError:
                    break
    except FileNotFoundError:
        print("Ainda não existem contatos salvos.")


while True:
    print("\n=== Agenda de Contatos ===")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        adicionar_contato()
    elif opcao == '2':
        listar_contatos()
    elif opcao == '3':
        print("Saindo da aplicação.")
        break
    else:
        print("Opção inválida. Tente novamente.")

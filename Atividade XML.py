import xml.etree.ElementTree as ET

# Função para adicionar um novo contato
def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone: ")
    email = input("Digite o e-mail: ")
    
    contato = ET.Element("contato")
    ET.SubElement(contato, "nome").text = nome
    ET.SubElement(contato, "telefone").text = telefone
    ET.SubElement(contato, "email").text = email
    
    tree = ET.ElementTree(contato)
    
    try:
        with open('contatos.xml', 'rb') as arquivo:
            root = ET.fromstring(arquivo.read())
    except FileNotFoundError:
        root = ET.Element("contatos")
    
    root.append(contato)
    
    with open('contatos.xml', 'wb') as arquivo:
        tree = ET.ElementTree(root)
        tree.write(arquivo)
    
    print(f"Contato {nome} foi adicionado com sucesso.")

def listar_contatos():
    try:
        tree = ET.parse('contatos.xml')
        root = tree.getroot()
        
        for contato in root.findall('contato'):
            nome = contato.find('nome').text
            telefone = contato.find('telefone').text
            email = contato.find('email').text
            
            print(f"Nome: {nome}")
            print(f"Telefone: {telefone}")
            print(f"E-mail: {email}")
            print("-" * 20)
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

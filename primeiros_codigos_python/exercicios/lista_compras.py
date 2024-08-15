lista_compras = [] 

while True:
    print("=== LISTAS DE COMPRAS ===")
    print("\n1. ADICIONAR ITEM")
    print("2. LISTAR ITENS")
    print("3. SAIR")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        novo_item = input("Digite o nome do novo_item: ")
        lista_compras.append(novo_item)
        print(f"Item '{novo_item}' adicionado com sucesso!")


    elif opcao == "2":
        if not lista_compras:
            print("Lista de compras vazia!")
        else:
            print("\nPRODUTOS")
            for item in lista_compras:
                print(f"- {item}")
    
    
    elif opcao == "3":
        print("Obrigado por usar o programa!")
        break
    else: 
        print("Opção inválida. Por favor, tente novamente.")
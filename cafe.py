print(".....Canelinha Cafe.....")
print(".......since 1980.......")
print()
nome = input("Digite seu nome:")
print()
print("Olá,", nome+"!", "Seja bem-vindo(a) ao Canelinha Cafe!")
print()

opcoes = {
    "cappucino": [12, 10],
    "frappucino": [12, 10],
    "moccacino": [12, 10],
    "macciato": [12, 10],
    "latte": [10, 10],
    "espresso": [7, 10],
    "espresso latte": [9, 10]
}

cadastros = {}
historico = {}

desconto = False
ciclo = True


# ---------------- CPF ----------------
def validar_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    dig1 = (soma * 10) % 11
    if dig1 == 10:
        dig1 = 0

    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    dig2 = (soma * 10) % 11
    if dig2 == 10:
        dig2 = 0

    return dig1 == int(cpf[9]) and dig2 == int(cpf[10])


# ---------------- Carrinho ----------------
def mostrar_carrinho(historico, opcoes, desconto):
    if not historico:
        print("Carrinho vazio.")
        return

    total = 0

    for item in historico:
        qtd = historico[item]
        preco = opcoes[item][0]
        subtotal = qtd * preco
        total += subtotal
        print(f"- {item} x{qtd} = R$ {subtotal}")

    if desconto:
        print("Total com desconto: R$", total * 0.9)
    else:
        print("Total: R$", total)


# ---------------- ADMIN ----------------
def menu_admin(opcoes):
    admin_ciclo = True

    while admin_ciclo:
        print("\n--- MENU ADMIN ---")
        contador = 1
        lista = list(opcoes.keys())

        for cafe in lista:
            print(contador, "-", cafe, "| Estoque:", opcoes[cafe][1])
            contador += 1

        print("1 - Alterar estoque")
        print("2 - Adicionar estoque")
        print("3 - Zerar estoque")
        print("0 - Sair do admin")

        escolha = int(input("Escolha: "))

        if escolha == 0:
            admin_ciclo = False

        elif escolha in [1, 2, 3]:
            while True:
                try:
                    item = int(input("Digite o número do produto: "))
                    if 1 <= item <= len(lista):
                        break
                    else:
                        print(f"Número inválido. Digite um número entre 1 e {len(lista)}.")
                except ValueError:
                    print("Entrada inválida. Digite um número inteiro.")
            
            cafe = lista[item - 1]

            if escolha == 1:
                novo = int(input("Novo valor de estoque: "))
                opcoes[cafe][1] = novo
                print("Estoque atualizado!")

            elif escolha == 2:
                add = int(input("Quantidade para adicionar: "))
                opcoes[cafe][1] += add
                print("Estoque adicionado!")

            elif escolha == 3:
                opcoes[cafe][1] = 0
                print("Estoque zerado!")

        else:
            print("Opção inválida.")


# ---------------- MENU ----------------
while ciclo:
    contador = 1
    for cafe in opcoes:
        print(contador, "-", cafe, "R$", opcoes[cafe][0], "| Estoque:", opcoes[cafe][1])
        contador += 1

    print("9 - Ver carrinho")
    print("10 - Cadastrar")
    print("11 - Login")
    print("12 - Remover item")
    print("0 - Finalizar")
    print()

    escolha = int(input("Escolha: "))
    print()

    if escolha == 0:
        mostrar_carrinho(historico, opcoes, desconto)
        print("Obrigado por comprar!")
        break

    elif 1 <= escolha <= len(opcoes):
        lista = list(opcoes.keys())
        cafe = lista[escolha - 1]

        qtd = int(input("Quantidade: "))
        estoque = opcoes[cafe][1]

        if qtd <= estoque and qtd > 0:
            historico[cafe] = historico.get(cafe, 0) + qtd
            opcoes[cafe][1] -= qtd
            print("Pedido adicionado!")
        else:
            print("Estoque insuficiente!")

    elif escolha == 9:
        mostrar_carrinho(historico, opcoes, desconto)

    elif escolha == 10:
        usuario = input("Crie um usuário: ")

        if usuario in cadastros:
            print("Usuário já existe.")
            continue

        senha = input("Crie uma senha: ")
        confirmar = input("Confirme a senha: ")

        if senha != confirmar:
            print("Senhas não coincidem.")
            continue

        cpf = input("Digite seu CPF: ")

        if not validar_cpf(cpf):
            print("CPF inválido.")
            continue

        cadastros[usuario] = {"senha": senha, "cpf": cpf}
        print("Cadastro realizado com sucesso! Desconto aplicado.")
        desconto = True

    elif escolha == 11:
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        # 🔥 LOGIN ADMIN
        if usuario == "admin" and senha == "admin@155":
            print("Login ADMIN realizado!")
            menu_admin(opcoes)

        # LOGIN NORMAL
        elif usuario in cadastros and cadastros[usuario]["senha"] == senha:
            print("Login realizado!")
            desconto = True

        else:
            print("Usuário ou senha incorretos.")

    elif escolha == 12:
        lista = list(opcoes.keys())

        escolha_item = int(input("Número do item: "))
        cafe = lista[escolha_item - 1]

        if cafe not in historico:
            print("Não está no carrinho.")
        else:
            qtd = int(input("Quantidade para remover: "))

            if qtd >= historico[cafe]:
                opcoes[cafe][1] += historico[cafe]
                del historico[cafe]
            else:
                historico[cafe] -= qtd
                opcoes[cafe][1] += qtd

            print("Removido com sucesso!")

    else:
        print("Opção inválida.")

    print()

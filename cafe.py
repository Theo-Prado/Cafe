print(".....Canelinha Cafe.....")
print(".......since 1980.......")
print()

nome = input("Digite seu nome:")
print()
print("Olá,", nome+"!", "Seja bem-vindo(a) ao Canelinha Cafe!")
print()

# preço, estoque
opcoes = {
    "cappucino": [12, 10],
    "frappucino": [12, 10],
    "moccacino": [12, 10],
    "macciato": [12, 10],
    "latte": [10, 10],
    "espresso": [7, 10],
    "espresso latte": [9, 10]
}

# agora cada usuário tem: senha + cpf
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

    # FINALIZAR
    if escolha == 0:
        mostrar_carrinho(historico, opcoes, desconto)
        print("Obrigado por comprar!")
        break

    # COMPRAR
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

    # CARRINHO
    elif escolha == 9:
        mostrar_carrinho(historico, opcoes, desconto)

    # CADASTRO
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

        cadastros[usuario] = {
            "senha": senha,
            "cpf": cpf
        }

        print("Cadastro realizado com sucesso! Você ganhou 10% de desconto.")
        desconto = True

    # LOGIN
    elif escolha == 11:
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if usuario in cadastros and cadastros[usuario]["senha"] == senha:
            print("Login realizado!")
            desconto = True
        else:
            print("Usuário ou senha incorretos.")

    # REMOVER ITEM
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

print(".....Canelinha Cafe.....")
print(".......since 1980.......")
print()
nome = input("Digite seu nome:")
print()
print("Olá,",nome+"!","Seja bem-vindo(a) ao serviço de auto atendimento do Canelinha Cafe! A melhor cafeteria da região desde 1980!")
print()

# O primeiro valor sempre é o preço e o segundo valor sempre é o estoque.
opcoes = {
    "cappucino": [12, 10],
    "frappucino": [12, 10],
    "moccacino": [12, 10],
    "macciato": [12, 10],
    "latte": [10, 10],
    "espresso": [7, 10],
    "espresso latte": [9, 10]
}

# Histórico de cadastro, nome, senha e cpf respectivamente.
cadastros = {}

# Histórico do pedido atual
historico = {}

# Verifica se o cpf é válido para aplicar o desconto.
cpf_valido = False

# Aplica o desconto.
desconto = False

# Ciclos para while.
ciclo = True
ciclo_cpf = True

def mostrar_carrinho(historico, opcoes, desconto):
    if not historico:
        print("Carrinho vazio.")
        return

    total = 0

    for item in historico:
        quantidade = historico[item]
        preco = opcoes[item][0]

        subtotal = preco * quantidade
        total += subtotal

        print(f"- {item} x{quantidade} = R$ {subtotal}")

    if desconto:
        total_com_desconto = total * 0.9
        print("Total com desconto: R$", total_com_desconto)
    else:
        print("Total: R$", total)

while ciclo:
  contador = 1
  for cafe in opcoes:
    preco = opcoes[cafe][0]
    print(contador, "-", cafe, "R$", preco)
    contador += 1
  print("8 - Adicionar saldo")
  print("9 - Mostrar pedidos no carrinho")
  print("10 - Cadastrar-se para ganhar desconto")
  print("11 - Fazer login para ganhar desconto")
  print("12 - Remover um item do pedido")
  print("0 - Finalizar")
  print()
  escolha = int(input("Digite a opção que queira selecionar:"))
  print()
  if escolha == 0:
    ciclo = False
    desconto = False
    cpf_valido = False
    mostrar_carrinho(historico, opcoes, desconto)
    print(f"Obrigado por comprar no Canelinha Cafe! Volte sempre, {nome}!")
elif 1 <= escolha <= len(opcoes):
    lista_cafes = list(opcoes.keys())
    cafe = lista_cafes[escolha - 1]

    estoque = opcoes[cafe][1]

    quantidade = int(input(f"Quantos {cafe} você quer? "))

    if quantidade <= 0:
        print("Quantidade inválida.")
    
    elif quantidade <= estoque:
        # adiciona no carrinho
        if cafe in historico:
            historico[cafe] += quantidade
        else:
            historico[cafe] = quantidade

        # dá baixa no estoque
        opcoes[cafe][1] -= quantidade

        print(f"Você escolheu {quantidade}x {cafe}. Pedido sendo preparado!")

    else:
        print(f"Estoque insuficiente! Temos apenas {estoque} disponível(is).")
  elif escolha == 9:
    mostrar_carrinho(historico, opcoes, desconto)
  elif escolha == 10:
    ciclo_cpf = True
    while ciclo_cpf:
      cpf = input("Digite seu cpf:")
      cpf = cpf.replace('.','').replace('-','').replace('/','').replace('|','').replace('\\','')
      if len(cpf) != 11 or cpf == cpf[0] * 11:
        print("CPF inválido.")
        continue
      soma = 0
      for i in range(9):
        soma += int(cpf[i]) * (10 - i)
      dig1 = (soma * 10) % 11
      if dig1 == 11:
        dig1 = 0
      soma = 0
      for i in range(10):
        soma += int(cpf[i]) * (11 - i)
      dig2 = (soma * 10) % 11
      if dig2 == 10:
        dig2 = 0
      cpf_valido = dig1 == int(cpf[9]) and dig2 == int(cpf[10])
      if cpf_valido:
        if cpf in cadastros:
          print("Esse cpf já esta cadastrado! Haverá um desconto de 10% em seu pedido!")
          ciclo_cpf = False
          desconto = True
        else:
          cadastros.append(cpf)
          ciclo_cpf = False
          desconto = True
          print("Cadastro realizado com sucesso! Haverá um desconto de 10% em seu pedido!")
      else:
        print("Erro! Cpf inválido ou digitado incorretamente.")
  elif escolha == 11:
    cpf = input("Digite seu cpf:")
    cpf = cpf.replace('.','').replace('-','').replace('/','').replace('|','').replace('\\','')
    if cpf in cadastros:
      desconto = True
      print("Login realizado com sucesso! Haverá um desconto de 10% em seu pedido!")
    else:
      print("Desculpe, esse cpf não esta cadastrado em nosso sistema.")
elif escolha == 11:
    lista_cafes = list(opcoes.keys())

    escolha1 = int(input("Digite o número do item que deseja remover: "))
    cafe = lista_cafes[escolha1 - 1]

    if cafe not in historico:
        print("Esse item não está no carrinho.")
    
    else:
        quantidade_remover = int(input(f"Quantos {cafe} deseja remover? "))
        quantidade_atual = historico[cafe]

        if quantidade_remover <= 0:
            print("Quantidade inválida.")

        elif quantidade_remover >= quantidade_atual:
            # remove tudo
            del historico[cafe]
            opcoes[cafe][1] += quantidade_atual  # devolve ao estoque
            print(f"{cafe} removido completamente do carrinho.")

        else:
            # remove parcialmente
            historico[cafe] -= quantidade_remover
            opcoes[cafe][1] += quantidade_remover  # devolve ao estoque
            print(f"{quantidade_remover}x {cafe} removido(s).")
    print()
    print("Remoção realizada!")
    print()
    print("Seu carrinho:")
    print()
    mostrar_carrinho(historico, opcoes, desconto)
  else:
    print("Número inválido.")
  print()

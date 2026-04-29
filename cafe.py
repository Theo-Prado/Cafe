print(".....Canelinha Cafe.....")
print(".......since 1980.......")
print()
nome = input("Digite seu nome:")
print()
print("Olá,",nome+"!","Seja bem-vindo(a) ao serviço de auto atendimento do Canelinha Cafe! A melhor cafeteria da região desde 1980!")
print()

opcoes = [
    "Canelinha (A especialidade da casa!)",
    "Cappuccino",
    "Mocaccino",
    "Espresso",
    "Espresso Latte",
    "Latte"
]

precos = [
    15,
    12,
    11,
    8,
    10,
    10
]

cadastros = []
historico = []
historico_precos = []

cpf_valido = False
desconto = False
ciclo = True
ciclo_cpf = True

def mostrar_carrinho(historico, historico_precos, desconto):
    if not historico:
      print("Carrinho vazio.")
    desconto_10 = sum(historico_precos) * 0.10
    for i, item in enumerate(historico):
      print("-", item, "R$", historico_precos[i])
    if desconto:
      print("Total com desconto: R$",
              sum(historico_precos) - desconto_10)
    else:
        print("Total: R$", sum(historico_precos))
    if not historico:
      print("Carrinho vazio.")

while ciclo:
  contador = 1
  for i in range(len(opcoes)):
    cafe = opcoes[i]
    preco = precos[i]
    print(contador,"-",cafe,"R$",preco)
    contador = contador + 1
  print("7 - Adicionar saldo")
  print("8 - Mostrar pedidos no carrinho")
  print("9 - Cadastrar-se para ganhar desconto")
  print("10 - Fazer login para ganhar desconto")
  print("11 - Remover um item do pedido")
  print("0 - Finalizar")
  print()
  escolha = int(input("Digite a opção que queira selecionar:"))
  print()
  if escolha == 0:
    ciclo = False
    desconto = False
    cpf_valido = False
    mostrar_carrinho(historico, historico_precos, desconto)
    print(f"Obrigado por comprar no Canelinha Cafe! Volte sempre, {nome}!")
  elif 1 <= escolha <= 6:
    conta = escolha - 1
    historico.append(opcoes[conta])
    historico_precos.append(precos[conta])
    print("Você escolheu",opcoes[conta]+".","Seu pedido esta sendo preparado!")
  elif escolha == 8:
    mostrar_carrinho(historico, historico_precos, desconto)
  elif escolha == 9:
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
      if dig1 == 10:
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
  elif escolha == 10:
    cpf = input("Digite seu cpf:")
    cpf = cpf.replace('.','').replace('-','').replace('/','').replace('|','').replace('\\','')
    if cpf in cadastros:
      desconto = True
      print("Login realizado com sucesso! Haverá um desconto de 10% em seu pedido!")
    else:
      print("Desculpe, esse cpf não esta cadastrado em nosso sistema.")
  elif escolha == 11:
    escolha1 = int(input("Digite o item que deseja remover:"))
    conta = escolha1 - 1
    escolha2 = int(input("Digite quantos desse item deseja remover:"))
    escolha2 = escolha2 + 1
    for item in range(1,escolha2):
                      historico.remove(opcoes[conta])
                      historico_precos.remove(precos[conta])
    print()
    print("Remoção realizada!")
    print()
    print("Seu carrinho:")
    print()
    mostrar_carrinho(historico, historico_precos, desconto)
  else:
    print("Número inválido.")
  print()

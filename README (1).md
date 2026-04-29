# ☕ Canelinha Cafe — Sistema de Auto Atendimento

> Sistema de auto atendimento interativo via terminal para a cafeteria Canelinha Cafe, tradição desde 1980.

---

## 📋 Sobre o Projeto

O **Canelinha Cafe** é uma aplicação de linha de comando desenvolvida em Python que simula um totem de auto atendimento de cafeteria. O cliente pode montar seu pedido, gerenciar o carrinho, se cadastrar com CPF para obter desconto e finalizar a compra, tudo de forma simples e interativa.

---

## ✨ Funcionalidades

- Saudação personalizada com o nome do cliente
- Cardápio com **6 opções de bebidas** e seus respectivos preços
- **Carrinho de compras** com adição e remoção de itens
- **Cadastro por CPF** com validação completa dos dígitos verificadores
- **Login por CPF** para clientes já cadastrados
- **Desconto de 10%** para clientes cadastrados
- Exibição do total com ou sem desconto
- Resumo do pedido ao finalizar

---

## 🍵 Cardápio

| # | Bebida | Preço |
|---|---|---|
| 1 | Canelinha *(A especialidade da casa!)* | R$ 15 |
| 2 | Cappuccino | R$ 12 |
| 3 | Mocaccino | R$ 11 |
| 4 | Espresso | R$ 8 |
| 5 | Espresso Latte | R$ 10 |
| 6 | Latte | R$ 10 |

---

## 🚀 Como Usar

### Pré-requisitos

- Python 3.x instalado

### Executando o programa

```bash
python cafe.py
```

### Opções do menu

| Opção | Ação |
|---|---|
| `1` a `6` | Adicionar bebida ao carrinho |
| `8` | Ver carrinho e total |
| `9` | Cadastrar CPF e ganhar 10% de desconto |
| `10` | Fazer login com CPF cadastrado |
| `11` | Remover item do carrinho |
| `0` | Finalizar pedido |

---

## 🔐 Sistema de Desconto por CPF

- Ao se cadastrar (opção `9`), o CPF é **validado matematicamente** pelos dígitos verificadores
- CPFs já cadastrados podem fazer login (opção `10`) para ativar o desconto
- O desconto de **10%** é aplicado automaticamente no total do pedido

---

## 🛠️ Tecnologias

- **Linguagem:** Python 3
- **Interface:** Terminal / Linha de Comando

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request* com melhorias, correções ou novas funcionalidades.

---

*"A melhor cafeteria da região desde 1980." — Canelinha Cafe ☕*

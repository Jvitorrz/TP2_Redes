
---

# **Relatório do TP2**

## Principais Escolhas de Implementação

### Uso de `socket` e `threading`
- O **servidor** foi implementado com a biblioteca **socket**, para permitir comunicação via **TCP**, e **threading**, para permitir múltiplas conexões simultâneas.
- Cada cliente é tratado em uma **thread separada**, garantindo que vários usuários possam conversar ao mesmo tempo.

### Gerenciamento de Salas
- **Estrutura de dados utilizada:** Um **dicionário (`salas`)** armazena o nome das salas e a lista de clientes conectados.
- **Cada cliente pode entrar apenas em uma sala por vez.**
- **Ao sair da sala (`/sair`), o cliente pode entrar em outra sem desconectar do servidor.**

### Comunicação entre Clientes
- O servidor **envia mensagens apenas para clientes dentro da mesma sala**.
- O cliente **não pode enviar ou receber mensagens** de uma sala depois de sair dela.

### Logs no Servidor
- O servidor **imprime mensagens** informando quando um cliente:
  - **Cria uma sala** (`/criar <sala>`)
  - **Entra em uma sala** (`/entrar <sala>`)
  - **Sai de uma sala** (`/sair`)

Isso facilita a depuração e monitoramento da comunicação.

## Conclusão
O projeto atende aos requisitos especificados. O sistema permite uma comunicação eficiente entre múltiplos clientes e garante a organização das mensagens dentro das salas.

Como possíveis melhorias, pode-se implementar **mensagens privadas**, **suporte a autenticação de usuários**, ou até uma **interface gráfica (GUI)** para melhorar a usabilidade.

---

# Servidor de Chat com Suporte a Múltiplas Salas

## Descrição
Este projeto consiste em um Servidor de Chat com suporte a múltiplas salas, permitindo que diversos usuários se conectem ao mesmo tempo e conversem em diferentes salas de bate-papo, com o servidor responsável por gerenciar as conexões e encaminhar mensagens apenas para os participantes da mesma sala.

## Tecnologias Utilizadas
- **Linguagem:** Python
- **Bibliotecas:** `socket`, `threading`

## Como Executar

### Requisitos
- **Python** instalado.

### Instruções de Execução

1. **Clone o repositório**:
   ```sh
   git clone https://github.com/Jvitorrz/TP2_Redes.git
2. **Execute o servidor:**:
   ```sh
   python3 server.py
3. **Execute o cliente:**:
   ```sh
   python3 client.py

## Como Testar

- Execute o servidor e logo após execute clientes repetidamente utilizando em cada cliente as funções /salas (para ver a lista de salas criadas), /criar "sala", /entrar "sala" e /sair (para sair da sala atual).

## Funcionalidades Implementadas

- Suporte a múltiplas salas.
- Criação de salas com /criar "sala".
- Entrada e saída de salas com /entrar "sala" e /sair.
- Listagem de salas disponíveis com /salas.
- Envio e recebimento de mensagens apenas para usuários da mesma sala.
- Logs no servidor informando eventos importantes.

## Possíveis Melhorias Futuras

- Adicionar histórico de mensagens para que novos usuários vejam mensagens antigas.
- Implementar suporte a mensagens privadas entre usuários específicos.
- Criar uma interface gráfica para facilitar a usabilidade.
  

   
  
  
   

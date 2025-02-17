import socket
import threading

# Dicionário para armazenar salas e os clientes conectados nelas
salas = {}

lock = threading.Lock()

def handle_client(client_socket, username):
    """Lida com as mensagens recebidas de um cliente"""
    global salas
    sala_atual = None  

    while True:
        try:
            mensagem = client_socket.recv(1024).decode()
            if not mensagem:
                break

            # Comando para listar salas disponíveis
            if mensagem.lower() == "/salas":
                with lock:
                    lista_salas = ", ".join(salas.keys()) if salas else "Nenhuma sala disponível."
                client_socket.send(f"Salas disponíveis: {lista_salas}".encode())
                continue

            # Comando para criar uma nova sala
            if mensagem.lower().startswith("/criar "):
                sala_nome = mensagem.split(" ", 1)[1].strip()
                with lock:
                    if sala_nome in salas:
                        client_socket.send(f"A sala '{sala_nome}' já existe.".encode())
                    else:
                        salas[sala_nome] = []
                        print(f"[SERVIDOR] Sala '{sala_nome}' foi criada.")  
                        client_socket.send(f"Sala '{sala_nome}' criada! Use /entrar {sala_nome} para acessá-la.".encode())
                continue

            # Comando para entrar em uma sala
            if mensagem.lower().startswith("/entrar "):
                sala_nome = mensagem.split(" ", 1)[1].strip()
                with lock:
                    if sala_atual:
                        client_socket.send("Você já está em uma sala! Use /sair antes de entrar em outra.".encode())
                    elif sala_nome not in salas:
                        client_socket.send("Essa sala não existe. Use /salas para ver as disponíveis ou /criar <sala> para criar uma.".encode())
                    else:
                        salas[sala_nome].append(client_socket)
                        sala_atual = sala_nome
                        print(f"[SERVIDOR] {username} entrou na sala '{sala_nome}'.")  
                        client_socket.send(f"Você entrou na sala '{sala_nome}'. Agora pode conversar!".encode())
                continue

            # Comando para sair da sala
            if mensagem.lower() == "/sair":
                if sala_atual:
                    with lock:
                        if client_socket in salas[sala_atual]:
                            salas[sala_atual].remove(client_socket)
                    print(f"[SERVIDOR] {username} saiu da sala '{sala_atual}'.")  
                    sala_atual = None  
                    client_socket.send("Você saiu da sala.".encode())
                else:
                    client_socket.send("Você não está em nenhuma sala para sair.".encode())
                continue

            # Se o cliente tenta enviar mensagem sem estar em uma sala
            if not sala_atual:
                client_socket.send("Você não está em nenhuma sala. Use /entrar <sala> para participar.".encode())
                continue

            # Enviar mensagem apenas para clientes da mesma sala
            with lock:
                if sala_atual in salas and client_socket in salas[sala_atual]:  
                    for cliente in salas[sala_atual]:
                        if cliente != client_socket:
                            cliente.send(f"{username}: {mensagem}".encode())

        except:
            break
    
    print(f"[SERVIDOR] {username} desconectou do servidor.")  
    client_socket.close()

def start_server():
    """Inicia o servidor e gerencia conexões"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("0.0.0.0", 5000))  
    server.listen(5)
    
    print("[SERVIDOR] Servidor de Chat iniciado. Aguardando conexões...")

    while True:
        client_socket, addr = server.accept()
        print(f"[SERVIDOR] Nova conexão de {addr}")  

        client_socket.send("Digite seu nome: ".encode())
        username = client_socket.recv(1024).decode()

        client_socket.send("Bem-vindo ao chat! Use /salas para listar salas, /criar <sala> para criar e /entrar <sala> para participar.".encode()) 

        # Criar uma thread para lidar com este cliente
        client_thread = threading.Thread(target=handle_client, args=(client_socket, username))
        client_thread.start()

if __name__ == "__main__":
    start_server()

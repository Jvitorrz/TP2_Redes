import socket
import threading

def receive_messages(client_socket):
    """Recebe mensagens do servidor e as imprime na tela"""
    while True:
        try:
            mensagem = client_socket.recv(1024).decode()
            if not mensagem:
                break
            print(mensagem)
        except:
            break

def start_client():
    """Inicia o cliente e conecta ao servidor"""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 5000))  # Conectar ao servidor

    # Thread para receber mensagens do servidor
    recv_thread = threading.Thread(target=receive_messages, args=(client,))
    recv_thread.start()

    while True:
        mensagem = input()

        if mensagem.lower() == "/sair":
            client.send(mensagem.encode())

        elif mensagem.lower() in ["/salas"] or mensagem.lower().startswith(("/criar ", "/entrar ")):
            client.send(mensagem.encode())

        else:
            client.send(mensagem.encode())

if __name__ == "__main__":
    start_client()

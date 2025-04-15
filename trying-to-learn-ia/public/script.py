import openai 
openai.api_key = ""

def chat_with_ai():
    print("Bem-vindo ao Chat IA! (Digite 'sair' para encerrar a conversa)")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            print("Encerrando a conversa. Até mais!")
            break
        
        try:
            # Envia a mensagem do usuário para o modelo GPT
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um assistente amigável para conversas simples."},
                    {"role": "user", "content": user_input}
                ]
            )
            # Exibe a resposta do modelo
            ai_response = response['choices'][0]['message']['content']
            print(f"IA: {ai_response}")
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    chat_with_ai()

historico = []

def registrar_mensagem(mensagem, autor):
    historico.append(f"{autor}: {mensagem}")

# Uso:
registrar_mensagem("Oi, como você está?", "Usuário")
registrar_mensagem("Estou bem! Como posso ajudar?", "IA")

for msg in historico:
    print(msg)
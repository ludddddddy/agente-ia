from transformers import pipeline
import re

print("Carregando modelo...")

pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    max_new_tokens=100
)

print("Modelo carregado!\n")

# -----------------------------
# Função calculadora
# -----------------------------

def calcular(expressao):
    try:
        resultado = eval(expressao)
        return f"Resultado: {resultado}"
    except:
        return "Erro ao calcular"

# -----------------------------
# Função LLM
# -----------------------------

def responder_llm(pergunta):
    resposta = pipe(pergunta)
    return resposta[0]["generated_text"]

# -----------------------------
# Loop principal
# -----------------------------

print("Agente iniciado! Digite 'sair' para encerrar.\n")

while True:

    pergunta = input("Você: ")

    if pergunta.lower() == "sair":
        print("Encerrando agente...")
        break

    # verifica se parece uma conta
    if re.search(r"[0-9]+\s*[\+\-\*/]\s*[0-9]+", pergunta):
        resposta = calcular(pergunta)
    else:
        resposta = responder_llm(pergunta)

    print("\nAgente:", resposta)
    print()
# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber uma vantagem e retornar sua respectiva descrição.
def descrever_vantagem(vantagem):
    # Bloco 1 - Análise preditiva ✅
    if vantagem == "análise preditiva":
        return "capacidade de prever tendências e comportamentos futuros"

    # Bloco 2 - Processamento de linguagem natural ✅
    elif vantagem == "processamento de linguagem natural":
        return "habilidade de entender e gerar linguagem humana"

    # Bloco 3 - Automação ✅
    elif vantagem == "automação":
        return "automatização de tarefas repetitivas e processos"

    # Bloco 4 - Personalização ✅
    elif vantagem == "personalização":
        return "oferecer experiências personalizadas aos usuários"

# Imprime a descrição da vantagem recebida na "entrada" através da função "descrever_vantagem"
print(descrever_vantagem(entrada))


# Linha 2: Recebe a entrada do usuário
entrada = input()

# Linha 5: Define a função que recebe um conceito e retorna a descrição
def descrever_conceito(conceito):

    # Bloco 1 - CORRETO (já veio preenchido)
    if conceito == "aprendizado supervisionado":
        return "treinamento de modelos com dados rotulados"

    # Bloco 2 - CORRIGIDO: condição preenchida com o conceito correto
    elif conceito == "aprendizado não supervisionado":
        return "descoberta de padrões em dados não rotulados"

    # Bloco 3 (antigo linhas 16-17) - REMOVIDO!
    # Era uma armadilha: "aprendizado baseado em recompensas e punições"
    # não faz parte das saídas válidas deste desafio.

    # Bloco 4 - CORRIGIDO: condição preenchida com "redes neurais"
    elif conceito == "redes neurais":
        return "sistemas inspirados no cérebro humano para processamento de dados"

    # Bloco 5 - CORRIGIDO: condição preenchida com "processamento de linguagem natural"
    elif conceito == "processamento de linguagem natural":
        return "análise e geração de linguagem humana"

# Linha 28: Imprime o resultado
print(descrever_conceito(entrada))

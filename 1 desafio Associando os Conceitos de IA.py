# Linha 2: Recebe a entrada do usuário
entrada = input()

# Linha 5: Define a função que recebe um conceito e retorna a descrição
def descrever_conceito(conceito):

    # Linha 6-7: ✅ CORRETO — Já preenchido corretamente
    if conceito == "aprendizado supervisionado":
        return "treinamento de modelos com dados rotulados"

    # Linha 10-11: ❌ ERRO — Texto genérico "escreva aqui o conceito correspondente"
    elif conceito == "aprendizado não supervisionado":  # ← PRECISA CORRIGIR
        return "descoberta de padrões em dados não rotulados"   # ✅ Saída correta

    # Linha 13-14: ❌ ERRO DUPLO — Conceito E definição incorretos
    elif conceito == "escreva aqui o conceito correspondente":  # ← PRECISA CORRIGIR
        return "aprendizado baseado em recompensas e punições"  # ← SAÍDA ERRADA (não faz parte do desafio!)

    # Linha 16-17: ❌ ERRO — Texto genérico no conceito
    elif conceito == "escreva aqui o conceito correspondente":  # ← PRECISA CORRIGIR
        return "sistemas inspirados no cérebro humano para processamento de dados"  # ✅ Saída correta

    # Linha 19-20: ❌ ERRO — Texto genérico no conceito
    elif conceito == "escreva aqui o conceito correspondente":  # ← PRECISA CORRIGIR
        return "análise e geração de linguagem humana"          # ✅ Saída correta

# Linha 23: Imprime o resultado
print(descrever_conceito(entrada))

import random

# ===================
# CONFIGURAÇÕES
# ===================
N = 8  # número de rainhas que estarão presentes no tabuleiro
TAMANHO_POPULACAO = 100
MAXIMO_GERACOES = 200
TAXA_MUTACAO = 0.3
TAMANHO_TORNEIO = 5

# =======================
# FUNÇÕES DO ALGORITMO
# =======================

# Criar um indivíduo aleatório
def criar_individuo():
    return [random.randint(0, N - 1) for _ in range(N)]

# Calcular fitness: número de pares de rainhas se atacando
def avaliacao(individuo):
    ataques = 0
    for i in range(N):
        for j in range(i + 1, N):
            if individuo[i] == individuo[j]:
                ataques += 1  # mesma linha
            elif abs(individuo[i] - individuo[j]) == abs(i - j):
                ataques += 1  # mesma diagonal
    return ataques

# Seleção por torneio
def selecao_torneio(populacao):
    torneio = random.sample(populacao, TAMANHO_TORNEIO)
    torneio.sort(key=lambda ind: avaliacao(ind))
    return torneio[0]

# Cruzamento: crossover de um ponto
def cruzamento(pai1, pai2):
    ponto = random.randint(1, N - 1)
    filho = pai1[:ponto] + pai2[ponto:]
    return filho

# Mutação: alterar uma posição aleatória
def mutacao(individuo):
    if random.random() < TAXA_MUTACAO:
        coluna = random.randint(0, N - 1)
        linha = random.randint(0, N - 1)
        individuo[coluna] = linha

# =============================
# LOOP PRINCIPAL DO ALGORITMO
# =============================
def algoritmo_genetico():
    # Criar população inicial
    populacao = [criar_individuo() for _ in range(TAMANHO_POPULACAO)]

    for geracao in range(MAXIMO_GERACOES):
        # Avaliar se há solução perfeita
        populacao.sort(key=lambda ind: avaliacao(ind))
        melhor = populacao[0]
        melhor_avaliacao = avaliacao(melhor)

        print(f"Geração {geracao}: Melhor avaliação = {melhor_avaliacao}")

        if melhor_avaliacao == 0:
            print(f"Solução encontrada na geração {geracao}: {melhor}")
            return melhor

        # Nova população
        nova_populacao = []

        while len(nova_populacao) < TAMANHO_POPULACAO:
            # Seleção
            pai1 = selecao_torneio(populacao)
            pai2 = selecao_torneio(populacao)

            # Cruzamento
            filho = cruzamento(pai1, pai2)

            # Mutação
            mutacao(filho)

            # Adicionar filho à nova população
            nova_populacao.append(filho)

        populacao = nova_populacao

    print("Nenhuma solução perfeita encontrada.")
    return None

# Função para imprimir o tabuleiro
def imprimir_tabuleiro(solucao):
    # Borda superior
    print(" +" + "---" * N + "+")

    for linha in range(N):
        texto = f"{linha}|"
        for coluna in range(N):
            if solucao[linha] == coluna:
                texto += " Q "
            else:
                texto += " . "
        texto += "|"
        print(texto)

    # Borda inferior
    print(" +" + "---" * N + "+")

    # Números das colunas
    numeros_colunas = "   " + "  ".join(str(i) for i in range(N))
    print(numeros_colunas)
    print()

# =======================
# EXECUÇÃO
# =======================
if __name__ == "__main__":
    solucao = algoritmo_genetico()
    if solucao:
        print("Solução final:", solucao)
        imprimir_tabuleiro(solucao)
    else:
        print("Não foi possível encontrar uma solução.")

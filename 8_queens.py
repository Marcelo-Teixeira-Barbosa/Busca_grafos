import random

def queens_attacks(state):
    """
    Função que calcula o número de ataques entre rainhas em um estado.
    """
    attacks = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            # Verifica se há ataques na mesma linha, coluna ou diagonal
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                attacks += 1
    return attacks

def generate_random_state():
    """
    Função que gera um estado aleatório para o problema das 8 rainhas.
    """
    return [random.randint(1,8) for _ in range(8)]

def hill_climbing_with_random_restart(max_restarts):
    """
    Função que executa o algoritmo de subida da encosta com reinício aleatório
    para o problema das 8 rainhas.
    """
    best_state = None
    best_attacks = float('inf')
    restarts = 0
    
    while restarts < max_restarts:
        # Gera um estado aleatório
        current_state = generate_random_state()
        current_attacks = queens_attacks(current_state)
        print("current state")
        print(current_state)
        
        # Executa o algoritmo de subida da encosta
        while True:
            neighbors = []
            for i in range(8):
                for j in range(1,9):
                    if current_state[i] != j:
                        neighbor = list(current_state)
                        neighbor[i] = j
                        neighbors.append(neighbor)
            # Escolhe o melhor vizinho
            if not neighbors:
                break
            neighbor_attacks = [queens_attacks(neighbor) for neighbor in neighbors]
            best_neighbor_attacks = min(neighbor_attacks)
            best_neighbor = neighbors[neighbor_attacks.index(best_neighbor_attacks)]
            
            
            # Verifica se houve melhora na solução
            if best_neighbor_attacks >= current_attacks:
                break
            current_state = best_neighbor
            current_attacks = best_neighbor_attacks
            
        # Verifica se encontrou uma solução melhor do que a atual
        if current_attacks < best_attacks:
            best_state = current_state
            best_attacks = current_attacks
            
        # Incrementa o número de reinícios
        restarts += 1
        
    # Converte a lista de posições em uma matriz
    matrix = []
    for i in range(8):
        row = [0] * 8
        row[best_state[i] - 1] = 1
        matrix.append(row)
        
    return matrix, restarts, best_attacks


solution, restarts, best_attacks = hill_climbing_with_random_restart(max_restarts=100)
print()
for row in solution:
    print(row)
print("reinicios = ", restarts)
print("ataques = ", best_attacks)
# 🧬 Problema das N Rainhas com Algoritmo Genético

Este projeto implementa uma solução para o clássico **Problema das N Rainhas** utilizando um **Algoritmo Genético (AG)**. O objetivo é posicionar N rainhas em um tabuleiro NxN de forma que **nenhuma rainha ataque outra** (nem na mesma linha, coluna ou diagonal).


<img width="314" alt="image" src="https://github.com/user-attachments/assets/8ad37cf0-893b-44ac-b604-fb081e64eea6" />



---

## 📚 Sobre o Problema

No problema das N rainhas, o desafio é encontrar uma configuração onde:
- Cada **linha**, **coluna** e **diagonal** contenha **no máximo uma rainha**.
- Isso equivale a encontrar uma solução livre de conflitos entre peças de xadrez.

---

## ⚙️ Como Funciona o Algoritmo Genético

O algoritmo segue os seguintes passos:

1. **Geração da população inicial** com indivíduos aleatórios.
2. **Avaliação (fitness)** de cada indivíduo com base no número de conflitos entre rainhas.
3. **Seleção por torneio** dos melhores candidatos.
4. **Cruzamento (crossover)** entre dois pais para gerar filhos.
5. **Mutação aleatória** para manter a diversidade genética.
6. Repetição por até um número máximo de gerações ou até encontrar a solução perfeita (`fitness == 0`).

---

## 📁 Estrutura do Projeto

n-queens-genetic/
│
├── main.py # Código-fonte do algoritmo genético
├── README.md # Este arquivo


---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.6 ou superior

### Executando o código

```bash
python main.py
```
O algoritmo imprimirá, a cada geração, o melhor valor de fitness encontrado, e, ao encontrar uma solução perfeita, exibirá a configuração final.

🔧 Parâmetros Configuráveis
Você pode editar os seguintes valores no início do main.py:

```
N = 20               # Número de rainhas
POPULATION_SIZE = 100
MAX_GENERATIONS = 10000
MUTATION_RATE = 0.5
TOURNAMENT_SIZE = 5
```

# 📈 Exemplo de Saída
```
Geração 0: Melhor fitness = 9
Geração 1: Melhor fitness = 7
...
Geração 84: Melhor fitness = 0
Solução encontrada na geração 84: [12, 2, 7, 4, 18, ...]

```

# ✅ Melhorias Possíveis
Adicionar visualização gráfica do tabuleiro com matplotlib ou pygame.

Usar uma representação com permutação para evitar conflitos em linhas.

Substituir o one-point crossover por PMX (Partially Mapped Crossover).

Implementar elitismo, mantendo os melhores indivíduos em cada geração.

# 📄 Licença
Este projeto é de uso educacional e pode ser modificado livremente para fins de estudo, pesquisa ou melhoria.

# 🤝 Contribuição
Sinta-se à vontade para criar um fork, testar com diferentes valores de N, melhorar o algoritmo ou adicionar recursos!

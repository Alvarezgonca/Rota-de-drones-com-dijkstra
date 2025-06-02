import networkx as nx
import matplotlib.pyplot as plt

# Criamos um grafo com a biblioteca networkx
G = nx.Graph()

# Aqui definimos os lugares
lugares = [
    "Centro de Maricá",
    "Hospital Municipal Conde Modesto Leal",
    "UPA de Inoã",
    "Farmácia Popular",
    "Praça Orlando de Barros Pimentel",
    "Rodoviária de Maricá",
    "Escola Joana Benedicta Rangel",
    "Posto de Saúde de Itaipuaçu",
    "Farmácia Itaipuaçu",
    "UPA de Itaipuaçu"
]

# Agora vamos adicionar esses lugares como pontos ou nós
for lugar in lugares:
    G.add_node(lugar)

# Agora definimos as conexões entre esses lugares que vão ser as linhas ou arestas do grafo
ligacoes = [
    ("Centro de Maricá", "Hospital Municipal Conde Modesto Leal"),
    ("Centro de Maricá", "Rodoviária de Maricá"),
    ("Centro de Maricá", "Praça Orlando de Barros Pimentel"),
    ("Centro de Maricá", "Farmácia Popular"),
    ("Hospital Municipal Conde Modesto Leal", "Escola Joana Benedicta Rangel"),
    ("UPA de Inoã", "Rodoviária de Maricá"),
    ("Farmácia Popular", "Farmácia Itaipuaçu"),
    ("Farmácia Itaipuaçu", "Posto de Saúde de Itaipuaçu"),
    ("UPA de Itaipuaçu", "Posto de Saúde de Itaipuaçu"),
    ("UPA de Itaipuaçu", "UPA de Inoã")
]

# Adicionamos essas conexões no grafo
# O "weight=1" significa que todas as distâncias são iguais (só pra simular uma distância igual a outra)
for ligacao in ligacoes:
    G.add_edge(*ligacao, weight=1)

# Mostramos a lista dos locais numerados para o usuário poder escolher
print("Locais disponíveis:")
for i, lugar in enumerate(lugares):
    print(f"{i + 1}. {lugar}")

# Pedimos para o usuário digitar os números dos locais de origem e destino
orig_index = int(input("Digite o número do local de origem: ")) - 1
dest_index = int(input("Digite o número do local de destino: ")) - 1

# Pegamos os nomes dos lugares na lista
origem = lugares[orig_index]
destino = lugares[dest_index]

# Usamos o algoritmo de Dijkstra (como solicitado) para encontrar o caminho mais curto entre os dois locais.
caminho = nx.dijkstra_path(G, source=origem, target=destino, weight="weight")

# Mostramos o caminho encontrado, passo a passo.
print("\nCaminho mais curto:")
for i, lugar in enumerate(caminho):
    print(f"{i + 1}. {lugar}")

# Agora definimos os locais que são pontos de suprimento (tipo hospitais e farmácias) para mudarmos a cor (pq clara quis).
suprimentos = [
    "Hospital Municipal Conde Modesto Leal",
    "UPA de Inoã",
    "UPA de Itaipuaçu",
    "Farmácia Popular",
    "Farmácia Itaipuaçu",
    "Posto de Saúde de Itaipuaçu"
]

# Geramos as posições dos nós para mostrar visualmente o grafo.
posicoes = nx.spring_layout(G, seed=42)  # seed garante que o layout não muda toda vez

# Definimos a cor dos nós: verde se for ponto de suprimento, azul claro se não for.
cores_nos = ["green" if lugar in suprimentos else "lightblue" for lugar in G.nodes]

# Agora pintamos as conexões do caminho mais curto de vermelho, o resto fica cinza.
cores_arestas = []
for u, v in G.edges():
    if u in caminho and v in caminho and abs(caminho.index(u) - caminho.index(v)) == 1:
        cores_arestas.append("red")
    else:
        cores_arestas.append("gray")

# Criamos o gráfico/visualização do grafo.
plt.figure(figsize=(15, 8))
nx.draw(
    G,
    posicoes,
    with_labels=True,         # mostra o nome dos lugares
    node_color=cores_nos,     # cor dos locais
    edge_color=cores_arestas, # cor das conexões
    node_size=2000,           # tamanho dos nós (os círculos)
    font_size=9,              # tamanho das letras
    font_weight='bold'       # deixar as letras em negrito
)
plt.title(f"Caminho de '{origem}' para '{destino}'", fontsize=14)
plt.show()  # exibe o gráfico com tudo

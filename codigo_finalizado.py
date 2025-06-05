import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Mapeamento das letras para os nomes
mapa_nomes = {
    "A": "Araçatiba",
    "B": "Bombeiro",
    "C": "Cachoeira",
    "D": "C.P.N",
    "E": "C.C",
    "F": "Centro",
    "G": "Galpão Tech",
    "H": "G.Spar",
    "I": "Hosp. Theka",
    "J": "Hosp. Conde",
    "K": "Lagoa",
    "L": "Max",
    "M": "Moderna",
    "N": "Museu",
    "O": "Orla",
    "P": "Pacheco",
    "Q": "P.N",
    "R": "Popular",
    "S": "PS Inoa",
    "T": "PS Maricá",
    "U": "Praça",
    "V": "Praia",
    "W": "Praia P.N",
    "X": "Prefeitura",
    "Y": "Raia",
    "Z": "Tamoio",
    "AA": "Ultrafarma",
    "AB": "UPA 1",
    "AC": "UPA 2",
    "AD": "UPA 3",
}

mapa_numerico = {
    1: "Araçatiba",
    2: "Bombeiro",
    3: "Cachoeira",
    4: "C.P.N",
    5: "C.C",
    6: "Centro",
    7: "Galpão Tech",
    8: "G.Spar",
    9: "Hosp. Theka",
    10: "Hosp. Conde",
    11: "Lagoa",
    12: "Max",
    13: "Moderna",
    14: "Museu",
    15: "Orla",
    16: "Pacheco",
    17: "P.N",
    18: "Popular",
    19: "PS Inoa",
    20: "PS Maricá",
    21: "Praça",
    22: "Praia",
    23: "Praia P.N",
    24: "Prefeitura",
    25: "Raia",
    26: "Tamoio",
    27: "Ultrafarma",
    28: "UPA 1",
    29: "UPA 2",
    30: "UPA 3",
}

def renomear(vertice):
    return mapa_nomes.get(vertice, vertice)

G = nx.Graph()
arestas = [
    ("A", "G", 6), ("B", "C", 7), ("A", "C", 8), ("D", "E", 7), ("E", "F", 7),
    ("E", "C", 7), ("B", "D", 8), ("A", "F", 6), ("C", "H", 6), ("G", "H", 7),
    ("B", "I", 6), ("I", "H", 9), ("D", "J", 7), ("K", "J", 7), ("K", "E", 8),
    ("K", "L", 7), ("L", "F", 7), ("L", "M", 6), ("N", "M", 7), ("N", "K", 6),
    ("N", "O", 7), ("O", "J", 5), ("G", "P", 9), ("P", "Q", 7), ("Q", "A", 7),
    ("Q", "R", 7), ("R", "F", 8), ("R", "S", 7), ("S", "L", 7), ("S", "T", 7),
    ("T", "M", 8), ("T", "U", 1), ("S", "U", 1), ("R", "U", 1), ("Q", "U", 1),
    ("P", "U", 1), ("I", "V", 1), ("B", "V", 1), ("D", "V", 1), ("J", "V", 1),
    ("O", "V", 1), ("V", "W", 1), ("V", "X", 1), ("V", "Y", 1), ("V", "Z", 1),
    ("Z", "X", 1), ("X", "W", 1), ("W", "Y", 1), ("U", "AA", 1), ("U", "AB", 1),
    ("U", "AC", 1), ("U", "AD", 1), ("AA", "AB", 1), ("AB", "AC", 1), ("AC", "AD", 1),
]
for u, v, w in arestas:
    G.add_edge(renomear(u), renomear(v), weight=w)

# Dijkstra
print("Locais disponíveis:")
for num, nome in mapa_numerico.items():
    print(f"{num}: {nome}")
input_source = int(input("Digite o número do local de origem (1-30): "))
input_target = int(input("Digite o número do local de destino (1-30): "))

source_nome = mapa_numerico[input_source]
target_nome = mapa_numerico[input_target]

source = renomear(source_nome)
target = renomear(target_nome)
caminho = nx.dijkstra_path(G, source=source, target=target, weight="weight")

# Layout
pos = nx.spring_layout(G, seed=42)

# Animação
arestas_do_caminho = list(zip(caminho, caminho[1:]))
fig, ax = plt.subplots()

# Desenho inicial do grafo
cores_nos = []
for node in G.nodes:
    if node == source or node == target:
        cores_nos.append("lightgreen")
    elif node in caminho:
        cores_nos.append("yellow")
    else:
        cores_nos.append("lightgray")
nx.draw(G, pos, ax=ax, with_labels=True, node_color=cores_nos, edge_color="gray")
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)

# Animação
def atualizar(frame):
    if frame < len(arestas_do_caminho):
        edge = arestas_do_caminho[frame]
        nx.draw_networkx_edges(
            G, pos,
            edgelist=[edge],
            edge_color='red',
            width=4,
            ax=ax
        )

ani = animation.FuncAnimation(
    fig, atualizar,
    frames=len(arestas_do_caminho),
    interval=500,
    repeat=False
)

plt.show()
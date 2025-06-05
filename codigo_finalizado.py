import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

G = nx.Graph()
G.add_edge("A", "G", weight=6)
G.add_edge("B", "C", weight=7)
G.add_edge("A", "C", weight=8)
G.add_edge("D", "E", weight=7)
G.add_edge("E", "F", weight=7)
G.add_edge("E", "C", weight=7)
G.add_edge("B", "D", weight=8)
G.add_edge("A", "F", weight=6)
G.add_edge("C", "H", weight=6)
G.add_edge("G", "H", weight=7)
G.add_edge("B", "I", weight=6)
G.add_edge("I", "H", weight=9)
G.add_edge("D", "J", weight=7)
G.add_edge("K", "J", weight=7)
G.add_edge("K", "E", weight=8)
G.add_edge("K", "L", weight=7)
G.add_edge("L", "F", weight=7)
G.add_edge("L", "M", weight=6)
G.add_edge("N", "M", weight=7)
G.add_edge("N", "K", weight=6)
G.add_edge("N", "O", weight=7)
G.add_edge("O", "J", weight=5)
G.add_edge("G", "P", weight=9)
G.add_edge("P", "Q", weight=7)
G.add_edge("Q", "A", weight=7)
G.add_edge("Q", "R", weight=7)
G.add_edge("R", "F", weight=8)
G.add_edge("R", "S", weight=7)
G.add_edge("S", "L", weight=7)
G.add_edge("S", "T", weight=7)
G.add_edge("T", "M", weight=8)

G.add_edge("T", "U", weight=1)
G.add_edge("S", "U", weight=1)
G.add_edge("R", "U", weight=1)
G.add_edge("Q", "U", weight=1)
G.add_edge("P", "U", weight=1)
# I B D J O
G.add_edge("I", "V", weight=1)
G.add_edge("B", "V", weight=1)
G.add_edge("D", "V", weight=1)
G.add_edge("J", "V", weight=1)
G.add_edge("O", "V", weight=1)

G.add_edge("V", "W", weight=1)
G.add_edge("V", "X", weight=1)
G.add_edge("V", "Y", weight=1)
G.add_edge("V", "Z", weight=1)

G.add_edge("Z", "X", weight=1)
G.add_edge("X", "W", weight=1)
G.add_edge("W", "Y", weight=1)

G.add_edge("U", "AA", weight=1)
G.add_edge("U", "AB", weight=1)
G.add_edge("U", "AC", weight=1)
G.add_edge("U", "AD", weight=1)

G.add_edge("AA", "AB", weight=1)
G.add_edge("AB", "AC", weight=1)
G.add_edge("AC", "AD", weight=1)

caminho = nx.dijkstra_path(G, source="I", target="AD", weight="weight")
print("Menor caminho de A até AD:", caminho)

pos = nx.spring_layout(G, seed=42)


arestas_do_caminho = list(zip(caminho, caminho[1:]))


labels = nx.get_edge_attributes(G, 'weight')

pos = nx.spring_layout(G, seed=42)

fig, ax = plt.subplots()

# Desenha o grafo todo de fundo (nós e arestas cinzas)
cores_nos = []
for node in G.nodes:
    if node == "I" or node == "AD":
        cores_nos.append("lightgreen")  # origem e destino
    else:
        cores_nos.append("lightgray")  # os demais
nx.draw(G, pos, ax=ax, with_labels=True, node_color=cores_nos, edge_color="gray")


# Rótulos de peso das arestas
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)


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
    fig,              # figura que vai ser animada
    atualizar,        # função chamada a cada frame
    frames=len(arestas_do_caminho),  # número de etapas
    interval=500,     # tempo entre uma aresta e outra (milissegundos)
    repeat=False      # não repetir a animação
)
plt.show()


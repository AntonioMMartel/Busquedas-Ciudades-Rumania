# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

ab = search.GPSProblem('A', 'B'
                       , search.romania)

#Imprimes la busqueda de A a B con BFS
print("BFS:", search.breadth_first_graph_search(ab)[0].path(),
      "Nodos visitados:", search.breadth_first_graph_search(ab)[1])
#Imprimes la busqueda de A a B con DFS
print("DFS:", search.depth_first_graph_search(ab)[0].path(),
      "Nodos visitados:", search.depth_first_graph_search(ab)[1])
#Imprimes la busqueda de A a B con ramificación y acotación
print("Ramifiación y acotación:", search.ramificacion_y_acotacion_search(ab)[0].path(),
      "Nodos visitados:", search.ramificacion_y_acotacion_search(ab)[1])
#Imprimes la busqueda de A a B con ramificación y acotación con heurística
print("Ramifiación y acotación con heurística:", search.ramificacion_y_acotacion_informada_search(ab)[0].path(),
      "Nodos visitados:", search.ramificacion_y_acotacion_informada_search(ab)[1])


# Result: (No es muy de informaticos calcularlo a mano pero bueno)
# BFS:
# [<Node B>, <Node F>, <Node S>, <Node A>] : 140 + 99 + 211 = 590

# DFS:
# [<Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>] =
# 118 + 111 + 70 + 75 + 120 + 138 + 101 = 733

# Ramificacion y acotacion:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418

# Ramificacion y acotacion heuristica:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 211 + 99 + 140 = 418
# Este llega 4 veces más rápido.

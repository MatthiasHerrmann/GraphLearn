from ego.decomposition.paired_neighborhoods import decompose_neighborhood
import networkx as nx
from graphlearn import cipcorevector as ccv
import graphlearn.lsgg_core_interface_pair as cip 
import structout as so
import sys
#sys.path.insert(0, 


### Graph bauen und schauen ob vektorisierbar

def add_labels(g, s):
    ascii = "abcdefghijklmnopqrstuvwxyz"
    bla = "ba"
    ac = 0
    for n, l in zip(g.nodes(), s):
        g.nodes[n]['label'] = l
    for a, b in g.edges():
        g[a][b]['label'] = bla[ac]
        ac += 1
    return g


def test_vectorize():
    new_cipselector = lambda x, y:x
    decomposer = decompose_neighborhood
    g = nx.path_graph(3)
#    g.add_edge(1,2,label="b")
    g = add_labels(g, "243")
    print(so.graph.make_picture(g))
    exg = cip._edge_to_vertex(g)
    print(so.graph.make_picture(exg))
    target_vector = ccv.vertex_vec(g, decomposer)
    print(target_vector.__dict__)
    
#    print(target_vector.core_vec)


test_vectorize()

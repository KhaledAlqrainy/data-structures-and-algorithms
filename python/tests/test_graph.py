import pytest

from code_challenges.graph.graph import *


def test_add_node():
    expected = 'a'
    graph = Graph()
    actual = graph.add_node('a').value
    assert actual == expected

def test_add_edge_exists():
    graph = Graph()
    node_a = graph.add_node('a')
    node_b = graph.add_node('b')
    graph.add_edge(node_a,node_b)
    expected = ['b',0]
    edge = graph.adjacency_list[node_a][0]
    actual = [edge.vertex.value,edge.weight]
    assert actual == expected

def test_add_edge_does_not_exists():
    with pytest.raises(KeyError):
        graph = Graph()
        node_a = graph.add_node('a')
        node_b = Vertex('b')
        graph.add_edge(node_a,node_b)

def test_get_nodes(graph):
    expected = ['a', 'b', 'c', 'd', 'e', 'f']
    nodes = graph.get_nodes()
    actual = []
    for node in nodes:
        actual.append(node.value)
    assert actual == expected

def test_get_neighbors(graph):
    expected = ['c', ['a', 0], ['b', 0], ['e', 0]]
    nodes = graph.get_nodes()
    for node in nodes:
        if node.value == 'c':
            node_c = node
    neighbors = graph.get_neighbors(node_c)
    actual = [node_c.value]
    for edge in neighbors:
        actual += [[edge.vertex.value,edge.weight]]
    assert actual == expected

def test_get_neighbors_with_wieght(graph_weight):
    expected = ['c', ['a', 1], ['b', 5], ['e', 9]]
    nodes = graph_weight.get_nodes()
    for node in nodes:
        if node.value == 'c':
            node_c = node
    neighbors = graph_weight.get_neighbors(node_c)
    actual = [node_c.value]
    for edge in neighbors:
        actual += [[edge.vertex.value,edge.weight]]
    assert actual == expected

def test_get_size(graph):
    expected = 6
    actual = graph.size()
    assert actual == expected

def test_empty_graph():
    graph = Graph()
    actual = graph.get_nodes()
    assert not actual

def test_get_neighbors2():

    graph = Graph()

    banana = graph.add_node('Forza')

    apple = graph.add_node('Milan')

    graph.add_edge(apple, banana, 44)

    neighbors = graph.get_neighbors(apple)

    assert len(neighbors) == 1

    neighbor_edge = neighbors[0]

    assert neighbor_edge.vertex.value == 'Forza'

    assert neighbor_edge.weight == 44

def test_graph_business_trip():
    graph = Graph()
    p = graph.add_node('Pandora')
    a = graph.add_node('Arendelle')
    m = graph.add_node('Metroville')
    nm = graph.add_node('New Monstropolis')
    no = graph.add_node('Naboo')
    nar = graph.add_node('Narnia')

    graph.add_edge(p, a, 150)
    graph.add_edge(p, m, 82)

    graph.add_edge(a, p , 150)
    graph.add_edge(a, nm ,42)
    graph.add_edge(a, m ,99)

    graph.add_edge(nm, a, 42)
    graph.add_edge(nm, no, 73)
    graph.add_edge(nm, m, 105)

    graph.add_edge(no, nm, 73)
    graph.add_edge(no, m, 26)
    graph.add_edge(no, nar, 250)
    
    graph.add_edge(nar, m, 37)
    graph.add_edge(nar, no, 250)

    graph.add_edge(m, p, 82)
    graph.add_edge(m, a, 99)
    graph.add_edge(m, nm, 105)
    graph.add_edge(m, no, 26)
    graph.add_edge(m, nar, 37)
    
    
    assert graph.business_trip([m,p])==[True,164]
    assert graph.business_trip([a,nm,no])==[True,230]
    assert graph.business_trip([no,p])==[False,0]
    assert graph.business_trip([nar,a,no])==[False,0]


def test_depth_first():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    g = graph.add_node('g')
    h = graph.add_node('h')

    graph.add_edge(a, b)
    graph.add_edge(a, d)

    graph.add_edge(b,a)
    graph.add_edge(b,c)
    graph.add_edge(b,d)

    graph.add_edge(c,b)
    graph.add_edge(c,g)
    
    graph.add_edge(d, a)
    graph.add_edge(d,b)
    graph.add_edge(d,e)
    graph.add_edge(d,h)
    graph.add_edge(d,f)
    
    graph.add_edge(f,d)
    graph.add_edge(f,h)

    graph.add_edge(h,f)
    graph.add_edge(h,d)

    graph.add_edge(e,d)
    assert graph.graph_depth_first(a)==['a', 'b', 'c', 'g', 'd', 'e', 'h', 'f']

@pytest.fixture
def graph():
    graph = Graph()
    node_a = graph.add_node('a')
    node_b = graph.add_node('b')
    node_c = graph.add_node('c')
    node_d = graph.add_node('d')
    node_e = graph.add_node('e')
    node_f = graph.add_node('f')
    graph.add_edge(node_a,node_c)
    graph.add_edge(node_a,node_d)
    graph.add_edge(node_b,node_c)
    graph.add_edge(node_b,node_f)
    graph.add_edge(node_c,node_e)
    graph.add_edge(node_d ,node_e)
    graph.add_edge(node_e,node_f)
    return graph
    
@pytest.fixture
def graph_weight():
    graph = Graph()
    node_a = graph.add_node('a')
    node_b = graph.add_node('b')
    node_c = graph.add_node('c')
    node_d = graph.add_node('d')
    node_e = graph.add_node('e')
    node_f = graph.add_node('f')
    graph.add_edge(node_a,node_c,1)
    graph.add_edge(node_a,node_d,3)
    graph.add_edge(node_b,node_c,5)
    graph.add_edge(node_b,node_f,7)
    graph.add_edge(node_c,node_e,9)
    graph.add_edge(node_d ,node_e,8)
    graph.add_edge(node_e,node_f,4)
    return graph


class Vertex:
    """
        Class for Adding a node to the graph
        Arguments: value
        Returns: The added node
    """

    def __init__(self,value):
        """
        Initialization for a Vertex to hold a value.
        """
        self.value = value

    def __str__(self):
        return f"{self.value}"

class Edge:

    """
    a class for Adding a new edge between two nodes in the graph
     If specified, assigning a weight to the edge
    Arguments: 2 nodes to be connected by the edge, weight (optional)
    Returns: nothing
    
    """

    def __init__(self,vertex,weight):

        self.vertex = vertex
        self.weight = weight

class  Graph:
    """
    Initialization for a hashmap to hold the vertices
    """

    def __init__(self):
        self.adjacency_list = {}

    def add_node(self,value):
        """
        Method for Adding a node to the graph
       Arguments: value
       Returns: The added node
       """
        node = Vertex(value)
        self.adjacency_list[node] = []
        return node

    def add_edge(self,node1=None,node2=None,weight1=0):

        """
        Adds an edge to the graph
        """

        if node1 not in self.adjacency_list:
            raise KeyError

        elif node2 not in self.adjacency_list:
            raise KeyError

        else:
            edge = Edge(vertex=node2,weight=weight1)
            self.adjacency_list[node1].append(edge)
            edge = Edge(vertex=node1,weight=weight1)
            self.adjacency_list[node2].append(edge)

    def get_nodes(self):
        """
        Method to get all nodes in Graph
        Arguments: None
        return: All nodes
     """
        return self.adjacency_list.keys()

    def get_neighbors(self,node):
        return self.adjacency_list.get(node,[])

    def size(self):
        return len(self.adjacency_list)

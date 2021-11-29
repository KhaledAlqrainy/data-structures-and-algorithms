class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def enqueue(self, value):

        """ Add an item to the rear fo the queue """

        node = Node(value)

        if not self.front:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = self.rear.next
    
    def dequeue(self):

        """ deletes an from the rear of the queue """

        if self.is_empty():
            return ("Queue is empty")
        else:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value

        
    
        
    def is_empty(self):

        """ Returns False if the queue is empty or False if it is not """

        if self.front:
            return False
        return True 

    

    def peek(self):

        """ Returns the value at the top without modifying the queue, raises an exception otherwise """

        if not self.is_empty():
          return self.front.value
    
        return ("Cannot peek an empty stack")
  
    def __str__(self):
        current = self.front
        items = []
        while current:
            items.append(str(current.value))
            current = current.next
        return "\n".join(items)

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
    
    def breadth_first_search(self, start_vertex):

        queue = Queue()
        visited = set()
        result = ''
        queue.enqueue(start_vertex)
        visited.add(start_vertex)

        while len(queue):
            current_vertex = queue.dequeue()
            result += f"{current_vertex.value} ,"
            neighbors = self.get_neighbors(current_vertex)

            for edge in neighbors:

                neighbor_vertex = edge.vertex
                if neighbor_vertex in visited:
                    continue
                else:
                    visited.add(neighbor_vertex)
                    queue.enqueue(neighbor_vertex)
                    
        return result



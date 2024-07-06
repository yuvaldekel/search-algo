class Node:
    nodes = 1
    

    def __init__(self, value, neighbors) -> None:
        self.__value = value
        self.__id = Node.nodes
        Node.nodes += 1      

#        if type(neighbors) != list:
#            neighbors = [neighbors]  

        self.__neighbors = neighbors


    @property
    def value(self):
        return self.__value
    
    
    @value.setter
    def value(self, new_value):
        self.__value = new_value


    @property
    def id(self):
        return self.__id
    
    
    @id.setter
    def id(self, new_id):
        self.__id = new_id

        
    @property
    def neighbors(self):
        return self.__neighbors


    def get_neighbors_id(self):
        return [neighbor.id for neighbor in self.__neighbors]


    def add_neighbor(self, new_neighbors):
        
        if type(new_neighbors) != list:
            new_neighbors = [new_neighbors]

        self.__neighbors.extend(new_neighbors)


    def remove_neighbor(self, neighbors_remove):

        if type(new_neighbors) != list:
            new_neighbors = [new_neighbors]
        
        for neighbor in neighbors_remove:
        
            if neighbor in self.__neighbors:
                self.__neighbors.remove(neighbor)


    def __str__(self):
        return f"id - {self.__id} value - {self.__value} neighbors - {self.get_neighbors_id()}"


class Graph:

    def __init__(self) -> None:
        self.nodes = {}


    def create_node(self, value, neighbors = None):
        neighbor_nodes = []

        if not neighbors:
            neighbors = []

        for neighbor in neighbors:

            if neighbor in self.nodes:
                neighbor_nodes.append(self.nodes[neighbor])

        node = Node(value, neighbor_nodes)
        self.add_node(node)


    def add_node(self, node):
        
        if node.id not in self.nodes:
            self.nodes[node.id] = node
                    
        for neighbor in node.neighbors:
            neighbor.add_neighbor(node)


    def remove_node(self, node_id):
        node = self.nodes[node_id]

        if node.id in self.nodes:
            del self.nodes[node]
        
        for neighbor in node.neighbors:
            neighbor.remove_neighbor(node)

    
    def __str__(self):
        string = ""

        for node in self.nodes.values():
            string = f"{string}{str(node)}\n"
        
        string = string.strip()

        return string


def main():
    g = Graph()

    g.create_node(5)
    g.create_node(5, [1])
    g.create_node(5, [1, 2])

    print(g)


if __name__ == "__main__":
    main()
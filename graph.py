class Node:
    nodes = 1
    

    def __init__(self, value, *neighbors) -> None:
        self.__value = value
        self.__id = Node.nodes
        Node.nodes += 1        
        self.__neighbors = list(neighbors)


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


    def add_neighbor(self, *new_neighbors):
        self.__neighbors.extend(list(new_neighbors))


    def remove_neighbor(self, *neighbors_remove):
        
        for neighbor in neighbors_remove:
            if neighbor in self.__neighbors:
                self.__neighbors.remove(neighbor)

    
    def __str__(self):
        return f"id - {self.__id} value - {self.__value} neighbors - {self.__neighbors}"


class Graph:


    def __init__(self) -> None:
        self.nodes = {}


    def add_node(self, node):
        pass


def main():
    n = Node(5)
    n1 = Node(5, 1)
    n2 = Node(5, 1, 2)

    n.add_neighbor(2, 3)
    n1.add_neighbor(3)

    print(n)
    print(n1)
    print(n2)


if __name__ == "__main__":
    main()
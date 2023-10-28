from typing import Dict,List




class Graph:
    def __init__(self, directed = False) :
        self.graph : Dict[str, list] = {}
        self.directed = directed
        
    def get_all(self):
        return self.graph.keys()
    
    def _check_exist(self, node:str):
        return node in self.graph.keys()            
        
    def add_node(self,node:str, directed:bool ):
        if self._check_exist(node):
            raise f"this node {node} already exists " 
        else:
            self.graph[node]=[]
        
    def add_edge(self, node1:str,node2:str):
        if  not self._check_exist(node1) or not self._check_exist(node2):
            raise f"the node{node1} or node{node2} doesn't exist"
            
        self.graph[node1].append(node2)
        
        if  not self.directed:
            self.graph[node2].append(node1)
            
    
    def node_degree(self, node):
        if not self._check_exist(node):
            raise "the node doesn't exist"
        
        return len(self.graph[node])

    def print_graph(self):
        print(self.graph)
    
    def is_connected(self) -> bool:
        track_keeper : Dict[str,bool] = {}
        # Initialize with all nodes marked as unvisited (False)
        for node in self.graph.keys():
            track_keeper[node] = False

        # Define a helper function for DFS
        def dfs(node):
            track_keeper[node] = True
            for neighbor in self.graph[node]:
                if not track_keeper[neighbor]:
                    dfs(neighbor)
            

        # Choose a starting node (you can choose any node in the graph)
        start_node = next(iter(self.graph.keys()))

        # Start DFS from the chosen node
        dfs(start_node)

        # Check if all nodes are visited (connected)
        return all(track_keeper.values())

            
    
    def shortest_path(self, node1, end_node)-> list:  #BFS, DFS
        if node1 not in self.graph or node1 not in self.graph:
            return None
        # Initialize distances and previous nodes
        # We initialize the distances dictionary with all nodes having a 
        # distance of infinity except for the start_node, which has a 
        # distance of 0. The previous dictionary keeps track of the
        # previous node on the path to each node.
        distances = { node :float('inf') for node in self.graph}
        previous = { None for node in self.graph}
        distances[node1] = 0
        
        #Sets are often used to keep track of which elements have been visited, 
        # processed, or encountered in some way during the execution of an algorithm
        # or code.
        visited = set()
        
        while len(visited) < len(self.graph):
            #In the Dijkstra's algorithm, current_node initially starts as None because
            # we're looking for the unvisited node with the smallest distance,
            # and at the beginning of the algorithm, no nodes are visited yet.
            current_node = None
            for node in self.graph:
                #we want to update the table of address for the nearest node
                #so the condition is if the node is not visited before and the 
                #cost of it is less than infinity, update it replace the current node with the node
                if node not in visited and( current_node == None or distances[node] < distances[current_node]):
                    current_node = node
                    
                if distances[current_node] == float('inf'):
                    break # All remaining unvisited nodes are inaccessible
                visited.add(current_node)
                
                # Update distances to neighbors
                for neighbor in self.graph[current_node]:
                    potential_distance = distances[current_node]+1
                    if potential_distance < distances[neighbor]:
                        distances[neighbor] = potential_distance
                        previous[neighbor] = current_node
                        
                        
        path = []
        current_node = end_node
        while previous[current_node] is not None:
            path.insert(0,current_node)
            current_node = previous[current_node]
            
        if path:
            path.insert(0,node1)
            
        return path
            
        
                    
                        
                
            
            
        
        
        
g = Graph()
g.add_node("1", False)
g.add_node("2", False )
g.add_node("3", False)
g.add_node("4", False)
g.add_edge("1","2")
g.add_edge("2","4")
g.add_edge("3","1")
g.add_edge("4","1")
print("1" in g.get_all())
g.print_graph()
print(g.is_connected())
print("---------")
print(g.shortest_path(1,4))

'''
https://www.youtube.com/watch?v=j0IYCyBdzfA
'''

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        # print("Graph Dict:", self.graph_dict)
        
    def get_paths(self, start, end, path=[]):
        path = path + [start]
        
        # simplest case
        if start == end:
            return [path]
        
        # if city not found as a starting point 
        if start not in self.graph_dict:
            return []
        
        paths = []
        
        for node in self.graph_dict[start]: #accessing the array
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        
        return paths
            
if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
        ]
    
    route_graph = Graph(routes)
    
    start = "Mumbai"
    end = "Mumbai"
    paths = route_graph.get_paths(start, end)
    print(paths)
    

import collections

class DirectedGraph:
    def __init__(self, numnodes, edges):
        self.numnodes = numnodes
        self.adj = DirectedGraph._create_adjacencies(edges)

    @staticmethod
    def _create_adjacencies(edges):
        mydict = collections.defaultdict(list)
        for edge in edges:
            mydict[edge[0]].append(edge[1])
        mydict.default_factory = None
        return mydict

    def isCyclic(self):
        visited_nodes = set()
        stack_nodes = set()

        for node in self.adj:
            if node not in visited_nodes:
                cyclic = self.check_node(node, visited_nodes, stack_nodes)
                if cyclic:
                    return True

        return False

    def check_node(self, node, visited_nodes, stack_nodes):
        visited_nodes.add(node)
        stack_nodes.add(node)

        for neighbor in self.adj.get(node, []):
            if neighbor in stack_nodes:
                return True
            elif self.check_node(neighbor, visited_nodes, stack_nodes):
                return True

        stack_nodes.remove(node)
        return False


if __name__ == '__main__':
    mygraph = DirectedGraph(10, [[0,1], [1,2], [2,3], [3,1], [6,9]])
    print(mygraph.isCyclic())
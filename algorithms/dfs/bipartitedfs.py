from algorithms.ugraph import UGraph

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class BipartiteDFS:
    """"
    This class checks whether a graph G is bipartite.
    """

    def __init__(self, g: UGraph):
        self.isBipartite = True
        self.color = [False]*g.V
        self.marked = [False] * g.V
        self.edgeTo = [None] * g.V
        self.g = g
        self.odd_cycle = []
        for i in range(0, g.V):
            if not self.marked[i]:
                self.dfs(self.g, i)
        self.check(g)

    def dfs(self, g, v: int):
        self.marked[v] = True
        for node in g.close(v):
            # We found an odd cycle graph
            if len(self.odd_cycle) > 0:
                return

            if not self.marked[node]:
                self.edgeTo[node] = v
                self.color[node] = not self.color[v]
                self.dfs(g, node)
            elif self.color[v] == self.color[node]:
                # Whoa, we found a odd-cycle graph dude.
                self.isBipartite = False
                self.odd_cycle.append(node)
                x = v
                while x != v:
                    self.odd_cycle.append(x)
                    x = self.edgeTo[x]
                self.odd_cycle.append(node)
        pass

    def check(self, g):
        if self.isBipartite:
            for node_index in range(0, self.g.num_V()):
                for adj_node in self.g.close(node_index):
                    if self.color[node_index] == self.color[adj_node]:
                        raise "Wait, this isn't bipartite"
        else:
            pass

    # private boolean check(Graph G) {
    #     // graph is bipartite
    #     if (isBipartite) {
    #         for (int v = 0; v < G.V(); v++) {
    #             for (int w : G.adj(v)) {
    #                 if (color[v] == color[w]) {
    #                     System.err.printf("edge %d-%d with %d and %d in same side of bipartition\n", v, w, v, w);
    #                     return false;
    #                 }
    #             }
    #         }
    #     }

    #     // graph has an odd-length cycle
    #     else {
    #         // verify cycle
    #         int first = -1, last = -1;
    #         for (int v : oddCycle()) {
    #             if (first == -1) first = v;
    #             last = v;
    #         }
    #         if (first != last) {
    #             System.err.printf("cycle begins with %d and ends with %d\n", first, last);
    #             return false;
    #         }
    #     }

    #     return true;
    # }

    def what_color(self, v):
        return self.color[v]

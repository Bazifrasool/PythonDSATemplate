class UnionFind:
    def __init__(self,n):
        self.nodes_list = [x for x in range(0,n)]
    def find_disjoint(self,vertex):
        if vertex == self.nodes_list[vertex]:
            return vertex
        else:
            val =self.find_disjoint(self.nodes_list[vertex])
            return val
    def union_disjoint(self,child,parent):
        self.nodes_list[child] = parent
        return
    def add_edge(self,edge):
        p1=self.find_disjoint(edge[0])
        p2=self.find_disjoint(edge[1])
        if(p1 != p2):
            self.union_disjoint(edge[0],edge[1])
        else:
            print(" Has a cycle")
            quit()
    def print_list(self):
        print(self.nodes_list)

uf = UnionFind(3)
uf.add_edge([0,1])
uf.add_edge([1,2])
uf.add_edge([0,2])
uf.print_list()
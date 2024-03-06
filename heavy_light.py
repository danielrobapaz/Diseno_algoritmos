import numpy as np
 
N = 1024
 
# Matrix representing the tree
tree = np.full((N, N), -1)
multiply = lambda x, y: x*y
_sum = lambda x, y: x+y

class Node:
    def __init__(self):
        self.par = None  # Parent of this node
        self.depth = None  # Depth of this node
        self.size = None  # Size of subtree rooted with this node
        self.pos_segbase = None  # Position in segment tree base
        self.chain = None
 
# Initialize nodes
node = [Node() for _ in range(N)]
 
class Edge:
    def __init__(self):
        self.weight = None  # Weight of Edge
        self.deeper_end = None  # Deeper end
 
# Initialize edges
edge = [Edge() for _ in range(N)]
 
class SegmentTree:
    def __init__(self):
        self.base_array = np.zeros(N)
        self.tree = np.zeros(6*N)
 
# Initialize segment tree
s = SegmentTree()
 
# Function to add edges to the tree
def addEdge(e, u, v, w):
    tree[u-1][v-1] = e-1
    tree[v-1][u-1] = e-1
    edge[e-1].weight = w
 
# Recursive function for DFS on the tree
def dfs(curr, prev, dep, n):
    node[curr].par = prev
    node[curr].depth = dep
    node[curr].size = 1
 
    for j in range(n):
        if j != curr and j != node[curr].par and tree[curr][j] != -1:
            edge[tree[curr][j]].deeper_end = j
            dfs(j, curr, dep+1, n)
            node[curr].size += node[j].size
 
# Recursive function that decomposes the Tree into chains
def hld(curr_node, id, edge_counted, curr_chain, n, chain_heads):
    if chain_heads[curr_chain[0]] == -1:
        chain_heads[curr_chain[0]] = curr_node
 
    node[curr_node].chain = curr_chain[0]
    node[curr_node].pos_segbase = edge_counted[0]
    s.base_array[edge_counted[0]] = edge[id].weight
    edge_counted[0] += 1
 
    spcl_chld = -1
    spcl_edg_id = None
    for j in range(n):
        if j != curr_node and j != node[curr_node].par and tree[curr_node][j] != -1:
            if spcl_chld == -1 or node[spcl_chld].size < node[j].size:
                spcl_chld = j
                spcl_edg_id = tree[curr_node][j]
 
    if spcl_chld != -1:
        hld(spcl_chld, spcl_edg_id, edge_counted, curr_chain, n, chain_heads)
 
    for j in range(n):
        if j != curr_node and j != node[curr_node].par and j != spcl_chld and tree[curr_node][j] != -1:
            curr_chain[0] += 1
            hld(j, tree[curr_node][j], edge_counted, curr_chain, n, chain_heads)
 
# Recursive function that constructs Segment Tree for array[ss..se)
def construct_ST(ss, se, si):
    if ss == se-1:
        s.tree[si] = s.base_array[ss]
        return s.base_array[ss]
 
    mid = (ss + se) // 2
    s.tree[si] = max(construct_ST(ss, mid, si*2), construct_ST(mid, se, si*2+1))
    return s.tree[si]
 
 
# Function to get the LCA of nodes u and v
def LCA(u, v, n):
    LCA_aux = np.full(n+5, -1)
 
    if node[u].depth < node[v].depth:
        u, v = v, u
 
    while u != -1:
        LCA_aux[u] = 1
        u = node[u].par
 
    while v:
        if LCA_aux[v] == 1:
            break
        v = node[v].par
 
    return v
 
# Recursive function to get the minimum value in a given range of array indexes
def RMQUtil(ss, se, qs, qe, index, fun):
    if qs <= ss and qe >= se-1:
        return s.tree[index]
 
    if se-1 < qs or ss > qe:
        return -1
 
    mid = (ss + se) // 2
    return fun(RMQUtil(ss, mid, qs, qe, 2*index, fun), RMQUtil(mid, se, qs, qe, 2*index+1, fun))
 
# Return minimum of elements in range from index qs (query start) to qe (query end)
def RMQ(qs, qe, n, fun):
    if qs < 0 or qe > n-1 or qs > qe:
        print("Invalid Input")
        return -1
 
    return RMQUtil(0, n, qs, qe, 1, fun)
 
# Function to move from u to v keeping track of the maximum
def crawl_tree(u, v, n, chain_heads, fun, init_value):
    chain_v = node[v].chain
    ans = init_value
 
    while True:
        chain_u = node[u].chain
 
        if chain_u == chain_v:
            if u != v:
                ans = fun(RMQ(node[v].pos_segbase+1, node[u].pos_segbase, n, fun), ans)
            break
 
        else:
            ans = fun(ans,RMQ(node[chain_heads[chain_u]].pos_segbase, node[u].pos_segbase, n, fun))
            u = node[chain_heads[chain_u]].par
 
    return ans

# Function for MAX_EDGE query
def forall(u, v, n, chain_heads):
    lca = LCA(u, v, n)
    ans = crawl_tree(u, lca, n, chain_heads, multiply, 1) * crawl_tree(v, lca, n, chain_heads, multiply, 1)
    return ans > 0
 
def exists(u, v, n, chain_heads):
    lca = LCA(u, v, n)
    ans = crawl_tree(u, lca, n, chain_heads, _sum, 0) + crawl_tree(v, lca, n, chain_heads, _sum, 0)
    return ans > 0

def main():
    n = 11
    
    t, f = 1, 0
    addEdge(1, 1, 2, t)
    addEdge(2, 1, 3, f)
    addEdge(3, 1, 4, f)
    addEdge(4, 2, 5, f)
    addEdge(5, 2, 6, t)
    addEdge(6, 3, 7, t)
    addEdge(7, 6, 8, t)
    addEdge(8, 7, 9, t)
    addEdge(9, 8, 10, f)
    addEdge(10, 8, 11, t)
    
    
    root = 0
    parent_of_root = -1
    depth_of_root = 0
 
    dfs(root, parent_of_root, depth_of_root, n)
    chain_heads = np.full(N, -1)
 
    edge_counted = [0]
    curr_chain = [0]
 
    hld(root, n-1, edge_counted, curr_chain, n, chain_heads)
 
    construct_ST(0, edge_counted[0], 1)
 
    u = 8
    v = 10

    print(f"forall({u}, {v}) = {forall(u-1, v-1, n, chain_heads)}")
    print(f"exists({u}, {v}) = {exists(u-1, v-1, n, chain_heads)}")


if __name__ == "__main__":
    main()
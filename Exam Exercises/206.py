import sys

V = []
Adj = []
V_idx = {} 


# strip() - removes spaces in front or behind
# split() - splits words into differenet array elements

for line in sys.stdin:
    A = line.strip().split()
    for v in A:
        # v is a string, vertex name
        if not v in V_idx:
            V_idx[v] = len(V)
            V.append(v)
            Adj.append([])
    
    v_i = V_idx[A[0]]
    for i in range(1, len(A)):
        u_i = V_idx[A[i]]
        Adj[v_i].append(u_i)
        Adj[u_i].append(v_i)

def find_3_cycle():
    
    for u in range(len(V)):
        for v in Adj[u]:
            for w in Adj[v]:
                for x in Adj[w]:
                    if x == u:
                        return True
    
    return False
subgraphs=[]
def dfs(graph, start, end):
    fringe = [(start, [])]
    while fringe:
        state, path = fringe.pop()
        if path and state == end:
            yield path
            continue
        for next_state in graph[state]:
            if next_state in path:
                continue
            fringe.append((next_state, path+[next_state]))
    

graph = { 1: [2, 3, 5], 2: [1], 3: [1], 4: [2], 5: [2] }
vertex=[1,2,3,4,5]
vertices=[1,2,3,4,5]
cycles = [[node]+path  for node in graph for path in dfs(graph, node, node)]
print("cycles present in graph ",cycles)
x=len(cycles)

def findchain(v,a):
   
    if graph[v]==[0]:
        return
    u=graph[v]
    le=len(graph[v])
    for j in range(le):
        f=0
        for k in cycles:
            s=a
            if k[0]==u[j]:
                t=s+k
                subgraphs.append(t)
                f=1
        if f==0:
            s=a
            t1=s+graph[vertices[i]]
            subgraphs.append(t1)
            findchain(graph[vertices[i]],t1)
    return
prev=0
for i in range(x):
    y=cycles[i][0]
    if prev!=y and y in vertices:
        vertices.remove(y)
    prev=y
#print(vertices)
l=len(vertices)
for i in range(l):
    a=[]
    a.append(vertices[i])
    le=len(graph[vertices[i]])
    findchain(vertices[i],a)
#print(subgraphs)
for i in cycles:
    p=len(i)
    for j in range(2,p):
        subgraphs.append(i[0:j])
        #print(i[0:j])
    for k in range(1,p):  
        for j in range(k+2,p+1):
            subgraphs.append(i[k:j])
#print(subgraphs)
subgraphs=subgraphs+cycles
print("All subgraphs present in the graph ",subgraphs)
            
        



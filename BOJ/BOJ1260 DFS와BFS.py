n,m,v=map(int,input().split())
#n 노드수, m=간선수, v=시작노드

matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]  #인덱스 1부터할려고 n+1
visit=[0 for _ in range(n+1)]
for _ in range(m):
    x,y=map(int,input().split())
    matrix[x][y]=1
    matrix[y][x]=1

# print(matrix)

def dfs(v):
    print(v,end=' ')
    visit[v]=1
    for i in range(1,n+1):
        if visit[i]==0 and matrix[v][i]==1:
            dfs(i)

def bfs(v):
    queue=[v]
    visit[v]=0
    while(queue):
        v=queue[0]
        print(v,end=' ')
        del queue[0]
        for i in range(1,n+1):
            if visit[i]==1 and matrix[v][i]==1:
                queue.append(i)
                visit[i]=0

dfs(v)
print()
bfs(v)

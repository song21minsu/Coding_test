n=int(input()) #컴퓨터의수
m=int(input()) #컴퓨터 쌍의 수
matrix=[[0 for _ in range(n+1)] for _ in range(n+1)] #연결된 쌍 행렬

for _ in range(m):
    x,y=map(int,input().split())
    matrix[x][y]=1
    matrix[y][x]=1

print(matrix)
def bfs(v):
    queue=[v]
    visit=[]
    cnt=0
    while queue:
        q=queue.pop(0)
        visit.append(q)

        for i in range(1,n+1):
            if matrix[q][i] and i not in visit and i not in queue:
                queue.append(i)
                cnt+=1

    print(visit)
    return cnt

print(bfs(1))

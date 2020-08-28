n,m,k=map(int,input().split())
matrix=[[0]*m for _ in range(n)]
for _ in range(k):
    x,y=map(int,input().split())
    matrix[x][y]=1
visit=[[0]*m for _ in range(n)]

dx=[-1,0,1,0]
dy=[0,-1,0,1]

from collections import deque
def bfs(x,y):
    cnt=0
    q=deque()
    q.append((x,y))
    visit[x][y]=1
    cnt+=1
    while q:
        x,y=q.popleft()

        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]

            if 0<=nx<n and 0<=ny<m:
                if matrix[nx][ny]==1 and visit[nx][ny]==0:
                    visit[nx][ny]=1
                    q.append((nx,ny))

    return cnt
tmp=0
for i in range(n):
    for j in range(m):
        if matrix[i][j]==1 and visit[i][j]==0:
            tmp+=bfs(i,j)
print(tmp)

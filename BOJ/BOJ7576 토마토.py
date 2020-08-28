m,n=map(int,input().split())

matrix=[]

for _ in range(n):
    matrix.append(list(map(int,input().split())))

dx=[-1,0,1,0]
dy=[0,-1,0,1]


def bfs(cnt):
    if cnt==0:
        return 0
    while q:
        x,y=q.popleft()
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]

            if 0<=nx<n and 0<=ny<m:
                if matrix[nx][ny]==0:
                    q.append((nx,ny))
                    matrix[nx][ny]=matrix[x][y]+1
                    cnt-=1
                    if cnt==0:
                        return matrix[nx][ny]-1
    return -1

from collections import deque
q=deque()

cnt=0
for i in range(n):
    for j in range(m):
        if matrix[i][j]==1:
            q.append((i,j))
        elif matrix[i][j]==0:
            cnt+=1

print(bfs(cnt))

# for i in range(n):
#     print(matrix[i])

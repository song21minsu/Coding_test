n=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input())))
visit=[[0]*n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x,y):
    from collections import deque
    q=deque()
    q.append((x,y))
    visit[x][y]=1
    tmp=0

    while q:
        x,y=q.popleft()
        tmp+=1

        #사방위 탐색
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]

            #매트릭스 범위 나갔는지 확인
            if 0<=nx<n and 0<=ny<n:
                #매트릭스에 있고 visit에 없으면
                if matrix[nx][ny]==1 and visit[nx][ny]==0:
                    q.append((nx,ny))
                    visit[nx][ny]=1
    return tmp

arr=[]
for i in range(n):
    for j in range(n):
        if matrix[i][j]==1 and visit[i][j]==0:
            arr.append(bfs(i,j))

arr.sort()

print(len(arr))
for i in arr:
    print(i)

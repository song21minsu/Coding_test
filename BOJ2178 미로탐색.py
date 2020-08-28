n,m=map(int,input().split())
matrix=[[0]*m for _ in range(n)]
visit=[[0]*m for _ in range(n)]

for i in range(n):
    matrix[i]=(list(map(int,input())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visit[0][0]=1
def bfs(x,y):
    from collections import deque
    q=deque()
    q.append((x,y))

    while q:
        x,y=q.popleft()
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]

            if 0<=nx<n and 0<=ny<m:
                if matrix[nx][ny]==1 and visit[nx][ny]==0:
                    q.append((nx,ny))
                    visit[nx][ny]=visit[x][y]+1
    return visit[n-1][m-1]

print(bfs(0,0))

# for i in range(n):
#     print(visit[i])


#
# n,m=map(int,input().split())
# matrix=[[0]*m for _ in range(n)]
# visit=[[0]*m for _ in range(n)]
#
# for i in range(n):
#     matrix[i]=(list(map(int,input())))
#
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
# visit[0][0]=1
# def bfs(x,y):
#     from collections import deque
#     q=deque()
#     q.append((x,y,1))
#
#     while q:
#         x,y,c=q.popleft()
#         for d in range(4):
#             nx=x+dx[d]
#             ny=y+dy[d]
#
#             if 0<=nx<n and 0<=ny<m:
#                 if matrix[nx][ny]==1 and visit[nx][ny]==0:
#                     if nx==n-1 and ny==m-1:
#                         return c+1
#                     else:
#                         q.append((nx,ny,c+1))
#
# print(bfs(0,0))

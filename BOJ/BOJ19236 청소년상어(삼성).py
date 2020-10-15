from copy import deepcopy
from collections import deque
answer=0

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]

matrix=[[0]*4 for _ in range(4)]
fish=[[0,0,0] for _ in range(16)]
for i in range(4):
    s=list(map(int,input().split()))
    for j in range(0,8,2):
        matrix[i][j//2]=s[j]    #매트릭스안 물고기 위치
        fish[s[j]-1]=[i,j//2,s[j+1]-1]  #물고기 1~16 좌표(x,y) 및 방향(8방위)

q=deque()
shark=[0,0, fish[matrix[0][0]-1][2]]
fish[matrix[0][0]-1][2]=-1
score=matrix[0][0]
matrix[0][0]=-1

q.append((matrix,shark,score,fish))

while q:
    nmatrix,nshark,nscore,nfish=q.popleft()

    for i in range(16):
        if nfish[i][2]==-1:
            continue
        else:
            x,y,d=nfish[i]
            nx=x+dx[d]
            ny=y+dy[d]
            if (-1<nx<4 and -1<ny<4) and nmatrix[nx][ny]!=-1:
                if nmatrix[nx][ny]!=0:
                    tmp=nmatrix[nx][ny]
                    nmatrix[nx][ny]=i+1
                    nmatrix[x][y]=tmp
                    nfish[i][0]=nx
                    nfish[i][1]=ny
                    nfish[tmp-1][0]=x
                    nfish[tmp-1][1]=y
                else:
                    nfish[i][0]=nx
                    nfish[i][1]=ny
                    nmatrix[x][y]=0
                    nmatrix[nx][ny]=i+1
            else:
                for _ in range(1,8):
                    d=(d+1)%8
                    nx=x+dx[d]
                    ny=y+dy[d]
                    if (-1 < nx < 4 and -1 < ny < 4) and nmatrix[nx][ny] != -1:
                        if nmatrix[nx][ny]!=0:
                            tmp=nmatrix[nx][ny]
                            nmatrix[nx][ny] = i + 1
                            nmatrix[x][y] = tmp
                            nfish[i][0] = nx
                            nfish[i][1] = ny
                            nfish[tmp - 1][0] = x
                            nfish[tmp - 1][1] = y
                            nfish[i][2]=d
                        else:
                            nfish[i][0]=nx
                            nfish[i][1]=ny
                            nfish[i][2]=d
                            nmatrix[nx][ny]=i+1
                            nmatrix[x][y]=0
                        break

    sx,sy,sd=nshark
    flag=1
    for c in range(1,4):
        nsx=sx+c*dx[sd]
        nsy=sy+c*dy[sd]
        if 0<=nsx<4 and 0<=nsy<4 and nmatrix[nsx][nsy]>0:
            nmatrix2=deepcopy(nmatrix)
            nfish2=deepcopy(nfish)
            nmatrix2[sx][sy]=0
            tmp=nmatrix2[nsx][nsy]
            nsd=nfish2[tmp-1][2]
            nfish2[tmp-1][2]=-1
            nmatrix2[nsx][nsy]=-1
            q.append((nmatrix2,[nsx,nsy,nsd],nscore+tmp,nfish2))
            flag=0

    if flag:
        answer=max(answer,nscore)

print(answer)


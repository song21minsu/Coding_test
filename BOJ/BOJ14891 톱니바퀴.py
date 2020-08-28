import sys

from collections import deque
# q=[deque([[int(i) for i in sys.stdin.readline().rstrip()] for i in range(4)])]
q=[deque(map(int,sys.stdin.readline().rstrip())) for _ in range(4)]
# print(q)    # 1은 N극 0은 S극
k=int(sys.stdin.readline())
f=deque()
for _ in range(k):
    f.append(list(map(int,sys.stdin.readline().split())))
# print(f)
while f:
    #돌릴 톱니, 방향(1:시계,-1:반시계)
    num,direct=f.popleft()
    num-=1
    tmp2=q[num][2]  # 시작 2번(오른)
    tmp6=q[num][6]  # 시작 6번(왼)
    q[num].rotate(direct)   #시작 바퀴 회전

    tmp_direct=direct

    #시작바퀴의 왼쪽
    for i in range(num-1,-1,-1):
        if q[i][2]!=tmp6:
            tmp6=q[i][6]
            q[i].rotate(-tmp_direct)
            tmp_direct*=-1
        else:
            break

    tmp_direct=direct

    #시작바퀴의 오른쪽
    for i in range(num+1,4):
        if q[i][6]!=tmp2:
            tmp2=q[i][2]
            q[i].rotate(-tmp_direct)
            tmp_direct*=-1
        else:
            break
cnt=0
for i in range(4):
    if q[i][0]==1:
        cnt+=pow(2,i)
print(cnt)

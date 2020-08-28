from collections import deque
import sys
n,m=map(int,sys.stdin.readline().split())
f=list(map(int,sys.stdin.readline().split()))
q=deque(range(1,n+1))
cnt=0

for i in range(len(f)):
    if f[i] ==q[0]:
        q.popleft()
        continue

    q_idx = q.index(f[i])

    if q_idx > len(q)//2:
        q.rotate(len(q) - q_idx)
        cnt+=(len(q)-q_idx)

    else:
        q.rotate(-q_idx)
        cnt+=q_idx
    q.popleft()

print(cnt)

n=int(input())              #시험장 수
arr=list(map(int,input().split()))  # 시험장 당 응시자 수
b,c=map(int,input().split())    # 일단 b 1개 무조건 넣고 생각


cnt=0
for i in range(n):
    if arr[i]>0:
        arr[i]-=b           # 일단 총감독 하나 넣고 시작
        cnt+=1

    if arr[i]>0:
        cnt+=int(arr[i]/c)  # 몫만큼 더한다

        if arr[i]%c!=0:     # 나머지가있으면 감독관 한명 더 필요하다
            cnt+=1

print(cnt)
arr=[int(input()) for _ in range(9)]
answer=[]
# itertools 안쓰고 구현하기위해
def combi(arr,r):
    tmp=[]
    if r==1:
        for i in arr:
            tmp.append([i])
    elif r>1:
        for i in range(len(arr)-r+1):
            for j in combi(arr[i+1:],r-1):
                tmp.append([arr[i]]+j)

    return tmp

sol=combi(arr,7)

for i in sol:
    if sum(i)==100:
        answer.append(i)

for i in sorted(answer[0]):
    print(i)

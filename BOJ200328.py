#1157번
# alp=input().upper()
# arr=[]
# for i in set(alp):
#     arr.append(alp.count(i))
# if arr.count(max(arr))>1:
#     print("?")
# else:
#     top=arr.index(max(arr))
#     print(alp[top])

# n=int(input())
# a=list(map(int,input().split()))
# cnt=0
# for i in a:
#     tmp=0
#     if(i==1):
#         continue
#     for j in range(2,i+1):
#         if(i%j==0):
#             tmp+=1
#         if(tmp==1):
#             cnt+=1
# print(cnt)




while True:
    n=int(input())
    if n==0:
        break
    count = 0
    for i in range(n, 2*n+1):
        tmp = 0
        for j in range(n,i+1):
            if i % j ==0:
                tmp +=1

        if tmp == 1:
            count += 1
    print(count)

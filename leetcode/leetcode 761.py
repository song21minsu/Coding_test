from collections import deque
def makeLargestSpecial(S):
    q=deque(S)
    arr=[]
    q.popleft()
    q.pop()
    stack=deque()
    cnt=0
    for i in q:
        if i=='1':
            stack.append(i)
            cnt+=1
        elif i=='0':
            stack.append(i)
            cnt-=1
            if cnt==0:
                tmp=[]
                while stack:
                    tmp.append(stack.popleft())
                arr.append(''.join(tmp))
        arr=sorted(arr,reverse=True)

    answer='1'+''.join(arr)+'0'
    return answer

# print(makeLargestSpecial("110110100100"))
print(makeLargestSpecial("101010"))

#
# # <괄호>
#
# 110110100100
#
# 1011010010
#
# 10
# 110100
# 10
#
# 111010010100

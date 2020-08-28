while True:
    s=input()
    flag=0
    if s=='.':
        break
    arr=[]
    for i in s:
        if i=='(' or i=='[':
            arr.append(i)
        elif i==')':
            if arr and arr[-1] == '(':
                arr.pop()
            else:
                flag=1
                print('no')
                break
        elif i==']':
            if arr and arr[-1]=='[':
                arr.pop()
            else:
                flag=1
                print('no')
                break
    if flag==0:
        if not arr:
            print('yes')
        else:
            print('no')

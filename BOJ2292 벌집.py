n = int(input())
tmp=1
cnt=1
answer=1
if n==1:
    print(1)
else:
    while True:
        tmp+=cnt*6
        answer+=1
        if n<=tmp:
            break
        cnt+=1
    print(answer)

# 1     1
# 2~7   6
# 8~19  12
# 20~37 18


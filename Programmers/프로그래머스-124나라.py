def solution(n):
    answer=''
    while(n>0):

        a,b=divmod(n,3)
        if b==0:
            answer='4'+answer
            a-=1
        else:
            answer=str(b)+answer
        n=a
    return answer

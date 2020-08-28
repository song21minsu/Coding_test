def kthGrammar(n,k):
    if n==1:
        return 0
    if (k%2==0):
        return 1 if kthGrammar(n-1,k/2)==0 else 0
    else:
        return 0 if kthGrammar(n-1,(k+1)/2)==0 else 1

print(kthGrammar(1,1))
print(kthGrammar(2,1))
print(kthGrammar(2,2))
print(kthGrammar(4,5))


# 0부터 시작해서 0은 01로 변하고 1은 10으로 변하면서 계속 값이 증가합니다.
# 일단 반복되는 패턴을 찾으려고 했습니다.
#  row1 : 0
#  row2 : 01
#  row3 : 0110
#  row4 : 0110 1001
#  row5 : 0110 1001 1001 0110
#  row6 : 0110 1001 1001 0110 1001 0110 0110 1001
#  row7 : 0110 1001 1001 0110 1001 0110 0110 1001 1001 0110 0110 1001 0110 1001 1001 0110
# 다음과 같이 일정 패턴을 가지며 반복되는 모습을 확인할 수 있었습니다.
# 반복되는 성질을 이용하여 재귀적으로 입력받는 N과 K의 값을 줄여나가면서 값을 return 했습니다.

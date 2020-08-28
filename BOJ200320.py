# 백준 수학1단계

# import sys
#
# t= int(sys.stdin.readline())
#
# def hap(k,n):   #사람 수(people)는 호 수 (n) 합
#     if k==0:
#         return n
#     people=0
#     for i in range(1,n+1):
#         people+=hap(k-1,i)
#     return people
#
# for _ in range(t):
#     k= int(input())#층
#     n= int(input())#호
#     print(hap(k,n))
#
# 방법 2 이중포문

# import sys
# x=int(sys.stdin.readline())
#
# line=1
# while x>line:
#     x-=line
#     line+=1
#
# if line%2==0:
#     a=x
#     b=line-x+1
# else:
#     a=line-x+1
#     b=x
# print(str(a)+'/'+str(b))

# x=1       2    3       4    5    6    7
# [1/1], [1/2, 2/1], [3/1, 2/2, 1/3], [1/4, 2/3, 3/2, 4/1]
# 합은 모두 x+1
# 아래로   위로            아래로


#[1]           ->1
#[2,3,4,5,6,7]  ->6
#[8,....,19] -> 12
#[20,...,37] -> 18
#[38,...,61] -> 24

import sys
n=int(sys.stdin.readline())
sum=0
count=0
while n>sum:
    sum+=count*6
    count+=1
# https://oneshottenkill.tistory.com/27

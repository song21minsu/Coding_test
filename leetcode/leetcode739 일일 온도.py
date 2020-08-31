# import sys

def dailyTemperatures(T):
    arr=[0]*len(T)
    stack=[]

    for i,cur in enumerate(T):
        while stack and cur>T[stack[-1]]:
            last=stack.pop()
            arr[last]=i-last
        stack.append(i)

    return arr

print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# print(dailyTemperatures([55,38,53,81,61,93,97,32,43,78]))
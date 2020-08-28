import math
def solution(progresses, speeds):
    answer=[]
    arr=[]
    for i in progresses:
        arr.append(100-i)
    # print(arr)
    time=[]
    for i in range(len(arr)):
        time.append(math.ceil(arr[i]/speeds[i]))
    # print(time)
    while time:
        tmp=time.pop(0)
        cnt=1
        while time and tmp>=time[0]:
            time.pop(0)
            cnt+=1
        if len(time)==0:
            answer.append(cnt)
            break
        answer.append(cnt)
    return answer
# print(solution([93,30,55],[1,30,5]))

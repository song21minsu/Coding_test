def combinationSum(candidates,target):
    answer=[]

    def dfs(csum,index,path):
        # 종료
        if csum<0:
            return
        if csum==0:
            answer.append(path)
            return

        # 하나씩 후보자에서 빼서 재귀호출
        for i in range(index,len(candidates)):
            dfs(csum-candidates[i],i,path+[candidates[i]])

    dfs(target,0,[])
    return answer


candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates,target))
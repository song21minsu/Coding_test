def subsets(nums):
    answer=[]

    def dfs(index,path):
        # 경로 결과 추가
        answer.append(path)

        #경로 만들기
        for i in range(index,len(nums)):
            dfs(i+1,path+[nums[i]])

    dfs(0,[])

    return  answer

nums = [1,2,3]
print(subsets(nums))
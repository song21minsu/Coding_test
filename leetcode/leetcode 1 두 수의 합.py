def twoSum(nums,target):
    dic={}
    for i,v in enumerate(nums):
        if target-v in dic:
            return [dic[target-v],i]
        dic[v]=i
print(twoSum([1,7,11,15],9))

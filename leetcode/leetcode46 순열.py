def permute(nums):
    from itertools import permutations
    answer=list(permutations(nums))
    return answer




nums=[1,2,3]
print(permute(nums))
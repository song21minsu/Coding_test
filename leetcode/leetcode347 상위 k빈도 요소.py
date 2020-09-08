def topKFrequent(nums,k):
    from collections import Counter

    freqs=Counter(nums).most_common(k)
    return freqs

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums,k))
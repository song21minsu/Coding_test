# class Solution:
import collections
strs=["eat", "tea", "tan", "ate", "nat", "bat"]
def groupAnagrams(strs):
    anagrams=collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    # print(anagrams)
    # print(anagrams.keys())
    # print(anagrams.values())
    return anagrams.items()
print(groupAnagrams(strs))

def lengthOfLongestSubstring(s):
    arr={}
    start=0
    length=0

    for index, char in enumerate(s):
        if char in arr and start<=arr[char]:
            start=arr[char]+1
        else:
            length=max(length,index-start+1)

        arr[char]=index
        print(arr,start)

    return  length

s = "abcabcbb"
print(lengthOfLongestSubstring(s))
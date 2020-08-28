paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

import re,collections
def solution(paragraph,bannded):
    words=[word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]
    counts=collections.Counter(words)

    return counts.most_common(1)[0][0]

print(solution(paragraph,banned))

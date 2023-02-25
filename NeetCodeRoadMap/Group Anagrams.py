
# 0(m*n) Time Solution
from collections import defaultdict


def groupanagrams(strs):
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c)-ord("a")] +=1
        
        print(tuple(count))
        res[tuple(count)].append(s)

    return res.values()


        
print(groupanagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
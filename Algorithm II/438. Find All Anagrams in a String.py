def findAnagrams( s, p):
    if len(p) > len(s): return []
    dic1,dic2 = {},{}

    for i in range(len(p)):
        dic1[s[i]] = dic1.get(s[i],0)+1
        dic2[p[i]] = dic2.get(p[i],0)+1
    
    res = [0] if dic1 == dic2 else []

    l=0

    for i in range(len(p),len(s)):
        dic1[s[i]] = dic1.get(s[i],0)+1
        dic1[s[l]] -= 1

        if dic1[s[l]] == 0:
            dic1.pop(s[l])
        l+=1
        if dic1 == dic2:
            res.append(l)

    return res


s = "cbaebabacd"
p = "abc"
print(findAnagrams(s,p))
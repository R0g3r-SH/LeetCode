def subString(s):
    charSet = set()
    l = 0
    res = 0
    subs = ""

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
            subs = s[r:l]

        subs = s[r:l]
        charSet.add(s[r])
        res = max(res, r-l+1)

    print(s[r:l])
    return res


s = "pwwkew"
print(subString(s))

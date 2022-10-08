def lengthOfLongestSubstring(s) -> int:
        
    find = set()
    tlong = 1
    fprt = 1
    founded = False
    if s == "":
        return 0
    if s == " ":
        return 1

    for i in range(len(s)): 
        fprt = i
        while fprt < len(s):
            val = s[fprt]
            if val in find:
                
                founded = True
                break
            else:
                find.add(val)
            fprt+=1

        tlong = max(len(find),tlong)
        find.clear()
                
    if not founded:
        return len(s)

    return tlong
                

s= "aab"
print(lengthOfLongestSubstring(s))
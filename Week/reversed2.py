def reverseWords(s):
    li = list(s.split(" "))
    for i in range(len(li)):
        temps = list(li[i])
        l=0
        r= len(temps)-1
        while (l<=r):
            temps[l],temps[r]  = temps[r] ,temps[l]
            r-=1
            l+=1
        li[i] = "".join(temps)

    out = " ".join(li)
    return out


s = "Let's take LeetCode contest"
print(reverseWords(s))    
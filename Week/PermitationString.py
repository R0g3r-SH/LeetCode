



def checkInclusion(s1: str, s2: str) -> bool:
    dic = {}
    dic2 = set()
    counter = 0;
    maxl = 0

    for i in s1:
        dic[i]=0

    if len(s1) == len(s2):
        for i in s2:
            if i not in dic2 and i in dic:
                dic2.add(i)
            else:
                return False
        return True

    else:       
        for i in range(len(s2)-len(s1)):
            for j in range (i,i+len(s1)):
                if s2[j] in dic:
                    counter+=1
                    dic[s2[j]]+=1    
            maxl = max(maxl,counter)
            counter=0
        res = len(list(set(list(dic.values())))) == 1
        if maxl == len(dic) and res:
            return True
        else:
            return False
                

s1 ="adc"
s2 ="dcda"

print(checkInclusion(s1,s2))
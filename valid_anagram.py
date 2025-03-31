# several methods
# checking off method, sort and compare method, 
def isAnagram( s, t):
        pos = 0
        count = 0
        s1 = [0] * 26
        s2 = [0] * 26
        still_good = True

        # t_list = list(t)
        for i in s:
            pos = ord(i) - ord('a')
            s1[pos] +=1
        for i in t:
            pos = ord(i) - ord('a')
            s2[pos] +=1
        
        while still_good and count < 26:
            if s1[count] == s2[count]:
                count +=1
                continue
            else:
                still_good = False
        return still_good

print(isAnagram("boy", "yob"))
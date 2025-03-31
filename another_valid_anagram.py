def isAnagram( s: str, t: str) -> bool:
    first = [0] * 26
    second = [0] * 26
    i = 0
    while i < len(s):
        first[ord(s[i]) - ord('a')] +=1
        i+=1
    i = 0
    while i < len(t):
        second[ord(t[i]) - ord('a')] +=1
        i+=1
    for index in range(len(first)):
        if first[index] != second[index]:
            return False
    return True

print(isAnagram('racecar', 'carrace'))
print(isAnagram('xx', 'x'))
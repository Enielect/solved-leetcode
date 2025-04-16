from typing import List

def encode(strs: List[str]) -> str:
    new_str = ''
    for s in strs:
        delimiter = str(len(s)) + '#' + s
        new_str += delimiter
    return new_str

def decode(s: str) -> List[str]:
    final = []
    start = 0
    while start < len(s):
        substr = s.find('#', start)
        word_begin = start + substr - start + 1 
        word_end = int(s[start:substr]) + word_begin
        final.append(s[word_begin : word_end])
        start = word_end
    return final

print(decode('4#n2#t7###-code1##4#love3#you1##'))
print(decode('4#neet4#code4#love3#you'))
print(encode(['n2#t', '##-code', '#', 'love', 'you', '#']))
print(encode(["we","say",":","yes","!@#$%^&*()"]))
print(decode("2#we3#say1#:3#yes10#!@#$%^&*()"))

from typing import List

def encode(strs: List[str]) -> str:
        return ''.join(x+'%' for x in strs)
    
print(encode(['eni','boy']))

def decode(s:str) -> List[str]:
    final = s.split('%')
    final.pop()
    return final

print(decode(encode(['eni','boy'])))
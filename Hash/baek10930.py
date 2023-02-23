# sha-256 해시 알고리즘
import hashlib
S = input()
answer = hashlib.sha256(S.encode()).hexdigest()
print(answer)

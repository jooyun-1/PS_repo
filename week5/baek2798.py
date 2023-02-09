from itertools import combinations
N , M= input().split()
nums = input().split() #N장의 카드 입력
cards = list(combinations(nums,3)) #3장의 카드 조합
maxsum = 0
for card in cards : # 조합별 카드 합 반복하며 최대값 찾기
   if sum(map(int,card)) <= int(M) :
        maxsum = max(maxsum, sum(map(int,card)))
print(maxsum)     

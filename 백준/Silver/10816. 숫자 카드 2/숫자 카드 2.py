n = int(input())
cards = list(map(int,input().split()))
m = int(input())
nums = list(map(int,input().split()))

dic = dict()
for c in cards :
    if c in dic :
        dic[c] += 1
    else :
        dic[c] = 1

cards.sort()
start = min(cards)
end = max(cards)
answer = []

def binary(arr,target,start,end) :
    if start > end :
        return 0
    mid = (start + end) // 2
    if cards[mid] == target :
        return dic[target]
    elif cards[mid] > target :
        return binary(arr,target,start,mid-1)
    else :
        return binary(arr,target,mid+1,end)

for target in nums :
    print(binary(cards, target, 0, len(cards)-1), end=" ")


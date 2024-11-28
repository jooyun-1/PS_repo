from itertools import combinations
def solution(relation):
    col_size = len(relation[0])
    nums = range(col_size)
    candidates = []

    # 모든 후보키 조합 구하기
    for key_size in nums:
        for combination in combinations(nums, key_size+1):
            candidates.append(combination)

    # 각 조합에서 row들이 중복되는지 확인(유일성 확인)
    unique = []
    for candidate in candidates:
        lists = []
        for row in relation:
            rows = []
            for col in candidate:
                rows.append(row[col])
            lists.append(tuple(rows))
        if len(set(lists)) == len(relation):
            unique.append(candidate)

    # 유일성을 만족한 조합에서 부분집합이 있는지 확인(최소성 확인)
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if set(unique[i]).issubset(set(unique[j])):
                answer.discard(unique[j])
    return len(answer)
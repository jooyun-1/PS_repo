-- 7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛을 조회
SELECT F.FLAVOR FROM FIRST_HALF F JOIN JULY J ON F.FLAVOR = J.FLAVOR GROUP BY F.FLAVOR
ORDER BY (sum(F.TOTAL_ORDER) + sum(J.TOTAL_ORDER)) DESC LIMIT 3
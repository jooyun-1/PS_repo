SELECT A.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY, (SUM(S.SALES * B.PRICE)) AS TOTAL_SALES
FROM BOOK B JOIN AUTHOR A ON B.AUTHOR_ID = A.AUTHOR_ID
JOIN BOOK_SALES S ON B.BOOK_ID = S.BOOK_ID
WHERE S.SALES_DATE LIKE '2022-01%'
GROUP BY CATEGORY, AUTHOR_ID ORDER BY A.AUTHOR_ID, B.CATEGORY DESC
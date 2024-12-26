SELECT DATE_FORMAT(SALES_DATE,'%Y-%m-%d') as SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT FROM ONLINE_SALE
WHERE MONTH(SALES_DATE) = 3
union

SELECT DATE_FORMAT(SALES_DATE,'%Y-%m-%d'), PRODUCT_ID, NULL AS USER_ID , SALES_AMOUNT FROM OFFLINE_SALE
WHERE MONTH(SALES_DATE) = 3 ORDER BY SALES_DATE, PRODUCT_ID, USER_ID
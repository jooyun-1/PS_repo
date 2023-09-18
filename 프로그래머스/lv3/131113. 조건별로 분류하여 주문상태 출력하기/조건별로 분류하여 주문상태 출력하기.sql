-- 코드를 입력하세요
SELECT order_id, product_id, DATE_FORMAT(out_date,'%Y-%m-%d') as OUT_DATE, CASE WHEN DATEDIFF(out_date,"2022-05-01") > 0 THEN '출고대기' WHEN DATEDIFF(out_date,"2022-05-01") <= 0 THEN '출고완료' ELSE '출고미정' END as '출고여부' from FOOD_ORDER
order by order_id asc
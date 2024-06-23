-- 코드를 입력하세요
SELECT history_id, car_id, DATE_FORMAT(start_date,"%Y-%m-%d") as START_DATE, DATE_FORMAT(end_date,"%Y-%m-%d") as END_DATE, CASE WHEN DATEDIFF(END_DATE,START_DATE) >= 29 THEN '장기 대여' ELSE '단기 대여' END as RENT_TYPE from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where start_date like '2022-09-%' order by history_id desc  
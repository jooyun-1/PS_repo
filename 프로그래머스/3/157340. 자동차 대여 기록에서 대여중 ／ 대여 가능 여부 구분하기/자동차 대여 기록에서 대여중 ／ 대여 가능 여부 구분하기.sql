# SELECT CAR_ID, CASE WHEN CAR_ID IN (SELECT CAR_ID WHERE'2022-10-16' between start_date and end_date) THEN '대여중' ELSE '대여 가능' END AVAILABILITY FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# GROUP BY CAR_ID
# ORDER BY CAR_ID DESC

SELECT car_id, CASE WHEN car_id in (select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY where '2022-10-16' between start_date and end_date) THEN '대여중' ELSE '대여 가능' END availability from CAR_RENTAL_COMPANY_RENTAL_HISTORY group by car_id  order by car_id desc
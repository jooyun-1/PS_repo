-- 코드를 입력하세요
SELECT board_id, writer_id, title, price, CASE WHEN status = 'SALE' THEN '판매중' WHEN status = 'RESERVED' THEN '예약중' WHEN status = 'DONE' THEN '거래완료' END status from USED_GOODS_BOARD
where DATE_FORMAT(created_date,'%Y-%m-%d') = '2022-10-05' order by board_id desc

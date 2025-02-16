-- 코드를 입력하세요
# SELECT O.PRODUCT_ID, P.PRODUCT_NAME, SUM(P.PRICE*O.AMOUNT) AS TOTAL_SALES
# FROM (SELECT PRODUCT_ID, sum(AMOUNT) as AMOUNT, PRODUCE_DATE FROM FOOD_ORDER WHERE (PRODUCE_DATE>='2022-05-01') AND (PRODUCE_DATE<'2022-06-01') GROUP BY PRODUCT_ID) O LEFT JOIN FOOD_PRODUCT P
# ON O.PRODUCT_ID = P.PRODUCT_ID
# GROUP BY P.PRODUCT_ID
# ORDER BY TOTAL_SALES DESC

# SELECT P.PRODUCT_ID, P.PRODUCT_NAME, SUM(P.PRICE*O.AMOUNT) AS TOTAL_SALES
# FROM FOOD_PRODUCT P INNER JOIN (SELECT PRODUCT_ID, AMOUNT, PRODUCE_DATE FROM FOOD_ORDER where produce_date like '2022-05%') O
# ON P.PRODUCT_ID = O.PRODUCT_ID
select p.product_id, product_name, sum(amount*price) as total_sales
from food_product p join food_order o on p.product_id = o.product_id
where produce_date like '2022-05%'
group by p.product_id
order by total_sales desc, p.product_id



# select P.PRODUCT_ID, P.PRODUCT_NAME, SUM(P.PRICE*O.AMOUNT)
# FROM FOOD_PRODUCT P OUTER JOIN (SELECT PRODUCT_ID, sum(AMOUNT) as amount, PRODUCE_DATE FROM FOOD_ORDER WHERE (PRODUCE_DATE>='2022-05-01') AND (PRODUCE_DATE<'2022-06-01') GROUP BY PRODUCT_ID) O
# ON P.PRODUCT_ID = O.PRODUCT_ID
# (PRODUCE_DATE>='2022-05-01') AND (PRODUCE_DATE<'2022-06-01')

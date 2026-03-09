
SELECT seller_id,
        sum(price) as total_price,
        count(DISTINCT order_id) as total_orders

FROM tb_order_items

GROUP BY seller_id


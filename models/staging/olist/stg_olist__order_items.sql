with source as (
    select * from {{ source('raw', 'olist_order_items_dataset') }}
),

renamed as (
    select
        order_id,
        cast(order_item_id as integer)          as order_item_id,
        product_id,
        seller_id,
        cast(price as decimal(10, 2))           as price,
        cast(freight_value as decimal(10, 2))   as freight_value,
        cast(shipping_limit_date as timestamp)  as shipping_limit_at
    from source
)

select * from renamed
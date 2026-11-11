with source as (
    select * from {{ source('raw', 'olist_customers_dataset') }}
),

renamed as (
    select
        customer_id,
        customer_unique_id,
        cast(customer_zip_code_prefix as integer) as zip_code_prefix,
        lower(trim(customer_city))  as city,
        upper(trim(customer_state)) as state
    from source
)

select * from renamed
products (id, name, price) - продукты в магазине электроники
tags (id, name) - категории товаров к которым может относиться тот или иной продукт

```
products         | tags         
id, name, price  | id, name
                
1, milk, 31       1, tag1
2, potatos, 13    2, tag2
3, bread, 15      3, tag3
```

A product can have multiple tags.
Each tag can have multiple products.

Tables have many-to-many relationship.
Let's call it product_tags
This table should have two columns product_id and tag_id

select distinct products.name from products
left join product_tags on products.id=product_tags.product_id
left join tags on tags.id=product_tags.tag_id
where count(tags.id) > 10

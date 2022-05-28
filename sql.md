products (id, name, price) - products in electronics shop  
tags (id, name) - categories of goods to which a particular product may belong  

```
products         | tags         
id, name, price  | id, name
                
1, tv, 31000        1, tag1
2, laptop, 49000    2, tag2
3, mouse, 1500      3, tag3
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

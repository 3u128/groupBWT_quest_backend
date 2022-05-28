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

Database has many-to-many relationship.


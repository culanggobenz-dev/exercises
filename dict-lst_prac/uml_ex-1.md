::: mermaid
---
title: Shopping Puzzle
---
classDiagram
class ShoppingCart{
    + cart[]
}

class Product{
    + product~dict~
    + item ~str~ : name ~str~
    +  price ~str~ : ~int~
}

ShoppingCart <-- Product
:::
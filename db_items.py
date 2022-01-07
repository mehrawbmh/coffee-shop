table = {
    "capacity": "int",
    "number": "int",
    "is_taken": "bool"
}

category = {
    "name": "str",
    "is_sub": "bool",
    "parent_id": "int"
}

product = {
    "name": "str",
    "price": "int",
    "price_discount": "int",
    "description": "str",
    "category_id": "int",
    "image": "str"
}

basket_item = {
    "product_id": "int",
    "count": "int"
}

basket = {
    "created_at": "datetime",
    "updated_at": "datetime",
    "table_id": "int",
    "basket_items": "list"
}

order = {
    "basket_id": "int",
    "total_price": "int",
    "total_discount": "int",
    "estimated_waiting_time": "datetime",
    "is_paid": "bool",
    "is_finished": "bool"
}

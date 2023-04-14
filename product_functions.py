import db_connect as db
from flask import abort

def get_all_products():
    product_list = []
    with db.crete_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT name, supplier, color, price FROM products")
            for product in cursor.fetchall():
                product_dict = {
                    'name': product[0],
                    'supplier': product[1],
                    'color': product[2], 
                    'price': product[3],
                }
                product_list.append(product_dict)
    return product_dict

def create_new_product(product):
    existing_product = get_product_by_id(product['id'])
    if existing_product:
        return {'error': f"Product with id {product['id']} already exists"}, 409

    with db.create_connection() as connection:
        with connection.cursor() as cursor:
            query = "INSERT INTO products (name, supplier, color, price) VALUES (%s, %s, %s, %d);"
            values = (product['name'], product['supplier'], product['color'], product['price'])
            cursor.execute(query, values)
            connection.commit()
    return product, 201

def get_product_by_id(id):
    with db.crete_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name, supplier, color, price FROM products WHERE id = '" + id +"'")
            product = cursor.fetchone()
            if product is not None:
                return {
                    'id': product[0],
                    'name': product[1],
                    'supplier': product[2],
                    'color': product[3],
                    'price': product[4]
                }
            else:
                abort(
                    404, f"Product with ID {id} not found"
                )
                
def delete_product(id):
    with db.crete_connection() as connection:
        with connection.cursor() as cursor:
            delete_query = "DELETE FROM products WHERE id ='" + id + "'"
            cursor.execute(delete_query)
            connection.commit()
            return cursor.rowcount

def update_product(id, product):
    with db.crete_connection() as connection:
        with connection.cursor() as cursor:
            update_query = "UPDATE products SET supplier = %s, color = %s, price = %d WHERE id = %d"
            values = (product['supplier'], product['color'], product['price'], id)
            cursor.execute(update_query, values)
            connection.commit()
        return product
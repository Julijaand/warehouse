from mysql.connector import connect
import config
from datetime import datetime
from flask import abort
from flask import make_response


def get_products():
    with connect(**config.configValue) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name, supplier, color, price FROM products;")
            products = cursor.fetchall()

    product_list = []
    for product in products:
        product_list.append({
            'id': product[0],
            'name': product[1],
            'supplier': product[2],
            'color': product[3],
            'price': product[4],
        })

    return product_list

def get_product_by_id(id):
    with connect(**config.configValue) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name, supplier, color, price FROM products;")
            products = cursor.fetchall()
    product_list = []
    for product in products:
        product_list.append({
            'id': product[0],
            'name': product[1],
            'supplier': product[2],
            'color': product[3],
            'price': product[4],
        })
    if id in product_list:
        return product_list[id]
    else:
        abort(
            404, f"Product with ID {id} not found"
        )


def create_product(args):
    with connect(**config.configValue) as connection:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO products (name, supplier, color, price) VALUES (%s, %s);", (args['name'], args['supplier'], args['color'], args['price']))
            connection.commit()
            new_product_id = cursor.lastrowid

    return {'id': new_product_id, 'name': args['name'], 'supplier': args['supplier'], 'color': args['color'], 'price': args['price']}

import product_functions as pf
from flask import make_response


def read_all():
    return pf.get_all_products(), 200


def create_product(product):
    product, status_code = pf.create_new_product(product)
    return product, status_code


def get_product_by_id(id):
    return pf.get_product_by_id(id), 200


def delete_product(id):
    rows_affected = pf.delete_product(id)

    if rows_affected > 0:
        return make_response(f"{id} successfully deleted", 200)
    else:
        return make_response(f"Deletion of {id} failed. Product not found.", 404)


def update_product(id, product):
    return pf.update_product(id, product), 200
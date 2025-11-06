from fastapi import APIRouter
from connection import connection
from pydantic import BaseModel

restaurant_routes = APIRouter(prefix="/restaurants")

class Restaurant(BaseModel):
    name: str
    document: str
    comercial_name: str
    address: str

@restaurant_routes.get('/')
def get_restaurants():
    cursor = connection.cursor()
    sql = "SELECT * FROM restaurants"
    cursor.execute(sql)
    restaurants = cursor.fetchall()
    return restaurants

@restaurant_routes.get('/{id}')
def get_restaurants(id: int):
    cursor = connection.cursor()
    sql = "SELECT * FROM restaurants WHERE id = %s"
    cursor.execute(sql, id)
    restaurants = cursor.fetchone()
    return restaurants

@restaurant_routes.get('/{id}/itens')
def get_restaurant_itens(id: int):
    cursor = connection.cursor()
    sql = "SELECT * FROM itens WHERE restaurant=%(id)s"
    cursor.execute(sql, { "id": id })
    itens = cursor.fetchall()
    return itens

@restaurant_routes.post('/')
def post_restaurant(item: Restaurant):
    cursor = connection.cursor()
    sql = """
        INSERT INTO restaurants 
        (name, document, comercial_name, address)
        VALUES
        (%(name)s, %(document)s, %(comercial_name)s, %(address)s)
    """
    cursor.execute(sql, item.model_dump())
    connection.commit()
    return

@restaurant_routes.patch('/{id}')
def patch_restaurant(item: Restaurant, id: int):
    cursor = connection.cursor()
    sql = """
        UPDATE restaurants SET 
        name = %(name)s,
        document = %(document)s,
        comercial_name = %(comercial_name)s,
        address = %(address)s
        WHERE id = %(id)s
    """
    item = item.model_dump()
    item["id"] = id
    cursor.execute(sql, item)
    connection.commit()
    return

@restaurant_routes.delete('/{id}')
def delete_restaurant(id: int):
    cursor = connection.cursor()
    sql = """
        DELETE restaurants 
        WHERE id = %s
    """
    cursor.execute(sql, id)
    connection.commit()
    return

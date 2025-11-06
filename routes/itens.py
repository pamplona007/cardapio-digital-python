from fastapi import APIRouter
from connection import connection

itens_routes = APIRouter(prefix='/itens')

@itens_routes.get('/')
def get_itens():
    cursor = connection.cursor()
    sql = "SELECT * FROM itens"
    cursor.execute(sql)
    itens = cursor.fetchall()
    return itens

from fastapi import FastAPI
from routes.restaurants import restaurant_routes
from routes.itens import itens_routes

app = FastAPI()

app.include_router(restaurant_routes)
app.include_router(itens_routes)

@app.get("/")
def rota_inicial():
    return { 
        "message": "Olá mundo" 
    }

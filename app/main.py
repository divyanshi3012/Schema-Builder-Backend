from fastapi import FastAPI
from app.routes import product_routes, order_routes

app = FastAPI(title="HROne Ecommerce API")

app.include_router(product_routes.router)
app.include_router(order_routes.router)

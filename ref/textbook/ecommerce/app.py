from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import transaction

app = FastAPI()

class Product(BaseModel):
    id: str
    name: str
    price: float
    stock: int

# Retrieve a list of products
@app.get("/products", response_model=dict)
def get_products():
    return {k: v for k, v in root.catalog.items()}

# Retrieve a single product by ID
@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: str):
    product = root.catalog.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Add a new product
@app.post("/products", response_model=Product)
def create_product(product: Product):
    if product.id in root.catalog:
        raise HTTPException(status_code=400, detail="Product already exists")
    root.catalog[product.id] = product.dict()
    transaction.commit()
    return product

# Update a product by ID
@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: str, updated_product: Product):
    if product_id not in root.catalog:
        raise HTTPException(status_code=404, detail="Product not found")
    root.catalog[product_id] = updated_product.dict()
    transaction.commit()
    return updated_product

# Delete a product by ID
@app.delete("/products/{product_id}")
def delete_product(product_id: str):
    if product_id not in root.catalog:
        raise HTTPException(status_code=404, detail="Product not found")
    del root.catalog[product_id]
    transaction.commit()
    return {"detail": "Product deleted"}

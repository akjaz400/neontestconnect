from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import get_db, Product

app = FastAPI()

class ProductCreate(BaseModel):
    name: str
    price: int

@app.post("/products")
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(name=product.name, price=product.price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return {"status": "success", "inserted_id": new_product.id}

@app.get("/products")
def list_products(db: Session = Depends(get_db)):
    # Pulls the data in real-time from your live Neon cloud instance
    return db.query(Product).all()

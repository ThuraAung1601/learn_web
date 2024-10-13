from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import Column, Integer, Float, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Database configuration
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://thuraaung@localhost:4321/shop" 
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Pydantic model
class Product(BaseModel):
    prodId: int
    prodName: str
    price: float
    stock: int

    class Config:
        orm_mode = True

# SQLAlchemy ORM model
class ProductORM(Base):
    __tablename__ = 'products'
    prodID = Column(Integer, primary_key=True, nullable=False)
    prodName = Column(String(63), unique=True)
    price = Column(Float)
    stock = Column(Integer)

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint to add a new product
@app.post("/product/")
async def add_new_product(product: Product, db: Session = Depends(get_db)):
    product_orm = ProductORM(
        prodID=product.prodId,
        prodName=product.prodName,
        price=product.price,
        stock=product.stock
    )
    db.add(product_orm)
    db.commit()
    db.refresh(product_orm)
    return product_orm

# Endpoint to retrieve the list of products
@app.get("/products/")
async def get_all_products(db: Session = Depends(get_db)):
    products = db.query(ProductORM).all()
    return products

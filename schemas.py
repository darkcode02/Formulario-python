from pydantic import BaseModel

class ProductoBase(BaseModel):
    nombre_producto: str
    costo_producto: float

class ProductoCreate(ProductoBase):
    pass

class Producto(ProductoBase):
    id_producto: int

    class Config:
        orm_mode = True

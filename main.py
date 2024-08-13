from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import crud, models, schemas
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def read_index(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@app.get("/productos/", response_class=HTMLResponse)
def read_productos(request: Request, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    productos = crud.get_productos(db, skip=skip, limit=limit)
    return templates.TemplateResponse("lista_productos.html", {"request": request, "productos": productos})

@app.get("/productos/agregar", response_class=HTMLResponse)
def get_agregar_producto(request: Request):
    return templates.TemplateResponse("agregar_producto.html", {"request": request})

@app.post("/productos/", response_class=HTMLResponse)
def create_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    db_producto = crud.create_producto(db=db, producto=producto)
    return HTMLResponse(content=f"Producto creado: {db_producto.nombre_producto}", status_code=201)

from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")

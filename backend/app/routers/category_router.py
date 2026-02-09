from fastapi import APIRouter, HTTPException
from typing import List
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryResponse

router = APIRouter(prefix="/categorias", tags=["Categorías"])

@router.post("/", response_model=CategoryResponse)
async def create_category(category: CategoryCreate):
    existing = await Category.find_one(Category.nombre == category.nombre)
    if existing:
        raise HTTPException(status_code=400, detail="La categoría ya existe")
    
    new_cat = Category(**category.dict())
    await new_cat.insert()
    return new_cat

@router.get("/", response_model=List[CategoryResponse])
async def get_categories():
    return await Category.find_all().to_list()
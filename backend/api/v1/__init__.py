from fastapi import APIRouter
from .chat import router as chat_router
from .product import router as products_router

router = APIRouter()
router.include_router(chat_router)
router.include_router(products_router, prefix="/product")
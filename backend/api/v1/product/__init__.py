from fastapi import APIRouter
from ...core.mongo import db

router = APIRouter()


@router.get("/{uuid}")
def get_product(uuid: str): ...
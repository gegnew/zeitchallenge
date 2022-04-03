from fastapi import APIRouter

from app.schemas import StringCounts
from app.schemas.schemas import InputText
from .util import count_letters

router = APIRouter()


@router.post("/count", response_model=StringCounts)
async def count_string(text: InputText):
    return dict(count_letters(text.dict()["text"]))

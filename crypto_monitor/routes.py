from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
from backend.blocks.models import Block, Currency, Provider
from django.db.models import Q
from django.utils.timezone import now

router = APIRouter()

class BlockOut(BaseModel):
    id: int
    currency: str
    block_number: int
    created_at: Optional[str]
    stored_at: str

    class Config:
        orm_mode = True

@router.get("/blocks", response_model=List[BlockOut])
async def get_blocks(currency: Optional[str] = None, skip: int = 0, limit: int = 10):
    query = Block.objects.all()
    if currency:
        query = query.filter(currency__name__iexact=currency)
    blocks = query.order_by("-stored_at")[skip:skip+limit]
    return blocks

@router.get("/blocks/{block_id}", response_model=BlockOut)
async def get_block(block_id: int):
    try:
        block = Block.objects.get(id=block_id)
        return block
    except Block.DoesNotExist:
        raise HTTPException(status_code=404, detail="Block not found")

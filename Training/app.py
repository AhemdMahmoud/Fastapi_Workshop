from typing import Union
#import query
import time

from fastapi import FastAPI, Query
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items")
def read_item(item_id: int = Query (..., gt= 12 ,lt=48,description= "this is actual i want "), q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items")
def update_item(item_id: int, item: Item, q: Union[str, None] = None):
    updated_price = (item.price) + 3
    return {"price":updated_price+3, "is_offer":item.is_offer, "item_id": item_id, "q": q}

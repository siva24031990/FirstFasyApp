# -*- coding: utf-8 -*-
from fastapi import FastAPI
myapp=FastAPI()

@myapp.get("/")
async def simply():
    return{"message","Success"}

from fastapi import FastAPI
from cardata import CarData

car = CarData()
app = FastAPI(
title="FoodAPI",
    description="ApiRestFul para la gestión de coches",
    version="0.0.1",
    contact={
        "name":"Adrian Tomas",
        "url":"http://www.mastermind.ac"
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },

)

#Definicion de los endpoints

#Devolución de todos los coches, con tres query parameters,total,skip,all.
@app.get("/coches")
async def get_coches(total:int=10, skip:int=0, all:bool=False):
    if all:
        return await car.get_allICoches()
    return await car.get_coches(skip, total)

#Devolución de un solo coche, con un path parameter obligatorio con el id del coche.
@app.get("/coches/coche/{id}")
async def get_coche(id:int):
    return await car.get_coche(id)

#Devolución de los coches de una marca, con el query parameter marca de tipo String obligatorio.
@app.get("/coches/marca")
async def get_coche(marca: str):
    return await car.get_cochesMarca(marca)

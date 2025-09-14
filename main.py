from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel

from datos.database import get_db
from logica.servicios import ServicioEstudiante, ServicioSondeo
from fastapi.middleware.cors import CORSMiddleware

class PreguntaSchema(BaseModel):
    id: int
    texto_pregunta: str
    tipo_respuesta: str
    class Config:
        orm_mode = True

class PlantillaPreguntaSchema(BaseModel):
    peso: float
    pregunta: PreguntaSchema
    class Config:
        orm_mode = True

class EstudianteSchema(BaseModel):
    id: int
    nombre: str
    apellido: str
    salon: str
    genero: str
    class Config:
        orm_mode = True

app = FastAPI(title="API de EMA", version="0.1.0")
origins = [
    "http://localhost",
    "http://localhost:8080", 
    "*" 
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

servicio_estudiante = ServicioEstudiante()
servicio_sondeo = ServicioSondeo()

@app.get("/api/estudiantes", response_model=List[EstudianteSchema], tags=["Estudiantes"])
def obtener_estudiantes(db: Session = Depends(get_db)):
    estudiantes = servicio_estudiante.obtener_todos_los_estudiantes(db)
    return estudiantes

@app.get("/api/plantilla-sondeo", response_model=List[PlantillaPreguntaSchema], tags=["Sondeos"])
def obtener_plantilla_por_edad(edad: int, db: Session = Depends(get_db)):
    plantilla = servicio_sondeo.obtener_plantilla_para_edad(db, edad)
    return plantilla
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Estudiante(Base):
    __tablename__ = "estudiantes"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    apellido = Column(String)
    salon = Column(String)
    genero = Column(String)

class RangoEdad(Base):
    __tablename__ = "rangos_edad"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    edad_minima = Column(Integer)
    edad_maxima = Column(Integer)

class Pregunta(Base):
    __tablename__ = "preguntas"
    id = Column(Integer, primary_key=True, index=True)
    texto_pregunta = Column(String)
    tipo_respuesta = Column(String)

class PlantillaPorEdad(Base):
    __tablename__ = "plantillas_por_edad"
    id = Column(Integer, primary_key=True, index=True)
    rango_edad_id = Column(Integer, ForeignKey("rangos_edad.id"))
    pregunta_id = Column(Integer, ForeignKey("preguntas.id"))
    peso = Column(Float)
    pregunta = relationship("Pregunta")

class ResultadoSondeo(Base):
    __tablename__ = "resultados_sondeo"
    id = Column(Integer, primary_key=True, index=True)

class Respuesta(Base):
    __tablename__ = "respuestas"
    id = Column(Integer, primary_key=True, index=True)

from sqlalchemy.orm import Session
from . import modelos

class RepositorioEstudiante:
    def obtener_todos(self, db: Session):
        return db.query(modelos.Estudiante).all()

class RepositorioPlantilla:
    def obtener_por_edad(self, db: Session, edad: int):
        rango = db.query(modelos.RangoEdad).filter(
            modelos.RangoEdad.edad_minima <= edad, 
            modelos.RangoEdad.edad_maxima >= edad
        ).first()
        
        if not rango:
            return []
        
        plantillas = db.query(modelos.PlantillaPorEdad).filter(
            modelos.PlantillaPorEdad.rango_edad_id == rango.id
        ).all()
        
        return plantillas
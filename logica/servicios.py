from sqlalchemy.orm import Session
from datos.repositorios import RepositorioEstudiante, RepositorioPlantilla

class ServicioEstudiante:
    def __init__(self):
        self.repo = RepositorioEstudiante()
    
    def obtener_todos_los_estudiantes(self, db: Session):
        return self.repo.obtener_todos(db)

class ServicioSondeo:
    def __init__(self):
        self.repo = RepositorioPlantilla()
    
    def obtener_plantilla_para_edad(self, db: Session, edad: int):
        return self.repo.obtener_por_edad(db, edad)
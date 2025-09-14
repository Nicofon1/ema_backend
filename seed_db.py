from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datos.modelos import Base, Estudiante, RangoEdad, Pregunta, PlantillaPorEdad

DATABASE_URL = "sqlite:///./ema_app.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

RANGOS_EDAD_DATA = [
    {"id": 1, "nombre": "0-6 años (Preescolar)", "edad_minima": 0, "edad_maxima": 6},
    {"id": 2, "nombre": "6-9 años (Infancia)", "edad_minima": 6, "edad_maxima": 9},
    {"id": 3, "nombre": "9-12 años (Pre-adolescencia)", "edad_minima": 9, "edad_maxima": 12},
    {"id": 4, "nombre": "12-15 años (Adolescencia Media)", "edad_minima": 12, "edad_maxima": 15},
    {"id": 5, "nombre": "15-18 años (Adolescencia Tardía)", "edad_minima": 15, "edad_maxima": 18},
]
PREGUNTAS_DATA = [
    {"id": 1, "texto_pregunta": "¿El/la niño/a muestra cambios de humor drásticos e inexplicables?", "tipo_respuesta": "Si/No/No sé"},
    {"id": 2, "texto_pregunta": "¿El/la niño/a evita el contacto físico que antes disfrutaba o busca afecto indiscriminado?", "tipo_respuesta": "Si/No/No sé"},
    {"id": 3, "texto_pregunta": "¿Has observado señales físicas inexplicables como moretones o higiene descuidada?", "tipo_respuesta": "Si/No/No sé"},
    {"id": 4, "texto_pregunta": "¿El/la niño/a utiliza lenguaje o gestos de naturaleza sexual inapropiados para su edad?", "tipo_respuesta": "Nunca/A veces/Siempre"},
    {"id": 5, "texto_pregunta": "¿Hay un adulto no familiar con una influencia o control inusual sobre el/la niño/a?", "tipo_respuesta": "Si/No/No sé"},
    {"id": 6, "texto_pregunta": "En una escala de 1 a 10, ¿qué tan preocupado/a estás por el bienestar del niño/a?", "tipo_respuesta": "Escala"},
    {"id": 7, "texto_pregunta": "¿El estudiante ha mostrado cambios notables en su actitud (más reservado/a, agresivo/a)?", "tipo_respuesta": "Si/No/No sé"},
    {"id": 8, "texto_pregunta": "En una escala del 1 al 10, ¿en qué nivel ubicarías su tendencia a aislarse?", "tipo_respuesta": "Escala"},
    {"id": 9, "texto_pregunta": "¿El estudiante ha llegado con nuevas posesiones sin explicación clara?", "tipo_respuesta": "Nunca/A veces/Siempre"},
    {"id": 10, "texto_pregunta": "¿Has notado que el estudiante está frecuentemente con adultos que parecen controlar sus decisiones?", "tipo_respuesta": "Si/No/No sé"},
    {"id": 11, "texto_pregunta": "¿El estudiante ha manifestado comentarios o conductas sexualizadas no acordes a su edad?", "tipo_respuesta": "Nunca/A veces/Siempre"},
    {"id": 12, "texto_pregunta": "¿Has notado que el estudiante adopta formas de vestir que podrían considerarse sexualizadas?", "tipo_respuesta": "Si/No/No sé"},
    {"id": 13, "texto_pregunta": "En una escala del 1 al 10, ¿en qué nivel ubicarías tu percepción de riesgo?", "tipo_respuesta": "Escala"},
    {"id": 14, "texto_pregunta": "¿El estudiante se ha aislado de su grupo de amigos habitual?", "tipo_respuesta": "Si/No/No sé"},
    {"id": 15, "texto_pregunta": "¿El estudiante tiene posesiones caras (celulares, ropa) sin explicación?", "tipo_respuesta": "Nunca/A veces/Siempre"},
    {"id": 16, "texto_pregunta": "¿Está frecuentemente con adultos o adolescentes mucho mayores que lo controlan?", "tipo_respuesta": "Si/No/No sé"},
    {"id": 17, "texto_pregunta": "¿El estudiante ha manifestado comentarios, bromas o conductas sexualizadas?", "tipo_respuesta": "Nunca/A veces/Siempre"},
    {"id": 18, "texto_pregunta": "¿Pasa mucho tiempo en línea y muestra nerviosismo con sus dispositivos?", "tipo_respuesta": "Si/No/No sé"},
    {"id": 19, "texto_pregunta": "¿Se ha ausentado repetidamente o ha mencionado viajes injustificados?", "tipo_respuesta": "Si/No/No sé"},
    {"id": 20, "texto_pregunta": "En una escala del 1 al 10, ¿en qué nivel ubicarías tu percepción de riesgo?", "tipo_respuesta": "Escala"},
    {"id": 21, "texto_pregunta": "¿Ha habido una caída drástica e inexplicable en su rendimiento académico?", "tipo_respuesta": "Si/No/No sé"},
    {"id": 22, "texto_pregunta": "¿Tiene dinero o dispositivos caros que no corresponden a su situación familiar?", "tipo_respuesta": "Nunca/A veces/Siempre"},
    {"id": 23, "texto_pregunta": "¿Tiene una relación (amistosa/romántica) con una persona significativamente mayor y controladora?", "tipo_respuesta": "Si/No/No sé"},
    {"id": 24, "texto_pregunta": "¿Utiliza un lenguaje o habla de experiencias demasiado maduras para su edad?", "tipo_respuesta": "Nunca/A veces/Siempre"},
    {"id": 25, "texto_pregunta": "¿Es extremadamente secreto con su vida digital o tiene múltiples perfiles?", "tipo_respuesta": "Si/No/No sé"},
    {"id": 26, "texto_pregunta": "¿Falta a la escuela de manera recurrente sin justificación válida?", "tipo_respuesta": "Nunca/A veces/Siempre"},
    {"id": 27, "texto_pregunta": "En una escala del 1 al 10, ¿en qué nivel ubicarías tu percepción de riesgo?", "tipo_respuesta": "Escala"},
    {"id": 28, "texto_pregunta": "¿Ha abandonado su círculo de amigos de mucho tiempo o se ha aislado?", "tipo_respuesta": "Si/No/No sé"},
    {"id": 29, "texto_pregunta": "¿Justifica posesiones caras con 'regalos' o 'trabajos online' vagos?", "tipo_respuesta": "Nunca/A veces/Siempre"},
    {"id": 30, "texto_pregunta": "¿Depende emocional o financieramente de un adulto fuera de su núcleo familiar?", "tipo_respuesta": "Si/No/No sé"},
    {"id": 31, "texto_pregunta": "¿Normaliza o glorifica comportamientos de riesgo (sustancias, fiestas con adultos)?", "tipo_respuesta": "Nunca/A veces/Siempre"},
    {"id": 32, "texto_pregunta": "¿Hay evidencia de que participa en actividades en línea riesgosas?", "tipo_respuesta": "Si/No/No sé"},
    {"id": 33, "texto_pregunta": "¿Falta a clases para realizar 'viajes' o 'compromisos' con explicaciones vagas?", "tipo_respuesta": "Nunca/A veces/Siempre"},
    {"id": 34, "texto_pregunta": "En una escala del 1 al 10, ¿qué tan convencido/a estás de que está en un entorno seguro? (invertida)", "tipo_respuesta": "Escala"},
]
PLANTILLAS_DATA = [
    {"rango_edad_id": 1, "pregunta_id": 1, "peso": 1.0}, {"rango_edad_id": 1, "pregunta_id": 2, "peso": 1.3}, {"rango_edad_id": 1, "pregunta_id": 3, "peso": 1.5},
    {"rango_edad_id": 1, "pregunta_id": 4, "peso": 1.5}, {"rango_edad_id": 1, "pregunta_id": 5, "peso": 1.5}, {"rango_edad_id": 1, "pregunta_id": 6, "peso": 1.2},
    {"rango_edad_id": 2, "pregunta_id": 7, "peso": 1.0}, {"rango_edad_id": 2, "pregunta_id": 8, "peso": 1.1}, {"rango_edad_id": 2, "pregunta_id": 9, "peso": 1.2},
    {"rango_edad_id": 2, "pregunta_id": 10, "peso": 1.5}, {"rango_edad_id": 2, "pregunta_id": 11, "peso": 1.5}, {"rango_edad_id": 2, "pregunta_id": 12, "peso": 1.3},
    {"rango_edad_id": 2, "pregunta_id": 13, "peso": 1.5},
    {"rango_edad_id": 3, "pregunta_id": 14, "peso": 1.1}, {"rango_edad_id": 3, "pregunta_id": 15, "peso": 1.3}, {"rango_edad_id": 3, "pregunta_id": 16, "peso": 1.5},
    {"rango_edad_id": 3, "pregunta_id": 17, "peso": 1.5}, {"rango_edad_id": 3, "pregunta_id": 18, "peso": 1.4}, {"rango_edad_id": 3, "pregunta_id": 19, "peso": 1.3},
    {"rango_edad_id": 3, "pregunta_id": 20, "peso": 1.5},
    {"rango_edad_id": 4, "pregunta_id": 21, "peso": 1.2}, {"rango_edad_id": 4, "pregunta_id": 22, "peso": 1.4}, {"rango_edad_id": 4, "pregunta_id": 23, "peso": 1.5},
    {"rango_edad_id": 4, "pregunta_id": 24, "peso": 1.3}, {"rango_edad_id": 4, "pregunta_id": 25, "peso": 1.5}, {"rango_edad_id": 4, "pregunta_id": 26, "peso": 1.3},
    {"rango_edad_id": 4, "pregunta_id": 27, "peso": 1.5},
    {"rango_edad_id": 5, "pregunta_id": 28, "peso": 1.1}, {"rango_edad_id": 5, "pregunta_id": 29, "peso": 1.4}, {"rango_edad_id": 5, "pregunta_id": 30, "peso": 1.5},
    {"rango_edad_id": 5, "pregunta_id": 31, "peso": 1.3}, {"rango_edad_id": 5, "pregunta_id": 32, "peso": 1.5}, {"rango_edad_id": 5, "pregunta_id": 33, "peso": 1.5},
    {"rango_edad_id": 5, "pregunta_id": 34, "peso": 1.4},
]
ESTUDIANTES_DATA = [
    {"nombre": "Ana", "apellido": "García", "salon": "3A", "genero": "Femenino"},
    {"nombre": "Luis", "apellido": "Martinez", "salon": "5B", "genero": "Masculino"},
]

def sembrar_base_de_datos():
    print("Iniciando la siembra de la base de datos...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        for data in RANGOS_EDAD_DATA: db.add(RangoEdad(**data))
        db.commit()
        for data in PREGUNTAS_DATA: db.add(Pregunta(**data))
        db.commit()
        for data in PLANTILLAS_DATA: db.add(PlantillaPorEdad(**data))
        db.commit()
        for data in ESTUDIANTES_DATA: db.add(Estudiante(**data))
        db.commit()
        print("\n¡Siembra completada exitosamente!")
    except Exception as e:
        print(f"Error durante la siembra: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    sembrar_base_de_datos()
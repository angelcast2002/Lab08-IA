from itertools import combinations
import random

# Definimos los dias disponibles para los examenes
dias = ['lunes', 'martes', 'miercoles']

# Definimos los exámenes y los estudiantes que toman cada examen
examenes = ['IA', 'ADA', 'COMPIS', 'CALCULO', 'FISICA', 'QUIMICA', 'BIOLOGIA']
estudiantes_por_examen = {
    'IA': ['Angel', 'Alejandro'],
    'ADA': ['Diego'],
    'COMPIS': ['Alejandro', 'Mark'],
    'CALCULO': ['Angel', 'Mark'],
    'FISICA': ['Mark', 'Diego'],
    'QUIMICA': ['Diego', 'Angel'],
    'BIOLOGIA': ['Alejandro'],
}

# Definimos las variables que representan los exámenes y sus posibles días
variables = {examen: dias for examen in examenes}


# Definimos la función para verificar si una asignación es válida
def esValida(asignacion):
    # Verificar que los estudiantes que toman el mismo curso no tengan examen el mismo día
    for examen1, examen2 in combinations(variables, 2):
        if asignacion[examen1] == asignacion[examen2]:
            estudiantes_examen1 = set(estudiantes_por_examen[examen1])
            estudiantes_examen2 = set(estudiantes_por_examen[examen2])
            if len(estudiantes_examen1.intersection(estudiantes_examen2)) > 0:
                return False

    # Verificar que ningún estudiante tenga más de un examen por día
    for dia in dias:
        examenesPorDia = [examen for examen, diaAsignado in asignacion.items() if diaAsignado == dia]
        estudiantesPorDia = set()
        for examen in examenesPorDia:
            estudiantesPorDia.update(estudiantes_por_examen[examen])
        if len(estudiantesPorDia) < len(examenesPorDia):
            return False

    return True

class LocalSearch:
    def __init__(self, variables, dias, estudiantes_por_examen, esValida):
        self.variables = variables
        self.dias = dias
        self.estudiantes_por_examen = estudiantes_por_examen
        self.esValida = esValida
        self.asignacion = self.generar_asignacion_inicial()

    def generar_asignacion_inicial(self):
        # Generar una asignación inicial aleatoria
        asignacion = {}
        for examen in self.variables:
            asignacion[examen] = random.choice(self.dias)
        return asignacion

    def generar_vecinos(self):
        # Generar todas las soluciones vecinas cambiando un examen de día
        vecinos = []
        for examen in self.variables:
            for dia in self.dias:
                if self.asignacion[examen] != dia:
                    vecino = self.asignacion.copy()
                    vecino[examen] = dia
                    vecinos.append(vecino)
        return vecinos

    def local_search(self):
        while True:
            vecinos = self.generar_vecinos()
            # Ordenar los vecinos por su valor de evaluación
            vecinos.sort(key=self.esValida, reverse=True)
            # Si el mejor vecino es peor que la solución actual, devolver la solución actual
            if not self.esValida(vecinos[0]):
                return self.asignacion
            # Si no, actualizar la solución actual al mejor vecino
            self.asignacion = vecinos[0]


scheduler = LocalSearch(variables, dias, estudiantes_por_examen, esValida)
result = scheduler.local_search()
print(result)
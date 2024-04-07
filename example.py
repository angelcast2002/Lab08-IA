from itertools import combinations

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

class backTraking:
  def __init__(self, variables, dias, estudiantes_por_examen, esValida):
        self.variables = variables
        self.dias = dias
        self.estudiantes_por_examen = estudiantes_por_examen
        self.esValida = esValida
        self.asignacion = {}

  def backtracking_search(self):
    # Si la asignación es completa y válida, devolverla
    if set(self.asignacion.keys()) == set(self.variables) and self.esValida(self.asignacion):
        return self.asignacion

    # Seleccionar un examen sin asignar
    for examen in self.variables:
        if examen not in self.asignacion:
            # Para cada día, asignar ese día al examen y hacer una llamada recursiva
            for dia in self.dias:
                self.asignacion[examen] = dia
                result = self.backtracking_search()

                # Si la llamada recursiva devuelve una asignación válida, devolver esa asignación
                if result is not None:
                    return result

                # Si no, deshacer la asignación del día al examen
                del self.asignacion[examen]

    # Si ninguno de los días resulta en una asignación válida, devolver None
    return None

scheduler = backTraking(variables, dias, estudiantes_por_examen, esValida)
result = scheduler.backtracking_search()
print(result)
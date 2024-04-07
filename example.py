from itertools import combinations

# Definimos los dias disponibles para los examenes
dias = ['lunes', 'martes', 'miercoles']

# Definimos los exámenes y los estudiantes que toman cada examen
examenes = ['IA', 'ADA', 'COMPIS', 'SO', 'BD2', 'MD']
estudiantes_por_examen = {
    'IA': ['Angel', 'Alejandro'],
    'ADA': ['Angel', 'Diego'],
    'COMPIS': ['Alejandro', 'Mark'],
    'SO': ['Angel', 'Mark'],
    'BD2': ['Alejandro', 'Diego'],
    'MD': ['Diego', 'Mark'],
}

# Definimos las variables que representan los exámenes y sus posibles días
variables = {examen: dias for examen in examenes}


# Definimos la función para verificar si una asignación es válida
def esValida(asignacion):
    # Verificar que no haya dos exámenes en el mismo día
    for dia in dias:
        examenesPorDia = [examen for examen, diaAsignado in asignacion.items() if diaAsignado == dia]
        if len(examenesPorDia) > 1:
            return False
    
    # Verificar que los estudiantes que toman el mismo curso no tengan examen el mismo día
    for examen1, examen2 in combinations(examenes, 2):
        if asignacion[examen1] == asignacion[examen2]:
            estudiantes_examen1 = set(estudiantes_por_examen[examen1])
            estudiantes_examen2 = set(estudiantes_por_examen[examen2])
            if len(estudiantes_examen1.intersection(estudiantes_examen2)) > 0:
                return False
    
    return True

# Asignación válida
asignacion_valida = {'IA': 'lunes', 'ADA': 'martes', 'COMPIS': 'miercoles', 'SO': 'jueves', 'BD2': 'viernes', 'MD': 'sabado'}
print("¿La asignación es válida?", esValida(asignacion_valida))

# Asignación no válida
asignacion_no_valida = {'IA': 'lunes', 'ADA': 'martes', 'COMPIS': 'martes', 'SO': 'miercoles', 'BD2': 'lunes', 'MD': 'miercoles'}
print("¿La asignación es válida?", esValida(asignacion_no_valida))


class BackTrackingSearch:
  def __init__(self, variables, dominio, restricciones):
    self.variables = variables
    self.dominio = dominio
    self.restricciones = restricciones
    self.asignacion = {}
  
  def backTrackingSearch(self):
    if len(self.asignacion) == len(self.variables):
      return self.asignacion
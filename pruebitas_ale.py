from itertools import permutations

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

# Función para verificar si un estado es válido
def es_valido(estado):
    for dia in dias:
        examenes_dia = [e for e, d in estado.items() if d == dia]
        estudiantes_por_dia = {}
        for examen in examenes_dia:
            estudiantes = estudiantes_por_examen[examen]
            for estudiante in estudiantes:
                if estudiante in estudiantes_por_dia:
                    return False  # Mismo estudiante con más de un examen en un día
                estudiantes_por_dia[estudiante] = True
    return True

# Función para evaluar un estado utilizando una heurística (en este caso, cantidad de restricciones incumplidas)
def evaluar_estado(estado):
    restricciones_incumplidas = 0
    estudiantes_por_dia_por_examen = {examen: {dia: [] for dia in dias} for examen in examenes}
    for examen, dia in estado.items():
        estudiantes = estudiantes_por_examen[examen]
        for estudiante in estudiantes:
            if estudiante in estudiantes_por_dia_por_examen[examen][dia]:
                restricciones_incumplidas += 1  # Mismo estudiante con más de un examen en un día
            estudiantes_por_dia_por_examen[examen][dia].append(estudiante)
    return -restricciones_incumplidas  # Queremos minimizar las restricciones incumplidas

# Algoritmo de beam search
def beam_search(beam_width):
    mejor_estado = None
    mejor_puntaje = float('-inf')
    for permutacion in permutations(examenes):
        estado = {examen: None for examen in examenes}
        for i, examen in enumerate(permutacion):
            estado[examen] = dias[i % len(dias)]
        if es_valido(estado):
            puntaje_actual = evaluar_estado(estado)
            if puntaje_actual > mejor_puntaje:
                mejor_estado = estado
                mejor_puntaje = puntaje_actual
    return mejor_estado

# Ejecutar beam search
solucion = beam_search(5)
print("Solución encontrada:")
print(solucion)

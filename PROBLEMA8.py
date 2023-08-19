estudiantes = []

for i in range(3):
    print(f"Ingresando datos del estudiante {i + 1}:")
    carnet = input("Carnet: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    nota4 = float(input("Nota 4: "))
    
    promedio = (nota1 + nota2 + nota3 + nota4) / 4
    
    estudiante = {
        "Carnet": carnet,
        "Nombre": nombre,
        "Apellido": apellido,
        "Promedio": promedio
    }
    
    estudiantes.append(estudiante)

print("\nInformación de los estudiantes:")
for estudiante in estudiantes:
    print(f"Carné: {estudiante['Carnet']}, Nombre: {estudiante['Nombre']} {estudiante['Apellido']}, Promedio: {estudiante['Promedio']}")

promedio_general = sum(estudiante['Promedio'] for estudiante in estudiantes) / len(estudiantes)
print(f"\nPromedio general de todas las notas: {promedio_general}")
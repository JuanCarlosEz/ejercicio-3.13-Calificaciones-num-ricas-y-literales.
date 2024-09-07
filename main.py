class Calificacion:
    def __init__(self, nota):

        self.nota = nota

    def asignar_calificacion(self):

        if 9.1 <= self.nota <= 10:
            return "A Excelente"
        elif 8.1 <= self.nota <= 9.0:
            return "B Muy bien"
        elif 7.5 <= self.nota <= 8.0:
            return "C Bien"
        elif self.nota < 7.5:
            return "R Reprobado"
        else:
            return " incorrecta ingrese nota de 0 a 10"

try:
    nota = float(input("Ingrese la calificación numérica del estudiante: "))

    # Crear una instancia de la clase Calificacion
    calificacion = Calificacion(nota)

    # Asignar la calificación literal
    resultado = calificacion.asignar_calificacion()

    print(f"La calificación correspondiente es: {resultado}")

except ValueError:
    print("Por favor, ingrese un valor numérico válido.")

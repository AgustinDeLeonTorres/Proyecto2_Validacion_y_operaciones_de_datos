📋 Descripción del Proyecto
Este proyecto contiene dos programas en Python que demuestran el uso de estructuras de control y validación de datos, consolidando los conocimientos adquiridos en el módulo 2 del bootcamp.

🚀 Programas Implementados
1. Longitud de una Frase
Objetivo: Verificar si una palabra tiene entre 4 y 8 caracteres.

Lógica del programa:

Solicita al usuario una palabra

Calcula la longitud de la palabra con len()

Utiliza condicionales if-elif-else para verificar:

Si tiene entre 4-8 caracteres → "Correcta"

Si tiene menos de 4 → "Faltan letras"

Si tiene más de 8 → "Sobran letras"

Implementación:

# Solicitar palabra y calcular longitud
palabra = input("Ingresa una palabra: ")
longitud = len(palabra)

# Verificar rango de longitud
if 4 <= longitud <= 8:
    print("La palabra es correcta")
elif longitud < 4:
    print(f"Hacen falta letras. Solo tiene {longitud} letras")
else:
    print(f"Sobran letras. Tiene {longitud} letras")

2. Encuentra el Cuadrante
Objetivo: Determinar en qué cuadrante se encuentra un punto basado en sus coordenadas (X, Y).

Lógica del programa:

Solicita las coordenadas X e Y

Primero verifica casos especiales:

Si ambas son 0 → "Origen"

Si X es 0 → "Eje Y"

Si Y es 0 → "Eje X"

Luego verifica los cuadrantes:

Cuadrante I: X negativa, Y positiva

Cuadrante II: X positiva, Y positiva

Cuadrante III: X negativa, Y negativa

Cuadrante IV: X positiva, Y negativa

Implementación:

def encontrar_cuadrante():
    try:
        x = float(input("Ingrese la coordenada X: "))
        y = float(input("Ingrese la coordenada Y: "))
        
        # Casos especiales primero
        if x == 0 and y == 0:
            print("El punto se encuentra en el origen")
        elif x == 0:
            print("El punto se encuentra sobre el eje Y")
        elif y == 0:
            print("El punto se encuentra sobre el eje X")
        # Luego verificar cuadrantes
        elif x < 0 and y > 0:
            print("El punto se encuentra en el cuadrante I")
        elif x > 0 and y > 0:
            print("El punto se encuentra en el cuadrante II")
        elif x < 0 and y < 0:
            print("El punto se encuentra en el cuadrante III")
        else:
            print("El punto se encuentra en el cuadrante IV")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos")

💡 Reflexiones del Bootcamp
Hasta ahora en el bootcamp he aprendido:

📚 Conceptos Técnicos:
Variables y tipos de datos en Python

Estructuras de control (if, elif, else) para tomar decisiones

Funciones para organizar y reutilizar código

Manejo de errores con try-except para programas más robustos

Operadores de comparación y lógicos

🧠 Desarrollo de Lógica:
Aprendí a descomponer problemas en pasos más pequeños

Mejoré en pensar secuencialmente cómo resolver problemas

Entendí la importancia de validar datos de entrada

Aprendí que el orden de las condiciones es crucial en programación

🎯 Desafíos Superados:
El mayor desafío fue entender el sistema de cuadrantes cartesianos, especialmente:

Que el Cuadrante I tiene X negativa y Y positiva

La importancia de verificar primero los casos especiales (ejes y origen)

Cómo usar condicionales anidados de forma efectiva

🔄 Cambio de Mentalidad:
Ahora entiendo que programar no es solo escribir código, sino:

Pensar lógicamente antes de codificar

Probar con diferentes casos para asegurar que funcione correctamente

Leer errores para entender qué salió mal

Investigar cuando no entiendo algo

Este bootcamp me está enseñando no solo Python, sino una nueva forma de resolver problemas paso a paso.

📂 Estructura del Repositorio
text
/
├── AGUSTIN_DELEON_proyectoM2.py  # Código completo con ambos programas
├── README.md                     # Este archivo
└── demo/                         # Carpeta con ejemplos adicionales

🛠️ Cómo Ejecutar
Clona el repositorio

Ejecuta el archivo principal:
bash
python AGUSTIN_DELEON_proyectoM2.py

👨‍💻 Autor
Agustín De León - Estudiante de Python en el Bootcamp C35
# Solicitar al usuario que ingrese una palabra
palabra = input("Ingresa una palabra: ")

# Calcular la longitud de la palabra
longitud = len(palabra)

# Verificar en qué rango se encuentra la longitud
if 4 <= longitud <= 8:
    # Si está entre 4 y 8 caracteres, es correcta
    print("La palabra es correcta")
elif longitud < 4:
    # Si tiene menos de 4 caracteres, faltan letras
    print(f"Hacen falta letras. Solo tiene {longitud} letras")
else:
    # Si tiene más de 8 caracteres, sobran letras
    print(f"Sobran letras. Tiene {longitud} letras")


print("*******************************")

def encontrar_cuadrante():
    #Programa que determina el cuadrante de un punto en el plano cartesiano
    print("\n=== DETERMINACIÓN DE CUADRANTE ===")
    
    try:
        # Solicitar las coordenadas al usuario
        x = float(input("Ingrese la coordenada X: "))
        y = float(input("Ingrese la coordenada Y: "))
        
        # Verificar casos especiales primero (ESENCIAL)
        if x == 0 and y == 0:
            print("El punto se encuentra en el origen")
        elif x == 0:
            print("El punto se encuentra sobre el eje Y")
        elif y == 0:
            print("El punto se encuentra sobre el eje X")
        # Ahora sí verificar los cuadrantes (CORREGIDOS)
        elif x > 0 and y > 0:    # Cuadrante I: X positiva, Y positiva
            print("El punto se encuentra en el cuadrante I")
        elif x < 0 and y > 0:    # Cuadrante II: X negativa, Y positiva
            print("El punto se encuentra en el cuadrante II")
        elif x < 0 and y < 0:    # Cuadrante III: X negativa, Y negativa
            print("El punto se encuentra en el cuadrante III")
        else:  # x > 0 and y < 0 - Cuadrante IV: X positiva, Y negativa
            print("El punto se encuentra en el cuadrante IV")
            
    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos")

encontrar_cuadrante()
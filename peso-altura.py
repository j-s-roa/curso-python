# Solicitar el peso y la estatura al usuario
peso = float(input("Ingresa tu peso en kg: "))
estatura = float(input("Ingresa tu estatura en metros: "))

# Calcular el índice de masa corporal (IMC)
imc = peso / (estatura ** 2)

# Redondear el resultado a dos decimales
imc = round(imc, 2)

# Mostrar el resultado en la consola
print("Tu índice de masa corporal es:", imc)

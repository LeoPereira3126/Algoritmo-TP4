def orden_oracion(oracion):
    palabras = oracion.split()
    longitud = [(palabra, sum(1 for caracter in palabra if caracter.isalpha())) for palabra in palabras]    
    palabras_ordenadas = sorted(longitud, key=lambda x: x[1], reverse=True)
    orden_final = [palabra[0] for palabra in palabras_ordenadas]
    nueva_cadena = " ".join(orden_final)
    return nueva_cadena


cadena = input("Por favor ingrese una oración para su proximo ordenamiento: ")
cadena_ordenada = orden_oracion(cadena)
print("-" *148 )
print("Frase original: ")
print(cadena)
print()
print("Frase ordenada: ")
print(cadena_ordenada)
print("-" * 148)

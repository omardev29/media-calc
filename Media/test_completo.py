from media import media, mediana, moda, varianza, desviacion_estandar

# Test data
numeros = [2, 4, 4, 4, 5, 5, 7, 9]
print(f"\nDatos de prueba: {numeros}")
print(f"Media: {media(numeros):.2f}")
print(f"Mediana: {mediana(numeros):.2f}")
print(f"Moda: {moda(numeros)}")
print(f"Varianza: {varianza(numeros):.2f}")
print(f"Desviación Estándar: {desviacion_estandar(numeros):.2f}")

# Test with different data types
decimales = [1.5, 2.5, 2.5, 3.5, 4.5]
print(f"\nDatos decimales: {decimales}")
print(f"Media: {media(decimales):.2f}")
print(f"Mediana: {mediana(decimales):.2f}")
print(f"Moda: {moda(decimales)}")

# Test with empty list
vacios = []
print(f"\nLista vacía: {vacios}")
print(f"Media: {media(vacios)}")
print(f"Mediana: {mediana(vacios)}")
print(f"Moda: {moda(vacios)}")
print(f"Varianza: {varianza(vacios)}")
print(f"Desviación Estándar: {desviacion_estandar(vacios)}")

# Print version
import media
print(f"\nVersión de la librería: {media.__version__}")

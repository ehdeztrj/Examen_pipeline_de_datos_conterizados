import csv
import time
from collections import defaultdict

print("Iniciando procesamiento secuencial...")
start_time = time.time()

resultados = defaultdict(float)
archivo = 'ventas_125054088.csv'

try:
    with open(archivo, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader) # Saltar el encabezado
        for campos in reader:
            if len(campos) != 8: 
                continue
            try:
                fecha_hora = campos[1]
                categoria = campos[3]
                cantidad = float(campos[5])
                precio = float(campos[6])
                
                # Extraer hora
                hora = fecha_hora.split(" ")[1].split(":")[0]
                ingreso = cantidad * precio
                
                clave = f"{hora}_{categoria}"
                resultados[clave] += ingreso
            except Exception:
                continue

    # Guardar resultados en un txt para comparar después
    with open('scripts/resultado_secuencial.txt', 'w') as out:
        for k in sorted(resultados.keys()):
            linea = f"{k}\t{round(resultados[k], 2)}\n"
            out.write(linea)
            
    end_time = time.time()
    print(f"¡Terminado!")
    print(f"--- Tiempo de ejecución secuencial: {round(end_time - start_time, 2)} segundos ---")
    print("Los resultados se guardaron en scripts/resultado_secuencial.txt")

except FileNotFoundError:
    print(f"Error: No se encontró el archivo {archivo} en el directorio actual.")
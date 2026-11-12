#!/usr/bin/env python3
import sys

# Formato del CSV:
# id,fecha_hora,tienda,categoria,producto,cantidad,precio_unitario,metodo_pago
# 0 ,1         ,2     ,3        ,4       ,5       ,6              ,7

for linea in sys.stdin:
    linea = linea.strip()
    
    # Ignoro encabezados y lineas vacias
    if not linea or linea.startswith("id,"):
        continue
        
    campos = linea.split(",")
    
    # Se hace la validacion
    if len(campos) != 8:
        continue
        
    try:
        fecha_hora = campos[1]
        categoria = campos[3]
        cantidad = float(campos[5])
        precio = float(campos[6])
        
        # Se extrae la hora: de "2025-01-01 14:30:00" saca "14"
        hora = fecha_hora.split(" ")[1].split(":")[0]
        
        ingreso = cantidad * precio
        
        # Se emite la clave y el valor separados por tabulador
        # Clave: Hora_Categoria (ej. 14_Electronica), Valor: ingreso
        print(f"{hora}_{categoria}\t{ingreso}")
        
    except Exception:
        # Se ignoran las lineas mal hechas para que no truene el job
        continue
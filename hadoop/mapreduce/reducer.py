#!/usr/bin/env python3
import sys

current_key = None
current_ingreso_total = 0.0

for linea in sys.stdin:
    linea = linea.strip()
    if not linea:
        continue
        
    try:
        key, ingreso_str = linea.split('\t', 1)
        ingreso = float(ingreso_str)
    except ValueError:
        continue
        
    if current_key == key:
        current_ingreso_total += ingreso
    else:
        if current_key is not None:
            # Se imprime el resultado del grupo anterior redondeado a 2 decimales
            print(f"{current_key}\t{round(current_ingreso_total, 2)}")
        current_key = key
        current_ingreso_total = ingreso

# Y ya se imprime el ultimo grupo si existe
if current_key == key:
    print(f"{current_key}\t{round(current_ingreso_total, 2)}")
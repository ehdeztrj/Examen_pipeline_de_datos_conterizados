import sys, random, csv
from datetime import datetime, timedelta

if len(sys.argv) == 2:
    matricula = sys.argv[1].strip()
else:
    matricula = input("Ingresa tu matricula (9 digitos): ").strip()

while not (matricula.isdigit() and len(matricula) == 9):
    matricula = input("Matricula invalida. Debe tener exactamente 9 digitos: ").strip()

random.seed(matricula)
print(f"Generando dataset para {matricula}... (tarda unos minutos)")

N = 5_000_000
tiendas = [f"Tienda_{str(i).zfill(2)}" for i in range(1, random.randint(15, 40))]
categorias = [
    "Electronica", "Abarrotes", "Ropa", "Hogar", "Juguetes",
    "Farmacia", "Deportes", "Papeleria", "Mascotas", "Bebidas"
]
productos = {c: [f"{c[:3].upper()}-{i:04d}" for i in range(1, random.randint(30, 80))] for c in categorias}
pagos = ["Efectivo", "Tarjeta", "Transferencia", "Vales"]
inicio = datetime(2025, 1, 1)

filename = f"ventas_{matricula}.csv"

with open(filename, "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["id", "fecha_hora", "tienda", "categoria", "producto", "cantidad", "precio_unitario", "metodo_pago"])
    
    for i in range(1, N + 1):
        cat = random.choice(categorias)
        fecha = inicio + timedelta(seconds=random.randint(0, 365*24*3600))
        w.writerow([
            i,
            fecha.strftime("%Y-%m-%d %H:%M:%S"),
            random.choice(tiendas),
            cat,
            random.choice(productos[cat]),
            random.randint(1, 20),
            round(random.uniform(5.0, 2500.0), 2),
            random.choice(pagos)
        ])

print(f"Listo. Archivo {filename} generado exitosamente.")
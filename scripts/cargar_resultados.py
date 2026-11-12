import psycopg2

# ¡Nota que el host ahora es "db", el nombre del contenedor en docker-compose!
DB_HOST = "db" 
DB_PORT = "5432"
DB_NAME = "datamart_db"
DB_USER = "admin"
DB_PASS = "admin123"

try:
    print("Conectando a PostgreSQL interno...")
    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASS)
    cur = conn.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS ingresos_hora_categoria (
            id SERIAL PRIMARY KEY,
            hora VARCHAR(2),
            categoria VARCHAR(50),
            ingreso_total NUMERIC(15, 2)
        )
    """)
    cur.execute("TRUNCATE TABLE ingresos_hora_categoria")

    print("Insertando registros...")
    with open("part-00000", "r") as f:
        for linea in f:
            if not linea.strip(): continue
            clave, ingreso = linea.strip().split('\t')
            hora, categoria = clave.split('_')
            cur.execute(
                "INSERT INTO ingresos_hora_categoria (hora, categoria, ingreso_total) VALUES (%s, %s, %s)",
                (hora, categoria, float(ingreso))
            )
            
    conn.commit()
    cur.close()
    conn.close()
    print("¡Carga exitosa! 240 registros insertados en la base de datos.")

except Exception as e:
    print(f"Error: {e}")
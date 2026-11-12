from fastapi import FastAPI, HTTPException
import psycopg2
from psycopg2.extras import RealDictCursor
import os

app = FastAPI(title="DataMart API - Examen 2do Parcial")

# Conectarse a la BD interna usando el nombre del contenedor "db"
DB_HOST = "db"
DB_PORT = "5432"
DB_NAME = os.getenv("POSTGRES_DB", "datamart_db")
DB_USER = os.getenv("POSTGRES_USER", "admin")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "admin123")

def get_db_connection():
    return psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASS)

# 1. GET /resultados -> todos los registros
@app.get("/resultados")
def obtener_todos():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM ingresos_hora_categoria")
    resultados = cur.fetchall()
    cur.close()
    conn.close()
    return resultados

# 2. GET /resultados/<clave> -> filtro por clave (categoria)
@app.get("/resultados/{categoria}")
def obtener_por_categoria(categoria: str):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM ingresos_hora_categoria WHERE categoria = %s", (categoria,))
    resultados = cur.fetchall()
    cur.close()
    conn.close()
    if not resultados:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return resultados

# 3. Metodo de escritura (DELETE) funcionando sobre la nueva tabla
@app.delete("/resultados/borrar/{id}")
def borrar_registro(id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM ingresos_hora_categoria WHERE id = %s RETURNING id", (id,))
    eliminado = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    
    if eliminado:
        return {"mensaje": f"Registro con ID {id} eliminado correctamente"}
    raise HTTPException(status_code=404, detail="ID no encontrado")
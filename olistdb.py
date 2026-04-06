import pandas as pd
from sqlalchemy import create_engine
import os

# 1. Configuración de la conexión
# Reemplaza 'tu_password' por la contraseña que pusiste en PostgreSQL
DB_USER = 'postgres'
DB_PASS = 'admin123'  # <--- CAMBIA ESTO
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'olist_db'

# Crear el motor de conexión
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# 2. Ruta de tus archivos CSV (Usa r'' para evitar problemas con las barras \)
path = r"C:\Users\barvi\Documents\Proyectos\Proyecto_2-Olist\Data" # <--- CAMBIA ESTO

# 3. Proceso ETL Automatizado
print("Iniciando carga de datos...")

for file in os.listdir(path):
    if file.endswith('.csv'):
        # Nombre de la tabla basado en el archivo (ej: olist_orders_dataset -> orders)
        table_name = file.replace('olist_', '').replace('_dataset', '').replace('.csv', '')
        
        print(f"Procesando: {file} -> Tabla: {table_name}")
        
        # Leer el archivo
        df = pd.read_csv(os.path.join(path, file))
        
        # --- TRANSFORMACIÓN BÁSICA (Paso profesional de limpieza) ---
        # Convertir nombres de columnas a minúsculas y quitar espacios/puntos
        df.columns = [c.lower().strip().replace(' ', '_').replace('.', '_') for c in df.columns]
        
        # --- CARGA (LOAD) ---
        # Subir a SQL (Si la tabla ya existe, la reemplaza)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        
print("\n¡Éxito! Todos los datos están en PostgreSQL.")

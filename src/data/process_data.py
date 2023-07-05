import os
import sys
import pandas as pd

# from ..helpers.DataLoader import DataLoader as DTL

sys.path.insert(0, os.path.join(os.path.dirname(sys.path[0]), "helpers"))
from DataLoader import DataLoader as DTL

# Ruta del archivo de datos en bruto
# input_filepath = "./data/raw/RH_bruto.csv"
# Reemplaza por DataLoader
reader = DTL("./data/raw/RH_bruto.csv")

# Ruta donde se guardará el archivo de datos procesados
output_filepath = "./data/processed/RH_procesado.csv"

# Leer los datos brutos
df = reader.load_data()

# Rellenar los valores faltantes
# Para 'Años_En_Empresa', 'Ingreso_Mensual', 'Evaluacion_Desempeño', y 'Nivel_Satisfaccion'
# vamos a usar la media de cada columna
for column in [
    "Años_En_Empresa",
    "Ingreso_Mensual",
    "Evaluacion_Desempeño",
    "Nivel_Satisfaccion",
]:
    df[column] = df[column].fillna(df[column].mean())

# Para 'Nombre', 'Apellido', 'Rol_Trabajo', 'Genero', y 'Desercion'
# vamos a rellenar los valores faltantes con un valor predeterminado
for column in ["Nombre", "Apellido", "Rol_Trabajo", "Genero", "Desercion"]:
    df[column] = df[column].fillna("Desconocido")

# Para 'ID_Empleado' vamos a eliminar las filas que tienen un valor faltante, ya que es un identificador único
df = df.dropna(subset=["ID_Empleado"])

# Guardar los datos procesados
df.to_csv(output_filepath, index=False)

print("Los datos se han procesado y guardado correctamente.")

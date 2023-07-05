# src/generate_figures.py
import pandas as pd
import matplotlib.pyplot as plt
from helpers.DataLoader import DataLoader as DTL


def plot_histogram(df, column, output_path):
    plt.figure(figsize=(10, 6))
    plt.hist(df[column])
    plt.title(f"Distribución de {column}")
    plt.xlabel(column)
    plt.ylabel("Frecuencia")

    plt.savefig(output_path)
    plt.close()


def main():
    reader = DTL("./data/processed/RH_procesado.csv")
    df = reader.load_data()

    # Asegúrate de que los datos estén correctamente procesados antes de intentar trazarlos
    plot_histogram(df, "Desercion", "./reports/figures/histograma_desercion.png")


if __name__ == "__main__":
    main()

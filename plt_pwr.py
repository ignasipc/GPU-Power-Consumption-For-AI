import matplotlib.pyplot as plt
import pandas as pd

def main():
    # Cargar el archivo
    df = pd.read_csv(
        "test1_ignasi.txt",  # Cambia por el nombre de tu archivo
        sep="\t",  # Separación por tabulación
        decimal=",",  # Convierte comas a decimales reales
        engine="python"  # Permite separadores irregulares
    )

    # Convertir W a número y quitar signo negativo
    df["W"] = df["W"].astype(float).abs()

    # Crear eje de tiempo en segundos: 1, 2, 3...
    df["t_seconds"] = range(1, len(df) + 1)

    print(f"\nDuración total de la prueba: {len(df)}s")
    print(f"Duración total formateada (HH:MM:SS): {len(df)// 3600:02d}:{(len(df) % 3600) // 60:02d}:{len(df)% 60:02d}")

    # Graficamos los resultados
    plt.figure(figsize=(10, 5))
    plt.plot(df["t_seconds"], df["W"], linewidth=1.5)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Watios (W)")
    plt.title("Consumo de Watios a lo largo del tiempo")
    plt.grid(True)
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    main()
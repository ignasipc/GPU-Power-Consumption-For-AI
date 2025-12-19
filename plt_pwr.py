import matplotlib.pyplot as plt
import pandas as pd

def main():
    name_hw = 'test1_ignasi'   # Nombre del archivo del monitor Hardware
    name_sw = 'gpu_log'          # Nombne del archivo del monitor Software

    # Cargar el archivo
    df_hw = pd.read_csv(
        "%s.txt" % name_hw,
        sep="\t",  # Separación por tabulación
        decimal=",",  # Convierte comas a decimales reales
        engine="python"  # Permite separadores irregulares
    )

    df_sw = pd.read_csv("%s.csv" % name_sw)

    # Convertir W a número y quitar signo negativo
    df_hw["W"] = df_hw["W"].astype(float).abs()

    # Crear eje de tiempo en segundos: 1, 2, 3...
    df_hw["t_seconds"] = range(1, len(df_hw) + 1)
    df_sw["t_seconds"] = range(1, len(df_sw) + 1)

    print(f"\nDuración total de la prueba Hardware: {len(df_hw)}s")
    print(f"Duración total de la prueba Software: {len(df_sw)}s")
    print(f"\nDuración total formateada Hardware (HH:MM:SS): {len(df_hw)// 3600:02d}:{(len(df_hw) % 3600) // 60:02d}:{len(df_hw)% 60:02d}")
    print(f"Duración total formateada Hardware (HH:MM:SS): {len(df_sw)// 3600:02d}:{(len(df_sw) % 3600) // 60:02d}:{len(df_sw)% 60:02d}")

    # Graficamos los resultados del monitor SW
    plt.figure(figsize=(10, 5))
    plt.plot(df_hw["t_seconds"], df_hw["W"], linewidth=1.5)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Watios (W)")
    plt.title("Consumo de Watios a lo largo del tiempo (Monitor SW)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('Plots/Plot_%s.png' % name_hw)
    plt.show()

    # Graficamos los resultados del monitor HW
    plt.figure(figsize=(10, 5))
    plt.plot(df_sw["t_seconds"], df_sw[" utilization.gpu [%]"], linewidth=1.5)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Uso de GPU (%)")
    plt.title("Porcentaje de uso de la GPU")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('Plots/Plot_%s.png' % name_sw)
    plt.show()



if __name__ == "__main__":
    main()
import matplotlib.pyplot as plt
import pandas as pd

def main():
    name_hw = 'test1_ignasi'   # Nombre del archivo del monitor Hardware
    name_sw = 'gpu_log'          # Nombne del archivo del monitor Software

    # Cargar el archivo
    df_hw = pd.read_csv(
        "Monitoring_logs/%s.txt" % name_hw,
        sep="\t",  # Separación por tabulación
        decimal=",",  # Convierte comas a decimales reales
        engine="python"  # Permite separadores irregulares
    )

    df_sw = pd.read_csv("Monitoring_logs/%s.csv" % name_sw)

    # Convertir W a número y quitar signo negativo
    df_hw["W"] = df_hw["W"].astype(float).abs()
    df_sw["W"] = df_sw[" power.draw [W]"].str.replace("W", "").astype(float)

    # Crear eje de tiempo en segundos: 1, 2, 3...
    df_hw["t_seconds"] = range(1, len(df_hw) + 1)
    df_sw["t_seconds"] = range(1, len(df_sw) + 1)

    print(f"\nDuración total de la prueba Hardware: {len(df_hw)}s")
    print(f"Duración total de la prueba Software: {len(df_sw)}s")
    print(f"\nDuración total formateada Hardware (HH:MM:SS): {len(df_hw)// 3600:02d}:{(len(df_hw) % 3600) // 60:02d}:{len(df_hw)% 60:02d}")
    print(f"Duración total formateada Hardware (HH:MM:SS): {len(df_sw)// 3600:02d}:{(len(df_sw) % 3600) // 60:02d}:{len(df_sw)% 60:02d}")

    # Graficamos los resultados del monitor HW y SW (W)
    plt.figure(figsize=(10, 5))
    plt.plot(df_hw["t_seconds"], df_hw["W"], linewidth=1.5, color="red", label="Consumo total (Monitor HW)")
    plt.plot(df_sw["t_seconds"], df_sw["W"], linewidth=1.5, color="green", label="Consumo de la GPU (Monitor SW)")
    plt.legend()
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Watios (W)")
    plt.title("Consumo de Watios a lo largo del tiempo (Monitor SW)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('Plots/Plot_power_consumption.png')
    plt.show()

    # Graficamos los resultados del monitor SW (% de uso)
    plt.figure(figsize=(10, 5))
    plt.plot(df_sw["t_seconds"], df_sw[" utilization.gpu [%]"], linewidth=1.5, color="")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Uso de GPU (%)")
    plt.title("Porcentaje de uso de la GPU")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('Plots/Plot_GPU_usage.png')
    plt.show()



if __name__ == "__main__":
    main()
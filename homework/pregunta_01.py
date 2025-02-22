"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import matplotlib.pyplot as plt
import pandas as pd
import os

def pregunta_01():
    colores_dict = {
        'Television': 'dimgray',
        'Newspaper': 'grey',
        'Internet': 'tab:blue',
        'Radio': 'lightgrey',
    }
    
    orden_dict = {
        'Television': 1,
        'Newspaper': 1,
        'Internet': 2,
        'Radio': 1,
    }
    
    peso_lineas = {
        'Television': 2,
        'Newspaper': 2,
        'Internet': 3,
        'Radio': 2,
    }
    
    archivo_csv = "files/input/news.csv"
    df = pd.read_csv(archivo_csv, index_col=0)

    plt.figure()
    
    for medio in df.columns:
        plt.plot(
            df[medio],
            color=colores_dict[medio],
            label=medio,
            zorder=orden_dict[medio],
            linewidth=peso_lineas[medio],
        )

    plt.title("How people get their news", fontsize=16)
    
    # Ocultar bordes y ejes no deseados
    ejes = plt.gca()
    ejes.spines['top'].set_visible(False)
    ejes.spines['left'].set_visible(False)
    ejes.spines['right'].set_visible(False)
    ejes.axes.get_yaxis().set_visible(False)

    for medio in df.columns:
        inicio = df.index[0]
        fin = df.index[-1]
        
        plt.scatter(x=inicio, y=df.at[inicio, medio], color=colores_dict[medio], zorder=orden_dict[medio])
        plt.text(
            inicio - 0.2,
            df.at[inicio, medio],
            f"{medio} {df.at[inicio, medio]}%",
            ha='right',
            va='center',
            color=colores_dict[medio],
        )

        plt.scatter(x=fin, y=df.at[fin, medio], color=colores_dict[medio])
        plt.text(
            fin + 0.2,
            df.at[fin, medio],
            f"{medio} {df.at[fin, medio]}%",
            ha='left',
            va='center',
            color=colores_dict[medio],
        )

    ruta_guardado = os.path.join("files", "plots")
    if not os.path.exists(ruta_guardado):
        os.makedirs(ruta_guardado)

    plt.tight_layout()
    plt.savefig(os.path.join(ruta_guardado, "news.png"))
    plt.show()
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

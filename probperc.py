import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

sns.set()
sns.set_context("paper")
sns.set_palette("colorblind")

# Funcion para obtener promedio y desviacion estandar
def prom_desv(datos):
    try:
        return np.mean(datos), np.std(datos)
    except:
        return np.nan, np.nan
        
def main():
    # Entrada de argumentos por consola (cadenas a listas)
    L_entrada = sys.argv[1].split()
    p_entrada = sys.argv[2].split()
    OPT = sys.argv[3].split()

    # Pasar a arreglos de Numpy de numeros enteros o flotantes
    L = np.array([int(i) for i in L_entrada])
    P = np.array([float(i) for i in p_entrada])

    # Lista de colores para las figuras 1 y 2
    colors = sns.color_palette("colorblind", n_colors=len(L))

    # Crear los objetos de figuras
    fig1, ax1 = plt.subplots(figsize=(8,6))    # Figura para la probabilidad de cluster percolante
    fig2, ax2 = plt.subplots(figsize=(8,6))    # Figura para Tamaño maximo promedio
    fig3, ax3 = plt.subplots(figsize=(8,6))    # Figura para tiempos computacionales

    # Iterar sobre los tamaños de matriz y las probabilidades de ocupacion para optmizer O3 (Figuras 1 y 2)
    for j, l in enumerate(L):
        prob = np.zeros(len(P))
        tam = np.zeros(len(P))
        desvtam = np.zeros(len(P))
        for i, p in enumerate(P):
            datos = np.loadtxt(f"./resultados/datos_{l}_{p}_O3.txt")
            prob[i], _ = prom_desv(datos[:,0])
            tam[i], desvtam[i] = prom_desv(datos[datos[:, 1] > 0, 1])
        ax1.plot(P, prob, label=f"L = {l}", marker='o', ms=6, color=colors[j], mec='black')
        ax2.errorbar(P, tam / (l * l), yerr=desvtam / (l * l), label=f"L = {l}", capsize = 3, fmt = '--o', ms=6, color=colors[j], mec='black')

    # Lista de colores para la figura 3
    colors = sns.color_palette("colorblind", n_colors=len(OPT))

    # Iterar sobre los optimizadores, los tamanos de matriz y probabilidades de ocupacion (Figura 3)
    # Los tiempos computacionales son para todas las probabilidades y semillas para un valor de tamaño de matriz
    for i, o in enumerate(OPT):
        WT = np.zeros(len(L))
        CT = np.zeros(len(L))
        for j, l in enumerate(L):
            wt = 0
            ct = 0
            for p in P:
                datos = np.loadtxt(f"./resultados/datos_{l}_{p}_{o}.txt")
                wt += np.sum(datos[:, 2])
                ct += np.sum(datos[:, 3])
            WT[j] = wt
            CT[j] = ct
        ax3.plot(L, WT, label=f"Wall time - {o}", color=colors[i], marker='o', ls='--', mec='black', ms=6)
        ax3.plot(L, CT, label=f"CPU time - {o}", color=colors[i], marker='o', mec='black', ms=6)

    # Configuracion de las graficas
    n = 15 # fontsize labels de los ejes
    m = 12 # fontsize del legend
    ax1.set_xlabel(r"Probabilidad de ocupacion $p$", fontsize=n)
    ax1.set_ylabel(r"Probabilidad de cluster percolante", fontsize=n)
    ax1.legend(fontsize=m)
    ax1.grid(True)
    fig1.tight_layout()
    fig1.savefig("Probabilidadcluster.pdf")

    ax2.set_xlabel(r"Probabilidad de ocupacion $p$", fontsize=n)
    ax2.set_ylabel(r"Tamaño promedio cluster percolante más grande", fontsize=n)
    ax2.legend(fontsize=m)
    ax2.grid(True)
    fig2.tight_layout()
    fig2.savefig("Tamanocluster.pdf")

    ax3.set_xlabel(r"Tamaño del lado de la malla", fontsize=n)
    ax3.set_ylabel(r"Tiempo comutacional [s]", fontsize=n)
    ax3.set_xscale("log")
    ax3.set_yscale("log")
    ax3.legend(loc='center', bbox_to_anchor=(0.85, 0.58), fontsize=m)
    ax3.grid(True)
    fig3.tight_layout()
    fig3.savefig("Tiempos.pdf")

    plt.close("all")
    
main()

        


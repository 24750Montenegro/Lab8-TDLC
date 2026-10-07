import os
import sys
import time
import multiprocessing as mp
import plotly.graph_objects as go

Iterations = [ 1, 10, 100, 1000, 10000, 100000, 1000000]
TIMEOUT = 800


def ejercicio_1 (n):
    counter = 0
    for i in range(n // 2, n + 1):
        for j in range(1, n - n // 2 + 1):
            k = 1
            while k <= n: # al no poder usar for con aumento k = k*2, se usa while
                counter += 1
                k *= 2       #k = k*2
    return counter


def ejercicio_2 (n):
    if (n <= 1):
        return
    for i in range (1, n + 1):
        for j in range (1, n+1):
            print("sequence")
            break


def ejercicio_3 (n):
    for i in range (1, (n // 3) + 1):
        for j in range (1, n + 1, 4):
                print("sequence")


def medir(funcion, n, conexion):
    sys.stdout = open(os.devnull, "w")
    inicio = time.perf_counter()
    funcion(n)
    conexion.send(time.perf_counter() - inicio)


def ejecutar(funcion, n):
    receptor, emisor = mp.Pipe(duplex=False)
    proceso = mp.Process(target=medir, args=(funcion, n, emisor))
    proceso.start()
    tiempo = receptor.recv() if receptor.poll(TIMEOUT) else None
    proceso.terminate()
    proceso.join()
    return tiempo


def graficar(nombre, iteraciones, tiempos):
    fig = go.Figure(go.Scatter(
        x=iteraciones,
        y=tiempos,
        mode="lines+markers",
        line=dict(color="#2a78d6", width=2),
        marker=dict(size=8),
        hovertemplate="n = %{x}<br>tiempo = %{y:.6f} s<extra></extra>",
    ))
    fig.update_layout(
        title=nombre,
        xaxis_title="Iteraciones (n)",
        yaxis_title="Tiempo (s)",
        template="plotly_white",
    )
    fig.update_xaxes(type="log")
    fig.update_yaxes(type="log")
    fig.show()


def main():
    ejercicios = {
        "Ejercicio 1": ejercicio_1,
        "Ejercicio 2": ejercicio_2,
        "Ejercicio 3": ejercicio_3,
    }
    resultados = {}

    for nombre, funcion in ejercicios.items():
        iteraciones, tiempos = [], []
        for n in Iterations:
            tiempo = ejecutar(funcion, n)
            if tiempo is None:
                print(f"{nombre} | n = {n}: supera {TIMEOUT} s, se omiten valores mayores")
                break
            print(f"{nombre} | n = {n}: {tiempo:.6f} s")
            iteraciones.append(n)
            tiempos.append(tiempo)
        resultados[nombre] = (iteraciones, tiempos)

    for nombre, (iteraciones, tiempos) in resultados.items():
        graficar(nombre, iteraciones, tiempos)


if __name__ == "__main__":
    main()

# Laboratorio No. 8
## Video

[Ver video de ejecución](https://youtu.be/vI4_LjDPJyc)

## Contenido

| Archivo / carpeta | Descripción |
|---|---|
| `Lab8.py` | Implementación y profiling de los ejercicios 1, 2 y 3 (inciso b) |
| `docs/` | documentos con los incisos teóricos (ejercicios 1a, 2a, 3a, 4 y 5) |

## Requisitos

- Python 3.10 o superior
- [Plotly](https://plotly.com/python/)

```bash
pip install plotly
```

## Ejecución

```bash
python Lab8.py
```

El programa ejecuta cada ejercicio con los tamaños de input
`n = 1, 10, 100, 1000, 10000, 100000, 1000000`, muestra en consola el tiempo de
cada ejecución y al terminar abre en el navegador una gráfica interactiva
(tamaño de input vs. tiempo) por ejercicio.

## Funcionamiento

- **Medición de tiempo:** se usa `time.perf_counter()` alrededor de cada llamada.
- **Límite de tiempo:** cada ejecución corre en un proceso separado con un límite
  definido por la constante `TIMEOUT` (en segundos). Si un valor de `n` lo supera,
  el proceso se detiene y se omiten los valores mayores de ese ejercicio, ya que
  también lo superarían. Para intentar valores más grandes basta con aumentar
  `TIMEOUT`.
- **Salida de `print`:** durante la medición la salida estándar se redirige a
  `os.devnull`, de modo que el costo del `print` se incluye en el tiempo pero no
  se imprimen millones de líneas en la consola.
- **Gráficas:** ambos ejes usan escala logarítmica, porque los tiempos van desde
  microsegundos hasta minutos.

## Resultados

Tiempos en segundos con `TIMEOUT = 800`. "—" indica que la ejecución superó el
`TIMEOUT`.

| n | Ejercicio 1 | Ejercicio 2 | Ejercicio 3 |
|---:|---:|---:|---:|
| 1 | 0.000003 | 0.000001 | 0.000001 |
| 10 | 0.000006 | 0.000026 | 0.000021 |
| 100 | 0.000391 | 0.000100 | 0.000617 |
| 1000 | 0.054203 | 0.000822 | 0.064736 |
| 10000 | 7.808349 | 0.014898 | 6.366590 |
| 100000 | — | 0.081230 | 645.507237 |
| 1000000 | — | 0.829642 | — |

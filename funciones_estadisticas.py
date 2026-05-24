# -*- coding: utf-8 -*-
"""
funciones_estadisticas.py
Funciones estadísticas reutilizables para el proyecto AquaLimpia S.A.
Utiliza NumPy, SciPy y Joblib.
"""

import numpy as np
from scipy import stats
from joblib import dump


def calcular_indicadores(columna, nombre_archivo="indicadores_aqualimpia.joblib"):
    """
    Calcula media, desviación estándar e intervalo de confianza al 95%.
    Guarda los resultados en un archivo Joblib para reutilización.

    Parámetros:
        columna: Serie de pandas con los valores numéricos a analizar.
        nombre_archivo: Nombre del archivo .joblib donde se guardan los resultados.

    Retorna:
        Diccionario con media, desviación estándar e IC 95%.
    """

    media = np.mean(columna)

    desviacion = np.std(columna, ddof=1)

    intervalo = stats.t.interval(
        confidence=0.95,
        df=len(columna) - 1,
        loc=media,
        scale=stats.sem(columna)
    )

    resultados = {
        "media": float(media),
        "desviacion_estandar": float(desviacion),
        "ic95": (
            float(intervalo[0]),
            float(intervalo[1])
        )
    }

    dump(resultados, nombre_archivo)

    return resultados


def evaluar_calidad_datos(df):
    """
    Evalúa la calidad del dataset revisando valores nulos,
    duplicados y tipos de datos.

    Parámetros:
        df: DataFrame de pandas con los datos del proyecto.

    Retorna:
        Diccionario con el reporte de calidad.
    """

    reporte = {
        "valores_nulos": df.isnull().sum(),
        "duplicados": df.duplicated().sum(),
        "tipos_datos": df.dtypes
    }

    return reporte

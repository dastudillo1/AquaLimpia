# -*- coding: utf-8 -*-
"""
funciones_reportes.py
Funciones para generar reportes Excel diferenciados por área
para el proyecto AquaLimpia S.A.
"""

import pandas as pd


def crear_reporte_operaciones(df, nombre_archivo="reporte_operaciones_aqualimpia.xlsx"):
    """
    Genera reporte Excel para el área de Operaciones.
    Incluye variables operativas clave para evaluar eficiencia
    y detectar alertas en el proceso de tratamiento.

    Parámetros:
        df: DataFrame con los datos procesados del proyecto.
        nombre_archivo: Nombre del archivo Excel de salida.

    Retorna:
        DataFrame con las columnas del reporte de operaciones.
    """

    reporte = df[
        [
            "fecha_registro",
            "planta",
            "caudal_entrada_m3_d",
            "DBO_entrada_mg_L",
            "DBO_salida_mg_L",
            "energia_aeracion_kWh",
            "lodos_generados_kg_d",
            "eficiencia_tratamiento",
            "alerta_operativa"
        ]
    ].copy()

    reporte.to_excel(nombre_archivo, index=False)

    return reporte


def crear_reporte_gestion_ambiental(df, nombre_archivo="reporte_gestion_ambiental_aqualimpia.xlsx"):
    """
    Genera reporte Excel para el área de Gestión Ambiental.
    Incluye variables de calidad del efluente y cumplimiento normativo
    para respaldar reportes ante organismos fiscalizadores.

    Parámetros:
        df: DataFrame con los datos procesados del proyecto.
        nombre_archivo: Nombre del archivo Excel de salida.

    Retorna:
        DataFrame con las columnas del reporte de gestión ambiental.
    """

    reporte = df[
        [
            "fecha_registro",
            "planta",
            "DBO_salida_mg_L",
            "cumplimiento_norma",
            "eficiencia_tratamiento",
            "alerta_operativa"
        ]
    ].copy()

    reporte.to_excel(nombre_archivo, index=False)

    return reporte

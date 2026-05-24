# Proyecto AquaLimpia S.A.

Ciencia de Datos  
Semana 8  

## Objetivo
Analizar el comportamiento de las plantas de tratamiento de aguas residuales para identificar patrones de incumplimiento normativo, evaluar la eficiencia del proceso y generar información útil para distintas áreas de la empresa.

## Preguntas de investigación
1. ¿Qué planta presenta mayor DBO de salida promedio?
2. ¿Qué porcentaje de registros cumple la norma ambiental?
3. ¿Cómo evoluciona el DBO de salida en el tiempo?
4. ¿Existe relación entre el caudal de entrada y el DBO de salida?

## Trabajo colaborativo
El proyecto utiliza dos archivos externos compartidos:
- funciones_estadisticas.py
- funciones_reportes.py

Estos módulos permiten reutilizar funciones dentro del notebook principal.

## Metodología
- Carga del dataset.
- Evaluación de calidad de datos.
- Creación de variables derivadas.
- Uso de funciones externas compartidas.
- Construcción de dashboard 2x2.
- Exportación de reportes para dos áreas.

## Resultados
- La Planta Norte presenta el mayor DBO de salida promedio con 36.6 mg/L.
- El 77.5% de los registros presenta incumplimiento normativo.
- La evolución temporal no muestra una tendencia clara de mejora.
- El caudal de entrada no explica por sí solo los incumplimientos.

## Decisiones recomendadas
- Priorizar revisión de la Planta Norte por mayor DBO de salida promedio.
- Investigar las causas del alto porcentaje de incumplimiento normativo.
- Monitorear los periodos de mayor DBO para planificar intervenciones.
- Usar los reportes exportados para apoyar decisiones por área.

## Reflexión ética
El análisis debe utilizarse para mejorar el proceso de tratamiento sin generar 
decisiones perjudiciales para comunidades específicas. Los resultados deben 
interpretarse considerando las limitaciones del dataset y el contexto operacional 
de cada planta. La comunicación de los incumplimientos debe ser equilibrada, 
presentando tanto los resultados críticos como las acciones correctivas disponibles.


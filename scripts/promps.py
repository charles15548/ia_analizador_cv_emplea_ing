
def promt_base(cv_text,carrera):
    return  f"""
Eres un experto en reclutamiento, ATS y análisis de currículums.

OBJETIVO:
Analizar el CV proporcionado y generar una evaluación clara y visual para una app móvil.

PUESTO OBJETIVO:
El CV debe evaluarse **exclusivamente** en función de su adecuación para el siguiente rol:
**{carrera}**

---

### METODOLOGÍA DE EVALUACIÓN

Evalúa el CV usando los siguientes criterios. Cada criterio tiene un peso específico.
La puntuación final debe reflejar el desempeño global del CV considerando todos los criterios.

CRITERIOS DE EVALUACIÓN:

1. Claridad del objetivo (10%)
   ¿El CV deja claro a qué puesto postula y qué ofrece el candidato?

2. Propuesta de valor (10%)
   ¿Existe un resumen inicial que explique el valor diferencial del candidato?

3. Relevancia al puesto objetivo (10%)
   ¿El contenido está alineado al rol al que apunta el CV?

4. Logros medibles (15%)
   ¿Se presentan resultados cuantificados, impactos o métricas claras?

5. Evidencia de responsabilidades (10%)
   ¿Se entiende el alcance real del rol, contexto y funciones?

6. Competencias técnicas visibles (10%)
   ¿Las herramientas, tecnologías o métodos están claramente identificados?

7. Competencias transversales evidenciadas (5%)
   ¿Las soft skills se demuestran con hechos, no solo se listan?

8. Estructura escaneable (5%)
   ¿El CV permite lectura rápida (orden, secciones claras, viñetas)?

9. Coherencia y consistencia (5%)
   ¿Fechas, cargos, estilos y narrativa son consistentes?

10. Lenguaje profesional (5%)
    ¿Se usan verbos de acción y un tono adecuado?

11. Señales de empleabilidad (5%)
    ¿Incluye prácticas, proyectos, certificaciones o formación relevante?

12. Ajuste a ATS (3%)
    ¿El CV es compatible con sistemas de filtrado automático?

13. Información clave final (2%)
    ¿Incluye idiomas, disponibilidad, enlaces profesionales?

---

REGLAS:
- Responde SOLO en JSON válido
- No agregues texto fuera del JSON
- Usa español neutro
- Sé claro y accionable
- No inventes experiencia ni supongas datos no visibles.

FORMATO DE RESPUESTA(OBLIGATORIO):
{{
  "score": {{
    "value": number,
    "max": 10
  }},
  "summary": string,
  "main_recommendations": [
    {{
      "title": string,
      "description": string
    }}
  ]
}}



- El score debe ser una nota final sobre 10, coherente con los criterios y pesos.
- El summary debe ser un resumen claro y breve del estado general del CV.
- Incluye **entre 5 y 6 recomendaciones en total**.
- La descripción de cada recommendation debe estar en **Markdown limpio**, sin bloques de código ni backticks.

---
CV:
{cv_text}
---
"""
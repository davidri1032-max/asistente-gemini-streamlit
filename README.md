# 💼 Simulador de Entrevistas Técnicas con IA (Challenge Lab)

Aplicación Web interactiva desarrollada con **Streamlit** y el **SDK oficial de Google Gemini (`google-genai`)**, diseñada para simular un proceso de selección técnica conducido por un **Líder Técnico Virtual**.

Proyecto desarrollado como entregable para el **Challenge Lab Autónomo** de la asignatura **Sistemas Inteligentes** en la **Universidad Autónoma de Occidente (UAdeO)**.

---

## 📋 Información Académica y del Proyecto
- **Institución:** Universidad Autónoma de Occidente (UAdeO)
- **Materia:** Sistemas Inteligentes
- **Docente:** Dra. Aiblis Susej Herrera Palafox
- **Modelo de IA:** Gemini Flash (`gemini-3.5-flash-lite`, `gemini-3.5-flash`, `gemini-3.8-flash`)
- **SDK Oficial:** `google-genai`
- **Framework Web:** Streamlit
- **Control de Versiones:** Git & GitHub
- **Plataforma de Despliegue:** Streamlit Community Cloud

---

## 🎯 Cumplimiento de Especificaciones del Sistema

| Bloque | Requerimiento | Implementación en la Aplicación |
| :--- | :--- | :--- |
| **A. Interfaz y Configuración** | Selector de rol (`st.selectbox`) con al menos 3 vacantes. | Selector dinámico con: *Desarrollador Python Junior*, *Desarrollador Web Frontend* e *Integrador de APIs y Bots*. |
| **A. Interfaz y Configuración** | Botón visible de "Reiniciar Entrevista". | Botón `🔄 Reiniciar Entrevista` en la barra lateral que limpia memoria, contadores y reinicia la sesión limpiamente. |
| **B. Lógica Conversacional** | Límite estricto de exactamente 3 preguntas. | Control de estado con `st.session_state.turn_count`, barra de progreso y finalización automática al 3.er turno. |
| **B. Lógica Conversacional** | Dinámica adaptativa de preguntas. | Cada pregunta se construye tomando en cuenta la respuesta y profundidad previa del candidato. |
| **B. Lógica Conversacional** | Transición de estado tras la 3.ª respuesta. | Se desactiva el chat de preguntas y se activa de inmediato el reporte estructurado de evaluación. |
| **C. Protección de Rol** | System Instructions y Anti-Jailbreak. | Prompt estricto de Líder Técnico. Si el candidato intenta desviar el tema (pedir recetas, chistes, etc.), el sistema lo declina amablemente, lo reorienta y no consume turnos. |
| **D. Reporte Final** | Reporte estructurado en Markdown. | Generación automática con: 1. Calificación Global (1-10), 2. Fortalezas Detectadas (>=2), 3. Áreas de Mejora (>=2) y 4. Dictamen Final (`APROBADO` o `NO APROBADO`). |

---

## 🧪 Matriz de Casos de Prueba (Edge Cases Superados)

1. **Intento de distracción / Jailbreak:**  
   El bot declina amablemente salir de su personaje de Líder Técnico, solicita enfocarse en la prueba técnica y reorienta a la pregunta pendiente sin incrementar el contador de turnos.
2. **Límite estricto de turnos:**  
   Tras la respuesta #3, no se genera una 4.ª pregunta; se concluye la fase de preguntas y se emite directamente el reporte final.
3. **Reinicio limpio de sesión:**  
   Al pulsar *Reiniciar Entrevista*, el contador vuelve a 0, el historial se borra y la aplicación formula una nueva primera pregunta sin errores en pantalla.
4. **Coherencia por vacante:**  
   - *Desarrollador Python Junior:* Preguntas sobre mutabilidad, estructuras de datos, funciones y generadores.  
   - *Desarrollador Web Frontend:* Preguntas sobre JavaScript moderno, DOM, layouts y rendimiento.  
   - *Integrador de APIs y Bots:* Preguntas sobre REST, Webhooks, autenticación e idempotencia.

---

## 📁 Estructura del Repositorio

```text
asistente-gemini-streamlit/
├── app.py                 # Aplicación principal de Streamlit con toda la lógica del simulador
├── requirements.txt       # Dependencias oficiales (streamlit, google-genai)
├── .gitignore             # Protección de credenciales y archivos locales
├── .streamlit/
│   └── secrets.toml       # Clave de API local (NO se sube al repositorio público)
├── run.bat                # Script de inicio rápido para Windows
└── README.md              # Documentación detallada del proyecto y despliegue
```

---

## 🚀 1. Ejecución Local en Windows

### Paso A: Instalar dependencias
Abre una terminal en la carpeta del proyecto y ejecuta:
```bash
python -m pip install -r requirements.txt
```

### Paso B: Configurar la API Key de Gemini
Crea o edita el archivo `.streamlit/secrets.toml` con tu clave de [Google AI Studio](https://aistudio.google.com/):
```toml
GEMINI_API_KEY = "tu_clave_de_gemini_aqui"
```

### Paso C: Iniciar el servidor de Streamlit
Ejecuta el siguiente comando en la terminal:
```bash
python -m streamlit run app.py
```
*(O simplemente haz doble clic en `run.bat`)*.

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`.

---

## 🌐 2. Publicación en GitHub y Despliegue en Streamlit Community Cloud

### Paso 1: Subir cambios al repositorio de GitHub
```bash
git add app.py requirements.txt run.bat README.md .gitignore
git commit -m "feat: Simulador de Entrevistas Técnicas con IA completado"
git push origin main
```

### Paso 2: Desplegar en Streamlit Cloud
1. Ve a [share.streamlit.io](https://share.streamlit.io) e inicia sesión con tu cuenta de GitHub.
2. Selecciona tu repositorio: `asistente-gemini-streamlit` y la rama `main`.
3. El archivo principal debe ser `app.py`.
4. Abre **Advanced settings...** y en la sección **Secrets** ingresa:
   ```toml
   GEMINI_API_KEY = "TU_GEMINI_API_KEY"
   ```
5. Haz clic en **Deploy!**.

---

## 📌 Entregables del Desafío
1. **Enlace Público:** URL de la app desplegada en `https://tu-app.streamlit.app`.
2. **Repositorio en GitHub:** Código fuente con `app.py` y `requirements.txt`.
3. **Evidencia de Ejecución:** Captura de pantalla de la entrevista de 3 preguntas y del reporte final generado.

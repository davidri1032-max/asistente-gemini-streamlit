# 🤖 Asistente Virtual 'Astra' - Sistemas Inteligentes (UAdeO)

Aplicación Web interactiva desarrollada con **Streamlit** y la **API de Google Gemini**, lista para desplegarse en **Streamlit Community Cloud**.

---

## 📋 Información del Proyecto
- **Institución:** Universidad Autónoma de Occidente (UAdeO)
- **Materia:** Sistemas Inteligentes
- **Docente:** Dra. Aiblis Susej Herrera Palafox
- **Modelo de IA:** Gemini 3.8 Flash (`gemini-3.8-flash`)
- **Framework Web:** Streamlit

---

## 📁 Estructura del Repositorio

```text
asistente-gemini-streamlit/
├── app.py                 # Aplicación principal de Streamlit con chat conversacional
├── requirements.txt       # Dependencias necesarias (streamlit, google-genai)
├── .gitignore             # Ignora credenciales y archivos temporales
├── .streamlit/
│   └── secrets.toml       # Clave de API local (NO se sube a GitHub)
├── .env                   # Variables de entorno locales de respaldo
├── run.bat                # Acceso rápido en Windows para iniciar la app
├── lab_guide.html         # Guía de laboratorio interactiva original
└── README.md              # Documentación e instrucciones
```

---

## 🚀 1. Ejecución Local en tu Computadora

### Paso A: Instalar dependencias
Abre la terminal en la carpeta del proyecto y ejecuta:
```bash
python -m pip install --default-timeout=1000 streamlit google-genai
```

### Paso B: Configurar la clave de Gemini
El proyecto ya cuenta con el archivo `.streamlit/secrets.toml` con tu clave:
```toml
GEMINI_API_KEY = "TU_CLAVE_AQUI"
```

### Paso C: Ejecutar el servidor de Streamlit
> ⚠️ **Importante:** Streamlit **NO** se corre con el botón ▶ de VS Code ni con `python app.py`.

Ejecuta el siguiente comando en la terminal:
```bash
python -m streamlit run app.py
```
*(O simplemente haz doble clic en `run.bat`)*.

Se abrirá automáticamente en tu navegador: `http://localhost:8501`.

---

## 🌐 2. Publicación en GitHub y Despliegue en Streamlit Cloud

### Paso 1: Subir a GitHub
1. Entra a [github.com](https://github.com) y crea un nuevo repositorio público llamado:
   `asistente-gemini-streamlit`
2. En la terminal de esta carpeta, inicializa y sube tu código:
   ```bash
   git init
   git add app.py requirements.txt .gitignore README.md
   git commit -m "feat: Asistente Astra con Streamlit y Gemini API"
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/asistente-gemini-streamlit.git
   git push -u origin main
   ```
   *(El archivo `.gitignore` garantiza que tu `.streamlit/secrets.toml` y claves personales jamás se publiquen en internet)*.

### Paso 2: Desplegar gratis en Streamlit Community Cloud
1. Ingresa a [share.streamlit.io](https://share.streamlit.io) e inicia sesión con tu cuenta de GitHub.
2. Presiona el botón **Create app**.
3. Selecciona tu repositorio: `TU_USUARIO/asistente-gemini-streamlit` y la rama `main`.
4. El archivo principal debe ser: `app.py`.
5. Despliega **Advanced settings...** y en el recuadro **Secrets** escribe:
   ```toml
   GEMINI_API_KEY = "TU_GEMINI_API_KEY_REAL_AQUI"
   ```
6. Haz clic en **Deploy!**.

---

## 🎓 Entregable del Laboratorio
Una vez finalizado el despliegue, obtendrás tu URL pública con certificado HTTPS:
```text
https://tu-usuario-asistente-gemini.streamlit.app
```
Copia este enlace y envíalo junto a tu repositorio de GitHub como evidencia de la práctica.

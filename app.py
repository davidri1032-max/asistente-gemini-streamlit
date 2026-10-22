import os
import streamlit as st
from google import genai
from google.genai import types

# ==============================================================================
# 1. CONFIGURACIÓN DE LA PÁGINA WEB
# ==============================================================================
st.set_page_config(
    page_title="Asistente AI - Sistemas Inteligentes",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Asistente Virtual 'Astra'")
st.caption("UAdeO • Materia: Sistemas Inteligentes • Dra. Aiblis Susej Herrera Palafox")

# ==============================================================================
# 2. GESTIÓN SEGURA DE LA API KEY (LOCAL Y STREAMLIT CLOUD)
# ==============================================================================
try:
    # Intenta leer la clave desde los secretos de Streamlit Cloud o .streamlit/secrets.toml
    api_key = st.secrets[AQ.Ab8RN6J97G4hEIp1Q2lErcz4uozMni-ltIF77lSqKI7oCz3ePA]
except Exception:
    # ⚠️ REEMPLAZA ESTA CADENA POR TU CLAVE REAL DE GOOGLE AI STUDIO PARA PRUEBAS LOCALES
    api_key =AQ.Ab8RN6J97G4hEIp1Q2lErcz4uozMni-ltIF77lSqKI7oCz3ePA

# Fallback complementario: variable de entorno del sistema o archivo .env
if not api_key or api_key == AQ.Ab8RN6J97G4hEIp1Q2lErcz4uozMni-ltIF77lSqKI7oCz3ePA:
    api_key = os.getenv(AQ.Ab8RN6J97G4hEIp1Q2lErcz4uozMni-ltIF77lSqKI7oCz3ePA, "")

# ==============================================================================
# 3. CONFIGURACIÓN DE PERSONALIDAD DEL BOT
# ==============================================================================
CONFIG_INSTRUCCIONES = types.GenerateContentConfig(
    system_instruction=(
        "Eres 'Astra', un asistente académico inteligente, formal y estructurado para la materia "
        "Sistemas Inteligentes de la UAdeO. Tu objetivo es explicar conceptos de Inteligencia Artificial, "
        "Agentes y Redes Neuronales de forma clara y accesible. Si te preguntan por entregas o fechas, "
        "indica amablemente que deben verificar las indicaciones de la Dra. Aiblis Susej Herrera Palafox."
    ),
    temperature=0.7
)

# Validar si se cuenta con API Key antes de continuar
if not api_key or api_key == "GEMINI_API_KEY":
    st.warning("⚠️ No se ha detectado una API Key de Gemini.")
    st.info("💡 En **Streamlit Cloud**: Configúrala en *Advanced Settings > Secrets* como `GEMINI_API_KEY = \"tu_clave\"`.\n\n"
            "💡 En **Local**: Colócala en el archivo `.streamlit/secrets.toml` o ingrésala en la barra lateral.")
    api_key = st.sidebar.text_input("🔑 Ingresa tu Gemini API Key:", type="password")
    if not api_key:
        st.stop()

# Modelo especificado en la práctica de laboratorio
MODEL_NAME = "gemini-3.8-flash"

# ==============================================================================
# 4. INICIALIZACIÓN PERSISTENTE EN MEMORIA (PREVIENE ERRORES DE CONEXIÓN)
# ==============================================================================
# Se guarda tanto el cliente como el chat en st.session_state para mantenerlos vivos
if "client" not in st.session_state or st.session_state.get("current_api_key") != api_key:
    try:
        st.session_state.client = genai.Client(api_key=api_key)
        st.session_state.current_api_key = api_key
        st.session_state.chat_session = st.session_state.client.chats.create(
            model=MODEL_NAME,
            config=CONFIG_INSTRUCCIONES
        )
    except Exception as e:
        st.error(f"❌ Error al inicializar el cliente de Gemini: {e}")
        st.stop()

# Historial gráfico de mensajes
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "👋 ¡Hola! Soy Astra. ¿En qué tema de Sistemas Inteligentes te puedo ayudar hoy?"}
    ]

# ==============================================================================
# 5. BARRA LATERAL (OPCIONES DE REINICIO)
# ==============================================================================
with st.sidebar:
    st.header("⚙️ Opciones del Agente")
    st.markdown(f"Modelo backend: **{MODEL_NAME}**")
    st.markdown("---")
    st.markdown("👨‍🎓 **Universidad Autónoma de Occidente**")
    st.markdown("📚 **Materia:** Sistemas Inteligentes")
    st.markdown("👩‍🏫 **Docente:** Dra. Aiblis Susej Herrera Palafox")
    st.markdown("---")
    
    if st.button("🧹 Limpiar Conversación"):
        try:
            st.session_state.chat_session = st.session_state.client.chats.create(
                model=MODEL_NAME,
                config=CONFIG_INSTRUCCIONES
            )
        except Exception as e:
            st.error(f"Error al reiniciar chat: {e}")
            
        st.session_state.messages = [
            {"role": "assistant", "content": "🧹 La sesión ha sido reiniciada. ¿Qué otra duda tienes?"}
        ]
        st.rerun()

# ==============================================================================
# 6. RENDERIZADO DEL HISTORIAL DE MENSAJES
# ==============================================================================
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ==============================================================================
# 7. ENTRADA DE TEXTO Y PROCESAMIENTO
# ==============================================================================
if user_input := st.chat_input("Escribe tu pregunta o duda aquí..."):
    # Renderizar el mensaje del usuario de inmediato
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generar la respuesta llamando a la API de Gemini
    with st.chat_message("assistant"):
        with st.spinner("Pensando respuesta..."):
            try:
                response = st.session_state.chat_session.send_message(user_input)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"❌ Error al consultar la API: {e}")

import streamlit as st

st.set_page_config(page_title="Timeline de IA", layout="centered")

st.title("🧠 Timeline Interactivo del Desarrollo de la Inteligencia Artificial")

st.write(
    "Usa la barra deslizante para explorar cinco hitos importantes en la historia de la IA."
)

# Datos del timeline
eventos = {
    1: {
        "año": 1950,
        "titulo": "Test de Turing",
        "descripcion": "Alan Turing propone el famoso test para evaluar si una máquina puede mostrar inteligencia similar a la humana."
    },
    2: {
        "año": 1956,
        "titulo": "Nacimiento de la IA",
        "descripcion": "Conferencia de Dartmouth: John McCarthy acuña el término *inteligencia artificial*."
    },
    3: {
        "año": 1997,
        "titulo": "Deep Blue vence al campeón mundial",
        "descripcion": "La supercomputadora de IBM vence a Garry Kasparov, marcando un hito en el aprendizaje automatizado."
    },
    4: {
        "año": 2012,
        "titulo": "Revolución del Deep Learning",
        "descripcion": "La red neuronal AlexNet gana ImageNet con una enorme mejora, impulsando el uso masivo del aprendizaje profundo."
    },
    5: {
        "año": 2023,
        "titulo": "IA generativa se masifica",
        "descripcion": "Modelos como GPT, DALL·E y otros popularizan la creación automática de texto e imágenes."
    }
}

# Slider
seleccion = st.slider(
    "Selecciona un hito de la historia:",
    min_value=1,
    max_value=5,
    value=1,
    format="Hito %d"
)

evento = eventos[seleccion]

# Mostrar contenido
st.subheader(f"📌 {evento['año']} — {evento['titulo']}")
st.write(evento["descripcion"])

import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Te Amo ❤️", layout="centered")

# HTML + CSS del corazón
html_code = """
<style>
body {
    background-color: #111;
}

.contenedor {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 80vh;
}

.corazon {
    width: 100px;
    height: 100px;
    background: red;
    position: relative;
    transform: rotate(-45deg);
    margin-bottom: 30px;
    animation: latido 1s infinite;
}

.corazon::before,
.corazon::after {
    content: "";
    width: 100px;
    height: 100px;
    background: red;
    border-radius: 50%;
    position: absolute;
}

.corazon::before {
    top: -50px;
    left: 0;
}

.corazon::after {
    left: 50px;
    top: 0;
}

@keyframes latido {
    0% { transform: scale(1) rotate(-45deg); }
    50% { transform: scale(1.2) rotate(-45deg); }
    100% { transform: scale(1) rotate(-45deg); }
}

.texto {
    font-size: 2em;
    color: pink;
    text-align: center;
}
</style>

<div class="contenedor">
    <div class="corazon"></div>
    <div class="texto">Te amo mucho amor 💖</div>
</div>
"""

# Mostrar en Streamlit
st.markdown(html_code, unsafe_allow_html=True)
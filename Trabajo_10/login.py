import streamlit as st

Usuario = "admin"
Contraseña = "Admin2026"
Intentos = 3

if "login" not in st.session_state:
    st.session_state.login = False

if "intentos" not in st.session_state:
    st.session_state.intentos = 0

st.set_page_config(page_title="Sistema", layout="centered")

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #e8eef5 0%, #dce7f3 100%);
    }

    .block-container {
        max-width: 900px;
        padding-top: 3rem;
    }

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        color: #172033;
        margin-bottom: 4px;
    }

    .subtitle {
        text-align: center;
        font-size: 16px;
        color: #4b5563;
        margin-bottom: 35px;
    }

    .section-box {
        background: #ffffff;
        padding: 30px;
        border-radius: 18px;
        box-shadow: 0 8px 28px rgba(15, 23, 42, 0.10);
        border: 1px solid #d9e2ec;
        margin-bottom: 24px;
    }

    .section-title {
        font-size: 26px;
        font-weight: 800;
        color: #111827;
        margin-bottom: 10px;
    }

    .small-text {
        color: #4b5563;
        font-size: 15px;
        margin-bottom: 22px;
    }

    label, .stTextInput label, .stNumberInput label, .stSelectbox label {
        color: #1f2937 !important;
        font-weight: 600 !important;
    }

    input {
        background-color: #ffffff !important;
        color: #111827 !important;
        border: 1.5px solid #9ca3af !important;
        border-radius: 10px !important;
    }

    input:focus {
        border-color: #2563eb !important;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.18) !important;
    }

    div.stButton > button {
        border-radius: 10px;
        height: 45px;
        font-weight: 700;
        border: none;
        background-color: #2563eb;
        color: white;
    }

    div.stButton > button:hover {
        background-color: #1d4ed8;
        color: white;
        border: none;
    }

    div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #111827 !important;
        border-radius: 10px !important;
        border: 1.5px solid #9ca3af !important;
    }

    [data-testid="stHeader"] {
        background: #0f172a;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">Sistema de Gestión</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Panel básico con inicio de sesión y operaciones principales</div>', unsafe_allow_html=True)

if not st.session_state.login:

    st.markdown("""
    <div class="section-box">
        <div class="section-title">Inicio de Sesión</div>
        <div class="small-text">Ingresa tus credenciales para acceder al sistema.</div>
    </div>
    """, unsafe_allow_html=True)

    usuario = st.text_input("Usuario")
    clave = st.text_input("Contraseña", type="password")

    if st.button("Ingresar", use_container_width=True):

        if st.session_state.intentos >= Intentos:
            st.error("Acceso bloqueado.")
        
        elif not usuario.isalnum():
            st.error("Usuario invalido.")
            st.session_state.intentos += 1

        elif len(clave) < 8 or not any(c.isalpha() for c in clave) or not any(c.isdigit() for c in clave):
            st.error("Contraseña invalida.")
            st.session_state.intentos += 1

        elif usuario == Usuario and clave == Contraseña:
            st.session_state.login = True
            st.session_state.intentos = 0
            st.rerun()

        else:
            st.session_state.intentos += 1
            st.error(f"Credenciales incorrectas ({st.session_state.intentos}/{Intentos})")

else:

    st.markdown("""
    <div class="section-box">
        <div class="section-title">Panel Principal</div>
        <div class="small-text">Selecciona una opción para continuar.</div>
    </div>
    """, unsafe_allow_html=True)

    opcion = st.selectbox(
        "Seleccione una opcion",
        ["Clasificar Numero", "Categoria Edad", "Calcular Tarifa"]
    )

    if opcion == "Clasificar Numero":

        st.markdown("""
        <div class="section-box">
            <div class="section-title">Clasificar Número</div>
            <div class="small-text">Determina si un número es positivo, negativo o cero.</div>
        </div>
        """, unsafe_allow_html=True)

        numero = st.number_input("Numero", value=0)

        if st.button("Clasificar"):

            if numero > 0:
                st.success("Numero positivo")

            elif numero < 0:
                st.error("Numero negativo")

            else:
                st.info("Numero cero")

    elif opcion == "Categoria Edad":

        st.markdown("""
        <div class="section-box">
            <div class="section-title">Categoría de Edad</div>
            <div class="small-text">Clasifica a la persona según su edad.</div>
        </div>
        """, unsafe_allow_html=True)

        edad = st.number_input("Edad", 0, 120, 18)

        if st.button("Ver Categoria"):

            if edad < 13:
                st.info("Niño")

            elif edad < 18:
                st.warning("Adolescente")

            elif edad < 65:
                st.success("Adulto")

            else:
                st.info("Adulto mayor")

    else:

        st.markdown("""
        <div class="section-box">
            <div class="section-title">Calcular Tarifa</div>
            <div class="small-text">Calcula el total según precio y edad del cliente.</div>
        </div>
        """, unsafe_allow_html=True)

        precio = st.number_input("Precio", min_value=0.0, value=100.0)
        edad = st.number_input("Edad Cliente", 0, 120, 30)

        if st.button("Calcular"):

            descuento = 0.15 if edad < 18 else 0.20 if edad >= 65 else 0
            total = precio * (1 - descuento)

            st.success(f"Total: ${total:.2f}")

    st.divider()

    if st.button("Cerrar Sesion", use_container_width=True):

        st.session_state.login = False
        st.rerun()
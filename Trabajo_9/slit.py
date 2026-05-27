
import streamlit as st


class LoginStreamlitApp:
    def __init__(self) -> None:
        self.usuario_correcto = "admin"
        self.contrasena_correcta = "admin2026"

        if "autenticado" not in st.session_state:
            st.session_state.autenticado = False

    def ejecutar(self) -> None:
        st.set_page_config(page_title="Login Streamlit", page_icon="🔐", layout="centered")
        st.title("Login con Streamlit")

        if st.session_state.autenticado:
            self.mostrar_panel()
        else:
            self.mostrar_login()

    def mostrar_login(self) -> None:
        with st.form("form_login"):
            usuario = st.text_input("Usuario")
            contrasena = st.text_input("Contraseña", type="password")
            enviar = st.form_submit_button("Ingresar", use_container_width=True)

        if enviar:
            if usuario.strip() == self.usuario_correcto and contrasena.strip() == self.contrasena_correcta:
                st.session_state.autenticado = True
                st.success("Bienvenido, administrador.")
                st.rerun()
            else:
                st.error("Usuario o contraseña incorrectos.")

    def mostrar_panel(self) -> None:
        st.success("Sesión iniciada correctamente.")
        st.subheader("Panel principal")
        st.write("Usuario autenticado: admin")

        if st.button("Cerrar sesión", use_container_width=True):
            st.session_state.autenticado = False
            st.rerun()


app = LoginStreamlitApp()
app.ejecutar()












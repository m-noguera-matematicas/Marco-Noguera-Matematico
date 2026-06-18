import streamlit as st

st.set_page_config(
    page_title="Portal Docente",
    page_icon="📚",
    layout="wide"
)

col1, col2 = st.columns([1,2])

with col1:

    st.image("foto.jpeg", width=320)

with col2:

    st.title("Marco Nogal")

    st.header("Matemático")

    #st.divider()

    st.write("""
Soy **Marco Antonio Noguera Alvarenga**, venezolano de nacimiento y mexicano de corazón.
Desde hace más de **17 años** tengo el privilegio de dedicarme a la docencia universitaria,
una profesión que considero no solo un trabajo, sino una verdadera vocación.

Mi formación académica es la de **Matemático**. A lo largo de mi trayectoria he impartido 
diferentes tipos de cursos entorno a las matemáticas a nivel universitario, convencido 
de que las matemáticas son una herramienta fundamental para
comprender el mundo y desarrollar el pensamiento crítico y que la educación es el camino 
más sólido para construir una mejor sociedad.

Fuera del aula disfruto de una buena taza de café, la ciencia ficción, la lectura,
el metal sinfónico y el estudio de temas relacionados con la ciencia y la filosofía.

> *"No podemos elegir las circunstancias, pero siempre podemos elegir la manera de responder a ellas."*

Bienvenido a este portal.
""")

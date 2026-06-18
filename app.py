import streamlit as st

st.set_page_config(
    page_title="Portal Docente",
    page_icon="📚",
    layout="wide"
)

col1, col2 = st.columns([1,2])

with col1:

    st.image("foto.jpeg", width=300)

with col2:

    st.title("Marco Nogal")

    st.subheader("Matemático")

    #st.divider()

    st.write("""
Soy **Marco Antonio Noguera Alvarenga**, venezolano de nacimiento y mexicano de corazón.
Desde hace más de **17 años** tengo el privilegio de dedicarme a la docencia universitaria,
una profesión que considero no solo un trabajo, sino una verdadera vocación.

Mi formación académica es la de **Matemático**. A lo largo de mi trayectoria he impartido
cursos de cálculo, probabilidad, estadística, investigación de operaciones y diseño de
experimentos, convencido de que las matemáticas son una herramienta fundamental para
comprender el mundo y desarrollar el pensamiento crítico.

Creo firmemente que la educación es el camino más sólido para construir una mejor sociedad,
y que un buen profesor no solo transmite conocimientos, sino también curiosidad,
disciplina y el deseo permanente de aprender.

Fuera del aula disfruto de una buena taza de café, la ciencia ficción, la lectura,
el metal sinfónico y el estudio de temas relacionados con la ciencia y la filosofía.

> *"No podemos elegir las circunstancias, pero siempre podemos elegir la manera de responder a ellas."*

Bienvenido a este portal.
""")

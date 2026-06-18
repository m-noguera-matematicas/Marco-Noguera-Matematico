import streamlit as st

st.set_page_config(
    page_title="Materiales de Matemáticas",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Materiales de Matemáticas")
st.subheader("Marco Antonio Noguera Alvarenga")

col1, col2 = st.columns([1, 2])

with col1:
    st.image("foto.jpg", caption="Marco Antonio Noguera Alvarenga", width=260)

with col2:
    st.markdown("""
Soy profesor de matemáticas con interés en la enseñanza del cálculo,
la probabilidad, la estadística, el diseño de experimentos y la investigación
de operaciones.

Este sitio reúne materiales de apoyo para mis estudiantes: notas de clase,
problemarios, tareas, exámenes y documentos complementarios.
""")

st.divider()

st.header("Cursos disponibles")

col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/1_Calculo.py", label="📘 Cálculo", icon="📘")
    st.page_link("pages/2_Probabilidad_Estadistica.py", label="📊 Probabilidad y Estadística", icon="📊")
    st.page_link("pages/3_Diseno_Experimentos.py", label="🧪 Diseño de Experimentos", icon="🧪")

with col2:
    st.page_link("pages/4_Investigacion_Operaciones.py", label="📈 Investigación de Operaciones", icon="📈")

st.divider()

st.caption("Sitio académico para distribución de materiales de clase.")

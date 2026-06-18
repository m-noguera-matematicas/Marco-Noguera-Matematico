import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Portal Docente | Marco Noguera",
    page_icon="📚",
    layout="wide"
)

# -----------------------------
# Datos generales
# -----------------------------

MATERIAS = {
    "Cálculo Integral": "materiales/calculo_integral",
    "Cálculo para Administración": "materiales/calculo_administracion",
    "Probabilidad y Estadística": "materiales/probabilidad_estadistica",
    "Estadística Inferencial": "materiales/estadistica_inferencial",
    "Diseño de Experimentos": "materiales/diseno_experimentos",
    "Investigación de Operaciones": "materiales/investigacion_operaciones",
}


def mostrar_pdfs(carpeta):
    ruta = Path(carpeta)

    if not ruta.exists():
        st.info("Aún no hay materiales cargados para esta materia.")
        return

    archivos_pdf = sorted(ruta.glob("*.pdf"))

    if not archivos_pdf:
        st.info("Aún no hay archivos PDF en esta sección.")
        return

    for archivo in archivos_pdf:
        with open(archivo, "rb") as f:
            st.download_button(
                label=f"📄 Descargar {archivo.stem}",
                data=f,
                file_name=archivo.name,
                mime="application/pdf"
            )


# -----------------------------
# Barra lateral
# -----------------------------

st.sidebar.title("📚 Portal Docente")

seccion = st.sidebar.radio(
    "Selecciona una sección",
    ["Inicio"] + list(MATERIAS.keys())
)

st.sidebar.divider()
st.sidebar.caption("Marco Antonio Noguera Alvarenga")


# -----------------------------
# Página principal
# -----------------------------

if seccion == "Inicio":
    st.title("Portal Docente")
    st.subheader("Marco Antonio Noguera Alvarenga")

    col1, col2 = st.columns([1, 2])

    with col1:
        try:
            st.image("foto.jpg", caption="Marco Antonio Noguera Alvarenga", width=260)
        except:
            st.info("Aquí irá tu fotografía.")

    with col2:
        st.markdown("""
Soy profesor de matemáticas. Este portal reúne materiales de apoyo para mis cursos:
notas de clase, libros, problemarios, tareas, exámenes y documentos complementarios.

Por ahora el sitio funcionará como repositorio de archivos PDF. Más adelante se podrán
agregar enlaces a videos, páginas web, simuladores, aplicaciones interactivas y otros
recursos digitales.
""")

    st.divider()

    st.header("Materias disponibles")

    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("""
- 📘 **Cálculo Integral**
- 📗 **Cálculo para Administración**
- 📊 **Probabilidad y Estadística**
""")

    with col_b:
        st.markdown("""
- 📈 **Estadística Inferencial**
- 🧪 **Diseño de Experimentos**
- ⚙️ **Investigación de Operaciones**
""")

    st.info("Usa el menú lateral para entrar a cada materia.")


# -----------------------------
# Páginas de materias
# -----------------------------

else:
    st.title(seccion)
    st.write("Materiales disponibles para descarga.")

    carpeta = MATERIAS[seccion]
    mostrar_pdfs(carpeta)

    st.divider()
    st.caption("Más adelante esta sección podrá incluir enlaces, videos y aplicaciones interactivas.")

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


import streamlit as st
import zipfile
import io
from pathlib import Path

st.title("📂 Organizador de Archivos (ZIP)")
st.write("Sube varios archivos y te los devolveré organizados en un archivo ZIP por categorías.")

uploaded_files = st.file_uploader("Elige tus archivos", accept_multiple_files=True)

if uploaded_files:
    # Creamos un archivo ZIP en memoria
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "x", zipfile.ZIP_DEFLATED) as zf:
        for file in uploaded_files:
            # Lógica de categorización
            ext = Path(file.name).suffix.lower()
            if ext in ['.jpg', '.png', '.jpeg']: folder = "Imagenes/"
            elif ext in ['.pdf', '.docx', '.txt']: folder = "Documentos/"
            else: folder = "Otros/"
            
            # Escribimos dentro del ZIP con la estructura de carpetas
            zf.writestr(f"{folder}{file.name}", file.getvalue())
            
    st.download_button(
        label="⬇️ Descargar archivos organizados (.zip)",
        data=buf.getvalue(),
        file_name="archivos_organizados.zip",
        mime="application/zip"
    )

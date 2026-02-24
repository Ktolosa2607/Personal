import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

st.title("🌐 Extractor de Titulares Web")
st.write("Introduce una URL para extraer los encabezados (h2).")

url = st.text_input("URL del sitio:", "https://elpais.com")

if st.button("Extraer Datos"):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        titulos = [t.get_text(strip=True) for t in soup.find_all('h2')]
        
        if titulos:
            df = pd.DataFrame(titulos, columns=["Titulares Encontrados"])
            st.success(f"¡Se encontraron {len(titulos)} titulares!")
            st.table(df) # Muestra una tabla limpia
        else:
            st.warning("No se encontraron etiquetas <h2> en esta página.")
            
    except Exception as e:
        st.error(f"Error: {e}")

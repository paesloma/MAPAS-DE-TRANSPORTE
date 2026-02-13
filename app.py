import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Configuración de la página
st.set_page_config(page_title="Mapa de Despachos y Cobertura", layout="wide")
st.title("📍 Mapa de Cobertura de Despachos - A Nivel Nacional")
st.markdown("Visualización de los puntos de distribución, transportistas y contactos en Ecuador.")

# Datos extraídos de las imágenes (con coordenadas aproximadas de las ciudades principales)
data = {
    "Despacho": [
        "Bodega Guayaquil", "Bodega Quito", "Bodega Manta", "Bodega Ambato", 
        "Loja", "Machala", "Riobamba", "Milagro", "Bodega Sto Domingo", 
        "Ibarra", "Cuenca"
    ],
    "Transporte": [
        "TRAINHCO", "IZCONT", "AUSTROVELO", "PIONEROS", 
        "GAVIOTAS", "GAVIOTAS", "BENZOR", "FLOTA CAÑARI", "MANUEL ORTIZ", 
        "XLM E HIJOS", "TRANSPORTE EMPRESA"
    ],
    "Contacto": [
        "Fernando Aucapiña", "Magaly Izquierdo", "David Avila", "Arturo Arequipa",
        "Luis Tapia", "Luis Tapia", "Milton Vasconez", "Antonio Encalada", "Manuel Ortiz",
        "Javier Perez", "Pedro Davila / Andres Vargas"
    ],
    "Teléfono": [
        "0958921894", "0992185765", "0969351070", "0983246371",
        "0991449793", "0991449793", "0999400262", "0999556788", "0993722448",
        "0996129736", "0998527171"
    ],
    "Latitud": [
        -2.1894, -0.1807, -0.9677, -1.2417, 
        -3.9931, -3.2581, -1.6636, -2.1333, -0.2530, 
        0.3517, -2.9001
    ],
    "Longitud": [
        -79.8891, -78.4678, -80.7127, -78.6195, 
        -79.2042, -79.9554, -78.6546, -79.5833, -79.1754, 
        -78.1223, -79.0059
    ],
    "Cobertura (Clientes)": [
        "Pequeños (< 10 unidades)", "Corales - Tiendas", "Manta, Portoviejo, Jipijapa...", 
        "Corales, Latacunga, Salcedo...", "Clientes de Loja, Saraguro", "Pasaje, Huaquillas, Santa Rosa...", 
        "Riobamba, Guano", "El Triunfo, Naranjal, La Troncal...", "Carmen, Pedernales, Esmeraldas...", 
        "Otavalo, Tulcán, Cayambe...", "Azogues, Gualaceo, Santa Isabel..."
    ]
}

df = pd.DataFrame(data)

# Crear dos columnas: una para el mapa y otra para los datos
col1, col2 = st.columns([2, 1])

with col1:
    # Centrar el mapa en Ecuador
    m = folium.Map(location=[-1.8312, -78.1834], zoom_start=6.5)

    # Agregar los marcadores al mapa
    for i, row in df.iterrows():
        # Crear un popup con la información
        popup_html = f"""
        <b>{row['Despacho'].upper()}</b><br>
        <b>Transporte:</b> {row['Transporte']}<br>
        <b>Contacto:</b> {row['Contacto']} ({row['Teléfono']})<br>
        <b>Cobertura:</b> {row['Cobertura (Clientes)']}
        """
        
        # Dibujar un círculo rojo
        folium.CircleMarker(
            location=[row['Latitud'], row['Longitud']],
            radius=8,
            popup=folium.Popup(popup_html, max_width=300),
            color='red',
            fill=True,
            fill_color='red',
            fill_opacity=0.7,
            tooltip=row['Despacho']
        ).add_to(m)

    # Mostrar el mapa en Streamlit
    st_folium(m, width=800, height=600)

with col2:
    st.subheader("📋 Directorio de Transportistas")
    # Mostrar la tabla resumida a un lado del mapa
    st.dataframe(df[['Despacho', 'Transporte', 'Contacto', 'Teléfono']], hide_index=True)

st.markdown("---")
st.markdown("💡 *Haz clic en los círculos rojos del mapa para ver los detalles de contacto, transportista y la cobertura específica de cada sector.*")

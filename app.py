import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Configuración inicial
st.set_page_config(page_title="Gestión de Despachos Ecuador", layout="wide")

# Estilo personalizado para mejorar la visibilidad (similar a tu captura)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stSelectbox, .stTextInput { color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚛 Sistema de Despachos y Cobertura Nacional")

# Base de datos completa basada en tus imágenes
data = [
    {"Despacho": "BODEGA GUAYAQUIL", "Clientes": "PEQUEÑOS (MENOR A 10 UNIDADES)", "Transporte": "TRAINHCO", "Contacto": "FERNANDO AUCAPIÑA", "Teléfono": "0958921894", "Lat": -2.1894, "Lon": -79.8891},
    {"Despacho": "BODEGA QUITO", "Clientes": "CORALES - TIENDAS", "Transporte": "IZCONT", "Contacto": "MAGALY IZQUIERDO", "Teléfono": "0992185765", "Lat": -0.1807, "Lon": -78.4678},
    {"Despacho": "BODEGA MANTA", "Clientes": "MANTA - PORTOVIEJO - MONTECRISTI - SUCRE - JIPIJAPA - SAN VICENTE - ROCAFUERTE - CHARAPOTO - JUNIN", "Transporte": "AUSTROVELO", "Contacto": "DAVID AVILA", "Teléfono": "0969351070", "Lat": -0.9677, "Lon": -80.7127},
    {"Despacho": "BODEGA AMBATO", "Clientes": "CORALES - TIENDAS - LATACUNGA - SALCEDO - PILLARO - PUJILI - CEVALLOS - PELILEO - BAÑOS DE AGUA SANTA", "Transporte": "PIONEROS", "Contacto": "ARTURO AREQUIPA", "Teléfono": "0983246371", "Lat": -1.2417, "Lon": -78.6195},
    {"Despacho": "LOJA", "Clientes": "CLIENTES DE LOJA - SARAGURO", "Transporte": "GAVIOTAS", "Contacto": "LUIS TAPIA", "Teléfono": "0991449793", "Lat": -3.9931, "Lon": -79.2042},
    {"Despacho": "PROVINCIA DE LOJA", "Clientes": "CATAMAYO - CALVAS - MACARA - ZAPOTILLO - PINDAL - ALAMOR - CELICA - PUYANGO", "Transporte": "YIRETRANS", "Contacto": "MARIO ATOCHA", "Teléfono": "0983449493", "Lat": -4.0000, "Lon": -79.5000},
    {"Despacho": "ORIENTE SUR", "Clientes": "ZAMORA - YANZATZA - GUALAQUISA - PANGUI - SANTIAGO DE MENDES - MACAS - SUCUA - PALORA - PABLO SEXTO", "Transporte": "UNIDOS", "Contacto": "ELENA ORTIZ", "Teléfono": "0989395188", "Lat": -4.0692, "Lon": -78.9567},
    {"Despacho": "ORIENTE NORTE", "Clientes": "PAZTAZA - PUYO - TENA - ORELLANA - SUCUMBIOS - LOS SACHAS - SHUSHUFINDI - LORETO - NUEVA LOJA - EL COCA", "Transporte": "EFICIENTRUCKS", "Contacto": "CARLOS PICON", "Teléfono": "0939528627", "Lat": -0.4594, "Lon": -76.9871},
    {"Despacho": "MACHALA", "Clientes": "MACHALA - PASAJE - HUAQUILLAS - ARENILLAS - STA ROSA - EL GUABO - CAMILO PONCE - ZARUMA - PORTOVELO - PIÑAS", "Transporte": "GAVIOTAS", "Contacto": "LUIS TAPIA", "Teléfono": "0991449793", "Lat": -3.2581, "Lon": -79.9554},
    {"Despacho": "RIOBAMBA", "Clientes": "RIOBAMBA - GUANO", "Transporte": "BENZOR", "Contacto": "MILTON VASCONEZ", "Teléfono": "0999400262", "Lat": -1.6636, "Lon": -78.6546},
    {"Despacho": "MILAGRO", "Clientes": "MILAGRO - EL TRIUNFO - SIMON BOLIVAR - NARANJAL - LA TRONCAL - NARANJITO - BUCAY - GRL ANTONIO ELIZALDE", "Transporte": "FLOTA CAÑARI", "Contacto": "ANTONIO ENCALADA", "Teléfono": "0999556788", "Lat": -2.1333, "Lon": -79.5833},
    {"Despacho": "LOS RIOS ZONA ALTA", "Clientes": "LA MANA - VALENCIA - QUEVEDO - BUENA FE - EL EMPALME - PICHINCHA - MOCACHE - VENTANAS - URDANETA - ECHEANDIA - QUINSALOMA", "Transporte": "PESADA MENDEZ", "Contacto": "NELSON CHIMBORAZO", "Teléfono": "0993176359", "Lat": -1.0225, "Lon": -79.4600},
    {"Despacho": "LOS RIOS ZONA BAJA", "Clientes": "MONTALVO - BABAHOYO - PUEBLO VIEJO - BABA - VINCES - SAN JUAN - CALUMA - MATA DE CACAO", "Transporte": "PESADA MENDEZ", "Contacto": "NELSON CHIMBORAZO", "Teléfono": "0993176359", "Lat": -1.8022, "Lon": -79.5344},
    {"Despacho": "BODEGA STO DOMINGO", "Clientes": "STO DOMINGO - CARMEN - PEDERNALES - SAN LORENZO - ESMERALDAS - QUININDE - RIO VERDE - ATACAMES", "Transporte": "MANUEL ORTIZ", "Contacto": "MANUEL ORTIZ", "Teléfono": "0993722448", "Lat": -0.2530, "Lon": -79.1754},
    {"Despacho": "IBARRA", "Clientes": "OTAVALO - TULCAN - IBARRA - CAYAMBE - QUINCHE", "Transporte": "XLM E HIJOS", "Contacto": "JAVIER PEREZ", "Teléfono": "0996129736", "Lat": 0.3517, "Lon": -78.1223},
    {"Despacho": "CLIENTES CUENCA", "Clientes": "CUENCA - AZOGUES - CAÑAR - GUALACEO - SIGSIG", "Transporte": "TRANSPORTE EMPRESA", "Contacto": "ANDRES VARGAS", "Teléfono": "0987935222", "Lat": -2.9001, "Lon": -79.0059}
]

df = pd.DataFrame(data)

# --- SIDEBAR: BUSCADOR Y LISTA ---
st.sidebar.header("⚙️ Opciones de Filtro")

# Buscador de texto automático
busqueda = st.sidebar.text_input("🔍 Buscar Ciudad o Cliente:", "").strip().upper()

# Lista desplegable
nombres_despacho = ["TODOS"] + sorted(df["Despacho"].unique().tolist())
seleccion_lista = st.sidebar.selectbox("Seleccione el punto de Despacho:", nombres_despacho)

# Lógica de filtrado combinada
if busqueda:
    # Filtra si el texto está en el nombre del Despacho O en la lista de Clientes
    df_filtrado = df[df["Despacho"].str.contains(busqueda) | df["Clientes"].str.contains(busqueda)]
else:
    if seleccion_lista == "TODOS":
        df_filtrado = df
    else:
        df_filtrado = df[df["Despacho"] == seleccion_lista]

# --- VISUALIZACIÓN ---
col_map, col_info = st.columns([2, 1])

with col_map:
    # Determinar centro del mapa
    if len(df_filtrado) == 1:
        centro = [df_filtrado["Lat"].iloc[0], df_filtrado["Lon"].iloc[0]]
        zoom = 10
    else:
        centro = [-1.8312, -78.1834]
        zoom = 7

    m = folium.Map(location=centro, zoom_start=zoom, tiles="CartoDB dark_matter")
    
    for _, r in df_filtrado.iterrows():
        popup_html = f"""
        <div style='color: black;'>
            <b>{r['Despacho']}</b><br>
            <b>Transporte:</b> {r['Transporte']}<br>
            <b>Contacto:</b> {r['Contacto']}<br>
            <hr>
            <b>Cobertura:</b> {r['Clientes']}
        </div>
        """
        folium.CircleMarker(
            location=[r['Lat'], r['Lon']],
            radius=10, color='red', fill=True, fill_color='red', fill_opacity=0.8,
            popup=folium.Popup(popup_html, max_width=300)
        ).add_to(m)
    
    st_folium(m, width="100%", height=500)

with col_info:
    if len(df_filtrado) == 1:
        row = df_filtrado.iloc[0]
        st.success(f"📍 Punto: {row['Despacho']}")
        st.write(f"**Transportista:** {row['Transporte']}")
        st.write(f"**Contacto:** {row['Contacto']}")
        st.write(f"**Teléfono:** {row['Teléfono']}")
        st.warning(f"**Cobertura:** {row['Clientes']}")
    elif len(df_filtrado) > 1:
        st.info(f"Se encontraron {len(df_filtrado)} resultados. Selecciona uno para ver detalles.")
    else:
        st.error("No se encontraron resultados para tu búsqueda.")

# Tabla inferior
st.dataframe(df_filtrado[["Despacho", "Transporte", "Contacto", "Teléfono"]], hide_index=True, use_container_width=True)

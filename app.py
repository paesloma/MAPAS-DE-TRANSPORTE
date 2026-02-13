import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Gestión de Despachos Ecuador", layout="wide")

st.title("🚛 Sistema de Despachos y Cobertura Nacional")

# Base de datos completa basada en las imágenes proporcionadas
data = [
    {"Despacho": "BODEGA GUAYAQUIL", "Clientes": "PEQUEÑOS (MENOR A 10 UNIDADES)", "Transporte": "TRAINHCO", "Contacto": "FERNANDO AUCAPIÑA", "Teléfono": "0958921894", "Lat": -2.1894, "Lon": -79.8891},
    {"Despacho": "CLIENTES GYE COMPLETO", "Clientes": "GUAYAQUIL COMPLETO", "Transporte": "IZCONT", "Contacto": "MAGALY IZQUIERDO", "Teléfono": "0992185765", "Lat": -2.1700, "Lon": -79.9200},
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
    {"Despacho": "CANTONES CUENCA (AZOGUES)", "Clientes": "AZOGUES - CAÑAR - TAMBO - BIBLIAN - DELEG", "Transporte": "TRANSPORTE EMPRESA", "Contacto": "PEDRO DAVILA", "Teléfono": "0998527171", "Lat": -2.7397, "Lon": -78.8486},
    {"Despacho": "CANTONES CUENCA (GUALACEO)", "Clientes": "GUALACEO - CHORDELEG - SIGSIG - PAUTE", "Transporte": "TRANSPORTE EMPRESA", "Contacto": "PEDRO DAVILA", "Teléfono": "0998527171", "Lat": -2.8914, "Lon": -78.7758},
    {"Despacho": "CANTONES CUENCA (STA ISABEL)", "Clientes": "STA ISABEL - JIRON - SAN FERNANDO", "Transporte": "TRANSPORTE EMPRESA", "Contacto": "PEDRO DAVILA", "Teléfono": "0998527171", "Lat": -3.2736, "Lon": -79.3142},
    {"Despacho": "CLIENTES CUENCA", "Clientes": "CUENCA", "Transporte": "TRANSPORTE EMPRESA", "Contacto": "ANDRES VARGAS", "Teléfono": "0987935222", "Lat": -2.9001, "Lon": -79.0059}
]

df = pd.DataFrame(data)

# Sidebar para selección descartable
st.sidebar.header("⚙️ Opciones de Filtro")
seleccion = st.sidebar.selectbox(
    "Seleccione el punto de Despacho:",
    options=["TODOS"] + sorted(df["Despacho"].unique().tolist())
)

# Filtrar DataFrame según selección
if seleccion != "TODOS":
    df_display = df[df["Despacho"] == seleccion]
    centro_lat = df_display["Lat"].iloc[0]
    centro_lon = df_display["Lon"].iloc[0]
    zoom = 10
else:
    df_display = df
    centro_lat = -1.8312
    centro_lon = -78.1834
    zoom = 7

# Layout
col_map, col_info = st.columns([2, 1])

with col_map:
    m = folium.Map(location=[centro_lat, centro_lon], zoom_start=zoom)
    
    for _, r in df_display.iterrows():
        popup_content = f"""
        <b>{r['Despacho']}</b><br>
        <b>Transporte:</b> {r['Transporte']}<br>
        <b>Contacto:</b> {r['Contacto']} ({r['Teléfono']})<br>
        <hr>
        <b>Clientes:</b> {r['Clientes']}
        """
        folium.CircleMarker(
            location=[r['Lat'], r['Lon']],
            radius=10,
            color='red',
            fill=True,
            fill_color='red',
            fill_opacity=0.7,
            popup=folium.Popup(popup_content, max_width=300)
        ).add_to(m)
    
    st_folium(m, width="100%", height=500)

with col_info:
    st.subheader("📋 Datos del Despacho")
    if seleccion == "TODOS":
        st.write("Selecciona una ciudad en el menú de la izquierda para ver el detalle.")
    else:
        st.info(f"**Punto:** {df_display['Despacho'].iloc[0]}")
        st.write(f"**Transportista:** {df_display['Transporte'].iloc[0]}")
        st.write(f"**Contacto:** {df_display['Contacto'].iloc[0]}")
        st.write(f"**Teléfono:** {df_display['Teléfono'].iloc[0]}")
        st.warning(f"**Cobertura:** {df_display['Clientes'].iloc[0]}")

st.dataframe(df_display[["Despacho", "Transporte", "Contacto", "Teléfono"]], hide_index=True)

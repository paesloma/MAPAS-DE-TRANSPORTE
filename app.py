import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Configuración de la página
st.set_page_config(page_title="Mapa Interactivo de Despachos", layout="wide")
st.title("📍 Mapa de Cobertura y Despachos - Interactivo")
st.markdown("Selecciona una ruta para ver los detalles completos del transporte y la zona de cobertura en el mapa.")

# Base de datos completa extraída de los registros
data = {
    "Ruta / Despacho": [
        "Bodega Guayaquil", "Clientes GYE Completo (Izcont)", "Clientes GYE Completo (Pioneros)",
        "Bodega Quito", "Bodega Manta", "Bodega Ambato", "Loja", "Provincia de Loja",
        "Oriente Sur", "Oriente Sur Centro", "Oriente Norte", "Machala", "Riobamba",
        "Milagro", "Los Rios Zona Alta", "Los Rios Zona Baja", "Bodega Sto Domingo",
        "Ibarra", "Cantones Cuenca (Freddy Samartin)", "Cantones Cuenca (Agustin Carpio)",
        "Cantones Cuenca (Jhon Rivera)", "Clientes Cuenca"
    ],
    "Transporte": [
        "TRAINHCO", "IZCONT", "PIONEROS", "IZCONT", "AUSTROVELO", "PIONEROS",
        "GAVIOTAS", "YIRETRANS", "UNIDOS", "AUSTROVELO", "EFICIENTRUCKS",
        "GAVIOTAS", "BENZOR", "FLOTA CAÑARI", "PESADA MENDEZ", "PESADA MENDEZ",
        "MANUEL ORTIZ", "XLM E HIJOS", "TRANSPORTE EMPRESA", "TRANSPORTE EMPRESA",
        "TRANSPORTE EMPRESA", "TRANSPORTE EMPRESA"
    ],
    "Contacto": [
        "Fernando Aucapiña", "Magaly Izquierdo", "Celso Duchitanga", "Magaly Izquierdo",
        "David Avila", "Arturo Arequipa", "Luis Tapia", "Mario Atocha", "Elena Ortiz",
        "Miguel Montoya", "Carlos Picon", "Luis Tapia", "Milton Vasconez",
        "Antonio Encalada", "Nelson Chimborazo", "Nelson Chimborazo", "Manuel Ortiz",
        "Javier Perez", "Pedro Davila (Jefe Logística)", "Pedro Davila (Jefe Logística)",
        "Pedro Davila (Jefe Logística)", "Andres Vargas"
    ],
    "Teléfono": [
        "0958921894", "0992185765", "0993570326", "0992185765", "0969351070", "0983246371",
        "0991449793", "0983449493", "0989395188", "0988535857", "0939528627", "0991449793",
        "0999400262", "0999556788", "0993176359", "0993176359", "0993722448", "0996129736",
        "0998527171", "0998527171", "0998527171", "0987935222"
    ],
    "Cobertura (Clientes / Zonas)": [
        "Pequeños (Menor a 10 unidades)", "Clientes GYE Completo", "Clientes GYE Completo",
        "Corales - Tiendas", "Manta - Portoviejo - Montecristi -

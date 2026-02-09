import streamlit as st
from views.categories import render_categories_view
from views.players import render_players_view
from views.dashboard import render_dashboard_view

# Configuración de la página
st.set_page_config(
    page_title="Minions FC Manager",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar (Menú Lateral)
st.sidebar.title("Minions FC ⚽")
st.sidebar.markdown("---")
opcion = st.sidebar.radio(
    "Navegación", 
    ["Categorías", "Registro Jugadores", "Ver Plantillas"]
)

st.sidebar.markdown("---")
st.sidebar.caption("v1.0 - Sistema de Gestión")

# Router de Vistas
if opcion == "Categorías":
    render_categories_view()
elif opcion == "Registro Jugadores":
    render_players_view()
elif opcion == "Ver Plantillas":
    render_dashboard_view()
import streamlit as st
import pandas as pd
from utils.api import ApiClient

def render_dashboard_view():
    st.header("📋 Visualizar Plantillas")

    # 1. Obtener Categorías
    cats_data = ApiClient.get("/categorias/")
    
    if not cats_data or (isinstance(cats_data, dict) and "error" in cats_data):
        st.info("No hay categorías disponibles para filtrar.")
        return

    opciones_cat = {f"{c['nombre']} ({c['alias']})": c["_id"] for c in cats_data}

    # Filtro
    col1, _ = st.columns([1, 2])
    with col1:
        cat_seleccionada = st.selectbox("Selecciona Categoría:", list(opciones_cat.keys()))
    
    if cat_seleccionada:
        cat_id = opciones_cat[cat_seleccionada]
        
        # Botón de recarga manual (opcional, pero útil)
        if st.button("🔄 Actualizar Lista"):
            st.rerun()

        # Obtener Jugadores
        jugadores = ApiClient.get(f"/jugadores/{cat_id}")
        
        if isinstance(jugadores, list) and jugadores:
            # Procesar datos para la tabla
            data = []
            for j in jugadores:
                data.append({
                    "Dorsal": j["numero_playera"],
                    "Nombre": j["nombre_completo"],
                    "Posiciones": ", ".join(j["posiciones"]),
                    "Nacimiento": j["fecha_nacimiento"]
                })
            
            df = pd.DataFrame(data)
            st.table(df)
            
            st.metric("Total Jugadores", len(jugadores))
        elif isinstance(jugadores, list) and not jugadores:
            st.info(f"La categoría {cat_seleccionada} aún no tiene jugadores registrados.")
        else:
            st.error(f"Error al cargar jugadores: {jugadores.get('error')}")
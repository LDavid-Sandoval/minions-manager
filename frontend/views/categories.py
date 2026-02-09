import streamlit as st
import pandas as pd
from utils.api import ApiClient

def render_categories_view():
    st.header("📂 Gestión de Categorías")
    st.markdown("Define las categorías de la temporada para validar las edades automáticamente.")

    # --- FORMULARIO DE CREACIÓN ---
    with st.expander("➕ Nueva Categoría", expanded=True):
        with st.form("form_cat"):
            c1, c2 = st.columns(2)
            nombre = c1.text_input("Nombre (Ej: Baby)", placeholder="Sub-15, Baby, etc.")
            alias = c2.text_input("Alias (Ej: 2012-2013)", placeholder="Generación X")
            
            c3, c4 = st.columns(2)
            anio_min = c3.number_input("Año Nacimiento Mínimo", min_value=2000, max_value=2030, value=2012)
            anio_max = c4.number_input("Año Nacimiento Máximo", min_value=2000, max_value=2030, value=2013)
            
            submitted = st.form_submit_button("Guardar Categoría")
            
            if submitted:
                if not nombre or not alias:
                    st.error("El nombre y el alias son obligatorios.")
                else:
                    payload = {
                        "nombre": nombre, "alias": alias,
                        "anio_min": int(anio_min), "anio_max": int(anio_max)
                    }
                    res = ApiClient.post("/categorias/", payload)
                    
                    if "error" in res:
                        st.error(f"❌ Error: {res['error']}")
                    else:
                        st.success(f"✅ Categoría '{nombre}' creada exitosamente.")
                        st.rerun() # Recargar para verla en la tabla

    # --- TABLA DE CATEGORÍAS EXISTENTES ---
    st.divider()
    st.subheader("Categorías Activas")
    
    cats = ApiClient.get("/categorias/")
    
    if isinstance(cats, list) and cats:
        df = pd.DataFrame(cats)
        # Seleccionamos y renombramos columnas para que se vea bonito
        if not df.empty:
            st.dataframe(
                df[["nombre", "alias", "anio_min", "anio_max"]].rename(columns={
                    "nombre": "Categoría", "alias": "Generación", 
                    "anio_min": "Año Min", "anio_max": "Año Max"
                }),
                use_container_width=True
            )
    elif "error" in cats:
        st.error(f"Error de conexión: {cats['error']}")
    else:
        st.info("No hay categorías registradas aún.")
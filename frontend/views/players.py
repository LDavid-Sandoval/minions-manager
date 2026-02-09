import streamlit as st
from datetime import date
from utils.api import ApiClient

def render_players_view():
    st.header("busts_in_silhouette: Registro de Jugadores")
    
    # 1. Cargar Categorías para el SelectBox
    cats_data = ApiClient.get("/categorias/")
    
    # Validar si hubo error o si la lista está vacía
    if isinstance(cats_data, dict) and "error" in cats_data:
        st.error(f"No se pudo conectar al backend: {cats_data['error']}")
        return
    
    if not cats_data:
        st.warning("⚠️ Primero debes crear una categoría en la pestaña 'Categorías'.")
        return

    # Crear diccionario para el select: "Nombre (Alias)" -> ID
    opciones_cat = {f"{c['nombre']} ({c['alias']})": c["_id"] for c in cats_data}

    # --- FORMULARIO ---
    with st.form("form_jugador", clear_on_submit=True):
        st.subheader("Datos del Jugador")
        
        c_cat, c_nombre = st.columns(2)
        cat_nombre = c_cat.selectbox("Selecciona Categoría", list(opciones_cat.keys()))
        nombre = c_nombre.text_input("Nombre Completo")
        
        c_fecha, c_num = st.columns(2)
        fecha_nac = c_fecha.date_input("Fecha de Nacimiento", min_value=date(2005, 1, 1), max_value=date.today())
        numero = c_num.number_input("Número de Playera", min_value=0, max_value=99, step=1)
        
        posiciones = st.multiselect(
            "Posición(es)", 
            ["Portero", "Defensa Central", "Lateral", "Medio Contención", "Medio Creativo", "Extremo", "Delantero"]
        )
        
        submitted = st.form_submit_button("Registrar Jugador")
        
        if submitted:
            if not nombre:
                st.error("El nombre es obligatorio.")
            elif not posiciones:
                st.error("Selecciona al menos una posición.")
            else:
                payload = {
                    "nombre_completo": nombre,
                    "fecha_nacimiento": str(fecha_nac),
                    "numero_playera": numero,
                    "posiciones": posiciones,
                    "categoria_id": opciones_cat[cat_nombre]
                }
                
                # Enviar al backend
                res = ApiClient.post("/jugadores/", payload)
                
                if "error" in res:
                    st.error(f"❌ {res['error']}")
                else:
                    st.success(f"✅ Jugador registrado correctamente en {cat_nombre}")
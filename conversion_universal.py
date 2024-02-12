import streamlit as st

# Título de la app
st.title("Conversor universal")

# Selección de categoría
categoria = st.selectbox("Selecciona una categoría:", [
    "Conversiones de temperatura",
    "Conversiones de longitud",
    "Conversiones de peso/masa",
    "Conversiones de volumen",
    "Conversiones de tiempo",
    "Conversiones de velocidad",
    "Conversiones de área",
    "Conversiones de energía",
    "Conversiones de presión",
    "Conversiones de tamaño de datos"
])

# Conversiones disponibles para cada categoría
conversiones = {
    "Conversiones de temperatura": ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"],
    "Conversiones de longitud": ["Pies a metros", "Metros a pies", "Pulgadas a centímetros", "Centímetros a pulgadas"],
    "Conversiones de peso/masa": ["Libras a kilogramos", "Kilogramos a libras", "Onzas a gramos", "Gramos a onzas"],
    "Conversiones de volumen": ["Galones a litros", "Litros a galones", "Pulgadas cúbicas a centímetros cúbicos", "Centímetros cúbicos a pulgadas cúbicas"],
    "Conversiones de tiempo": ["Horas a minutos", "Minutos a segundos", "Días a horas", "Semanas a días"],
    "Conversiones de velocidad": ["Millas por hora a kilómetros por hora", "Kilómetros por hora a metros por segundo", "Nudos a millas por hora", "Metros por segundo a pies por segundo"],
    "Conversiones de área": ["Metros cuadrados a pies cuadrados", "Pies cuadrados a metros cuadrados", "Kilómetros cuadrados a millas cuadradas", "Millas cuadradas a kilómetros cuadrados"],
    "Conversiones de energía": ["Julios a calorías", "Calorías a kilojulios", "Kilovatios-hora a megajulios", "Megajulios a kilovatios-hora"],
    "Conversiones de presión": ["Pascales a atmósferas", "Atmósferas a pascales", "Barras a libras por pulgada cuadrada", "Libras por pulgada cuadrada a bares"],
    "Conversiones de tamaño de datos": ["Megabytes a gigabytes", "Gigabytes a Terabytes", "Kilobytes a megabytes", "Terabytes a petabytes"]
}

# Selección de conversión dentro de la categoría
if categoria:
    conversion_seleccionada = st.selectbox(f"Selecciona una conversión de {categoria}:", conversiones[categoria])
    st.write(f"Has seleccionado: {conversion_seleccionada}")

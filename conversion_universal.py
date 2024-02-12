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
    "Conversiones de temperatura": {
        "Celsius a Fahrenheit": lambda celsius: celsius * 9/5 + 32,
        "Fahrenheit a Celsius": lambda fahrenheit: (fahrenheit - 32) * 5/9,
        "Celsius a Kelvin": lambda celsius: celsius + 273.15,
        "Kelvin a Celsius": lambda kelvin: kelvin - 273.15
    },
    "Conversiones de longitud": {
        "Pies a metros": lambda pies: pies * 0.3048,
        "Metros a pies": lambda metros: metros / 0.3048,
        "Pulgadas a centímetros": lambda pulgadas: pulgadas * 2.54,
        "Centímetros a pulgadas": lambda centimetros: centimetros / 2.54
    },
    "Conversiones de peso/masa": {
        "Libras a kilogramos": lambda libras: libras * 0.453592,
        "Kilogramos a libras": lambda kilogramos: kilogramos / 0.453592,
        "Onzas a gramos": lambda onzas: onzas * 28.3495,
        "Gramos a onzas": lambda gramos: gramos / 28.3495
    },
    "Conversiones de volumen": {
        "Galones a litros": lambda galones: galones * 3.78541,
        "Litros a galones": lambda litros: litros / 3.78541,
        "Pulgadas cúbicas a centímetros cúbicos": lambda pulgadas_cubicas: pulgadas_cubicas * 16.3871,
        "Centímetros cúbicos a pulgadas cúbicas": lambda centimetros_cubicos: centimetros_cubicos / 16.3871
    },
    "Conversiones de tiempo": {
        "Horas a minutos": lambda horas: horas * 60,
        "Minutos a segundos": lambda minutos: minutos * 60,
        "Días a horas": lambda dias: dias * 24,
        "Semanas a días": lambda semanas: semanas * 7
    },
    "Conversiones de velocidad": {
        "Millas por hora a kilómetros por hora": lambda mph: mph * 1.60934,
        "Kilómetros por hora a metros por segundo": lambda kph: kph / 3.6,
        "Nudos a millas por hora": lambda knots: knots * 1.15078,
        "Metros por segundo a pies por segundo": lambda mps: mps * 3.28084
    },
    "Conversiones de área": {
        "Metros cuadrados a pies cuadrados": lambda metros_cuadrados: metros_cuadrados * 10.7639,
        "Pies cuadrados a metros cuadrados": lambda pies_cuadrados: pies_cuadrados / 10.7639,
        "Kilómetros cuadrados a millas cuadradas": lambda km_cuadrados: km_cuadrados * 0.386102,
        "Millas cuadradas a kilómetros cuadrados": lambda millas_cuadradas: millas_cuadradas / 0.386102
    },
    "Conversiones de energía": {
        "Julios a calorías": lambda julios: julios * 0.239006,
        "Calorías a kilojulios": lambda calorias: calorias * 0.001,
        "Kilovatios-hora a megajulios": lambda kwh: kwh * 3.6,
        "Megajulios a kilovatios-hora": lambda mj: mj / 3.6
    },
    "Conversiones de presión": {
        "Pascales a atmósferas": lambda pascales: pascales * 0.00000986923,
        "Atmósferas a pascales": lambda atm: atm / 0.00000986923,
        "Barras a libras por pulgada cuadrada": lambda bars: bars * 14.5038,
        "Libras por pulgada cuadrada a bares": lambda psi: psi / 14.5038
    },
    "Conversiones de tamaño de datos": {
        "Megabytes a gigabytes": lambda mb: mb * 0.001,
        "Gigabytes a Terabytes": lambda gb: gb * 0.001,
        "Kilobytes a megabytes": lambda kb: kb * 0.001,
        "Terabytes a petabytes": lambda tb: tb * 0.001
    }
}

# Selección de conversión dentro de la categoría
if categoria:
    conversion_seleccionada = st.selectbox(f"Selecciona una conversión de {categoria}:", list(conversiones[categoria].keys()))
    valor_a_convertir = st.number_input(f"Ingrese el valor a convertir de {conversion_seleccionada.split(' a ')[0]}")
    if valor_a_convertir:
        resultado = conversiones[categoria][conversion_seleccionada](valor_a_convertir)
        st.write(f"El resultado de la conversión es: {resultado}")

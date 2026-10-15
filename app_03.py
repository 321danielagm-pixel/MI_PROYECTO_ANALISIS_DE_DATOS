import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# cargamos el excel deoases vs. Yardas.
df = pd.read_excel('YARDAS_PASOS_DATOS_TICS.xlsx', index_col=0)

# visualizar los primeros 5 datos de mi base de datos.
st.dataframe(df.head())

# Estadística descriptiva
st.header ("Estadística descriptiva")
st.dataframe (df.describe())

#esto sirve para renombrar las columnas de mi data
df.columns= [c.lower().replace(' ', '_') for c in df.columns]

col1, col2 = st.columns(2)

with col1:
    # esto es una gráfica de caja y bigote.
    #de los pases completos.
    fig, ax = plt.subplots ()
    ax.boxplot(df['pases_completos'])
    st.header("Diagrama de caja y bigote\n de pases completos")
    st.pyplot(fig)

with col2:
    # esto es una gráfica de caja y bigote.
    #de las yardas completos.
    fig, ax = plt.subplots ()
    ax.boxplot(df['yardas_totales'])
    st.header("Diagrama de caja y bigote\n de yardas totales")
    st.pyplot(fig)
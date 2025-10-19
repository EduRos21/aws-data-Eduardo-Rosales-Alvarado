import pandas as pd
import boto3
import io
import os
import streamlit as st
import plotly.express as px
import streamlit as st
import plotly.express as px 
import matplotlib.pyplot as plt

st.set_page_config(page_title="ProjectX Dashboard", layout="wide")

@st.cache_data
def load_data():
    
    s3 = boto3.client("s3")

    load_dotenv()
    bucket = os.getenv("BUCKET_NAME")
    key = os.getenv("SOURCE_DATA")
    res = s3.get_object(Bucket=bucket, Key=key)
    csv_content = res['Body'].read()
    
    return pd.read_csv(io.BytesIO(csv_content))

df = load_data()


st.title("Project X Dashboard")




# KPI 
total = len(df)
total_years = df["año"].nunique()
total_births = df["total"].sum()


col1, col2, col3 = st.columns(3)
col1.metric("Total de registros analizados", total)
col2.metric("Años", total_years)
col3.metric("Total de nacimientos", total_births)


col1, col2 = st.columns(2)
 
with col1:
    df_top_5_registros = df.nlargest(5, 'total')


    df_top_5_registros['etiqueta_x'] = (
        df_top_5_registros['estado'] + " - " + 
        df_top_5_registros['año'].astype(str) + 
        " (" + df_top_5_registros['total'].astype(str) + ")"
    )
    
    # 3. Crear la gráfica de barras
    fig = px.bar(
        df_top_5_registros,
        x='etiqueta_x',      # Eje X: Etiqueta única (Estado - Año (Total))
        y='total',           # Eje Y: Total de nacimientos
        color='estado',      # Colorear por Estado para diferenciar
        title='Top 5 estados con mayor total de nacimientos',
        labels={'etiqueta_x': 'Registro (Estado, Año, Total)', 'total': 'Total de Nacimientos'},
        height=600,
        text='total' # Opcional: Muestra el valor exacto encima de cada barra
    )
    
    # 4. Mejorar el diseño
    fig.update_traces(textposition='outside') # Coloca el texto fuera de la barra
    fig.update_xaxes(tickangle=45, tickfont=dict(size=10)) # Rota y reduce la fuente para mejor legibilidad
    
    # 5. Mostrar la gráfica en Streamlit
    st.plotly_chart(fig, use_container_width=True)
    
with col2:

    st.subheader("Distribución de Nacimientos por Sexo")

    # 1. Sumar los totales de cada categoría en todo el DataFrame
    total_hombres = df['hombres'].sum()
    total_mujeres = df['mujeres'].sum()
    total_no_especificado = df['no_especificado'].sum()
    
    # 2. Crear un DataFrame pequeño para la gráfica de pastel
    # Es útil para Plotly Express, aunque también se podría usar directamente con listas
    data_pie = pd.DataFrame({
        'Categoría': ['Hombres', 'Mujeres', 'No Especificado'],
        'Total': [total_hombres, total_mujeres, total_no_especificado]
    })
    
    # 3. Crear la gráfica de pastel
    fig_pie = px.pie(
        data_pie,
        values='Total',          # Los valores que determinan el tamaño de los "slices"
        names='Categoría',       # Las etiquetas de cada "slice"
        title='Nacimientos por Sexo (Total Acumulado en Todos los Años)',
        height=500,
        # Opcional: Personalizar el texto que aparece en la gráfica (porcentaje y valor)
        hover_data=['Total'],
        labels={'Total': 'Cantidad de Nacimientos'}
    )
    
    # Opcional: Mostrar los porcentajes y valores en la gráfica
    fig_pie.update_traces(textposition='inside', textinfo='percent+value')
    
    # 4. Mostrar la gráfica en Streamlit
    st.plotly_chart(fig_pie, use_container_width=True)
    
    #fig2 = px.pie(filtered_df, names="Type1", title="distribution")
    #st.plotly_chart(fig2, use_container_width=True)
    

st.subheader("Nacimientos en México")
st.dataframe(df.head(),  use_container_width=True)
st.caption("Datos obtenidos desde S3 (bucket: xideralaws-curso-bucket-eduardo)")

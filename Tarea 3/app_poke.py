import pandas as pd
import streamlit as st
import plotly.express as px
import pandas as pd 
import streamlit as st
import plotly.express as px 
import matplotlib.pyplot as plt

st.set_page_config(page_title="Pokémon Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("pokemon_data_pokeapi.csv")

df = load_data()


st.title("Pokémon Dashboard")
 
st.sidebar.header("Filtros")
type_filter = st.sidebar.multiselect("Tipo", options=df['Type1'].unique(), default=df['Type1'].unique())
generation_filter = st.sidebar.multiselect("Generación", options=df['Generation'].unique(), default=df['Generation'].unique())
 
filtered_df = df[(df['Type1'].isin(type_filter)) & (df['Generation'].isin(generation_filter))]
 
 
# KPI 
total_pokemon = len(df)
total_generation = df["Generation"].nunique()
is_legendary_pokemon = df["Legendary Status"].value_counts()
count_lp = is_legendary_pokemon["Yes"]

col1, col2, col3 = st.columns(3)
col1.metric("Total de Pokémon", total_pokemon)
col2.metric("Generaciones", total_generation)
col3.metric("Pokémon legendarios", count_lp)
 
 
col1, col2 = st.columns(2)
 
with col1:
    generation_count = df["Generation"].value_counts()
    plt.figure(figsize=(6,4))
    fig1 = px.bar(
        generation_count,
        #color_discrete_map={"1":"red", "2":"yellow", "3":"green", "4": "blue", "5":"black", "6":"white", "7":"orange", "8":"gray"}
    )
    st.plotly_chart(fig1,use_container_width=True)
with col2:
    fig2 = px.pie(filtered_df, names="Type1", title="distribution")
    st.plotly_chart(fig2, use_container_width=True)
 

df["Type2"] = df["Type2"].fillna("Unknown")
st.subheader("Pokémon Generación 1")
st.dataframe(df.head(151),  use_container_width=True)
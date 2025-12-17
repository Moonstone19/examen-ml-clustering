import streamlit as st
import pandas as pd
import numpy as np

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

st.set_page_config(page_title="Clustering ML", layout="wide")

st.title("Clustering – Facebook Live Sellers (Thailand)")
st.write("Application de clustering avec KMeans")

# Charger les données
df = pd.read_csv("live.csv")

features = [
    "num_reactions",
    "num_comments",
    "num_shares",
    "num_likes"
]

X = df[features]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42)
df["cluster"] = kmeans.fit_predict(X_scaled)

st.subheader("Aperçu des données")
st.dataframe(df.head())

fig, ax = plt.subplots()
ax.scatter(
    df["num_reactions"],
    df["num_likes"],
    c=df["cluster"]
)
ax.set_xlabel("Réactions")
ax.set_ylabel("Likes")

st.pyplot(fig)

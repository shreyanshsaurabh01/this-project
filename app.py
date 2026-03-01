import streamlit as st
import pandas as pd
import plotly.express as px

from simulation import run_simulation
from optimizer import alpha_star

st.set_page_config(page_title="this project", layout="wide")
st.title("this project Dashboard")

with st.sidebar:
    k = st.slider("k", 0.01, 2.0, 0.4)
    sigma = st.slider("sigma", 0.01, 2.0, 0.3)
    gamma = st.slider("gamma", 0.01, 0.95, 0.4)
    w0 = st.number_input("initial wealth", 1.0, 1_000_000.0, 10000.0)
    horizon = st.number_input("time horizon", 0.1, 20.0, 1.0)

result = run_simulation(k=k, sigma=sigma, gamma=gamma, w0=w0, horizon=horizon)
df = pd.DataFrame(result)

st.subheader("Spread Simulation")
st.plotly_chart(px.line(df, x="t", y="x", title="OU Spread"), use_container_width=True)

st.subheader("Wealth Trajectory")
st.plotly_chart(px.line(df, x="t", y="w", title="Wealth"), use_container_width=True)

st.subheader("Summary")
st.dataframe(df.describe().T, use_container_width=True)

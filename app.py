import altair as alt
import pandas as pd
import streamlit as st


df = pd.read_csv("players.csv")

df["distance_per_90"] = (df["distance"] / df["minutes"] * 90)
df["sprints_per_90"] = (df["sprints"] / df["minutes"] * 90)

st.title("Football Performance Dashboard")  
st.dataframe(df)

fastest_player = df.loc[df["max_speed"].idxmax()]
average_distance = df["distance"].mean()
total_sprints = df["sprints"].sum()

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Fastest player", fastest_player["name"])
    st.caption(f"Max speed: {fastest_player['max_speed']} km/h")

with col2:
    st.metric("Average distance", f"{average_distance:.0f} m")

with col3:
    st.metric("Total sprints", int(total_sprints))

with col4:
    st.metric("Average distance per 90 min", f"{df['distance_per_90'].mean():.0f} m")

with col5:
    st.metric("Average sprints per 90 min", f"{df['sprints_per_90'].mean():.1f}")

st.subheader("Speed profiles")
selected_player = st.selectbox(
    "Select player",
    df["name"]
)

st.subheader('Sprint per 90  vs Max Speed')
scatter =  alt.Chart(df).mark_circle(size=120).encode(
    x=alt.X(
        "sprints_per_90:Q",
        title="Sprints per 90 minutes"
    ),
    y=alt.Y(
        "max_speed:Q",
        title="Max Speed (km/h)"
    ),
    tooltip=[
        alt.Tooltip("name:N", title="Player"),
        alt.Tooltip("sprints_per_90:Q", title="Sprints per 90", format=".1f"),
        alt.Tooltip("max_speed:Q", title="Max speed", format=".1f")
    ]
)
st.altair_chart(scatter, use_container_width=True)
correlation = df["sprints_per_90"].corr(df["max_speed"])
st.metric(
    "Correlation: Sprints per 90 vs Max speed",
    f"{correlation:.2f}"
)
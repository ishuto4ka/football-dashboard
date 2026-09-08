import pandas as pd
import streamlit as st
import altair as alt
df = pd.read_csv("players.csv")

st.title("Football Performance Dashboard")

st.dataframe(df)

fastest_player = df.loc[df["max_speed"].idxmax()]
average_distance = df["distance"].mean()
total_sprints = df["sprints"].sum()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
    "Fastest player",
    fastest_player["name"]
)

st.caption(
    f"Max speed: {fastest_player['max_speed']} km/h"
)

with col2:
    st.metric(
        "Average distance",
        f"{average_distance:.0f} m"
    )

with col3:
    st.metric(
        "Total sprints",
        int(total_sprints)
    )
st.subheader("Max speed comparison")



chart = alt.Chart(df).mark_bar().encode(
    x=alt.X("name:N", title="Player"),
    y=alt.Y("max_speed:Q", title="Max speed, km/h"),
    tooltip=["name", "max_speed"]
)

st.altair_chart(chart, use_container_width=True)
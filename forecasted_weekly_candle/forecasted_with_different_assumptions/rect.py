import plotly.graph_objects as go

fig = go.Figure()

# Create scatter trace of text labels
fig.add_trace(go.Scatter(
    x=[1.5, 3],
    y=[2.5, 2.5],
    text=["Rectangle reference to the plot",
          "Rectangle reference to the axes"],
    mode="text",
))

# Set axes properties
fig.update_xaxes(range=[0, 4])
fig.update_yaxes(range=[0, 4])

# Add shapes
fig.add_shape(type="rect",
    xref="x", yref="y",
    x0=2.5, y0=0,
    x1=3.5, y1=2,
    line=dict(
        color="RoyalBlue",
        width=3,
    ),
    fillcolor="LightSkyBlue",
)
fig.add_shape(type="rect",
    xref="paper", yref="paper",
    x0=0.25, y0=0,
    x1=0.5, y1=0.5,
    line=dict(
        color="LightSeaGreen",
        width=3,
    ),
    fillcolor="PaleTurquoise",
)

fig.show()
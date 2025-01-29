import streamlit as st
import plotly.graph_objects as go

# Create a simple line chart
fig = go.Figure(data=go.Scatter(x=[1, 2, 3, 4], y=[10, 15, 7, 10]))
 
# Display the figure with Streamlit
st.plotly_chart(fig)
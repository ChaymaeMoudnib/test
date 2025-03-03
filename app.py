import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("My First Streamlit App")

# Header
st.header("Welcome to Streamlit!")

# Subheader
st.subheader("Let's learn how to build interactive apps.")

# Text
st.write("This is a simple app to demonstrate Streamlit's features.")

# Markdown
st.markdown("### Here's a list of things we'll cover:")
st.markdown("- **Text input**")
st.markdown("- **Sliders**")
st.markdown("- **Buttons**")
st.markdown("- **Charts**")

# Display an image
st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", caption="Streamlit Logo")

# Text input
user_input = st.text_input("Enter some text:", "Hello, Streamlit!")
st.write("You entered:", user_input)

# Number input
number = st.number_input("Enter a number:", min_value=0, max_value=100, value=50)
st.write("You selected:", number)

# Slider
slider_value = st.slider("Select a value:", 0, 100, 50)
st.write("Slider value:", slider_value)

# Button
if st.button("Click Me"):
    st.write("Button clicked!")

# Dropdown
option = st.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.write("You selected:", option)

# Line chart
data = pd.DataFrame({
    "x": np.arange(1, 101),
    "y": np.random.randn(100).cumsum()
})
st.line_chart(data, x="x", y="y")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file:", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Uploaded Data:")
    st.write(data)

# Sidebar
st.sidebar.header("Sidebar Controls")
sidebar_slider = st.sidebar.slider("Sidebar Slider:", 0, 100, 50)
st.sidebar.write("Sidebar Slider Value:", sidebar_slider)
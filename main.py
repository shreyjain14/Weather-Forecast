import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select Number of Forecast Days")
option = st.selectbox("Select Data to View", ("Temperature", "Sky"))

try:
    if place:
        filtered_data = get_data(place, days)
        st.subheader(f"{option} for the next {days} days on {place}")

        if option == "Temperature":
            temps = [dict['main']['temp']/10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temps, labels={'x': 'Date', 'y': 'Temperature (C)'})
            st.plotly_chart(figure)

        if option == "Sky":
            filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]
            images = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png', 'Rain': 'images/rain.png', 'Snow': 'images/snow.png'}
            image_list = [images[data] for data in filtered_data]
            st.image(image_list, width=150)
except KeyError:
    st.subheader('Please Enter a Valid City')

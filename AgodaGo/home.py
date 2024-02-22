import streamlit as st
from dest_map import generate_map
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Agoda Go! 👋")

if "clicked" not in st.session_state:
    st.session_state.clicked = False


def click_button() -> None:
    st.session_state.clicked = True


city: str = st.text_input("Type in a city to continue")
st.button("Go", on_click=click_button)

if st.session_state.clicked:
    map = generate_map(city.lower())
    st_folium(map, width=725)

import streamlit as st
from dest_map import generate_map
from streamlit_folium import st_folium


def click_button() -> None:
    st.session_state.clicked = True


def click_done_button() -> None:
    st.session_state.clicked = True


if "clicked" not in st.session_state:
    st.session_state.clicked = False

st.set_page_config(page_title="Agoda Go", page_icon="👋")

st.write("# Welcome to Agoda Go! 👋")

city: str = st.text_input("Type in a city to continue")
st.button("Go", on_click=click_button)


if st.session_state.clicked:
    map, locations = generate_map(city.lower())
    st_folium(map, width=725)

    st.markdown("# Your mission should you choose to accept it: \n")

    for i, loc in enumerate(locations.keys()):
        st.markdown(f"## {i+1}. {loc}")
        st.button("Done", key=i + 1, on_click=click_done_button())

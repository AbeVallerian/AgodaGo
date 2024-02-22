import streamlit as st
from dest_map import generate_map
from streamlit_folium import st_folium

N_LOCATIONS = 5


def reset_button() -> None:
    st.session_state.clicked = False

    st.session_state.visited1 = False
    st.session_state.visited2 = False
    st.session_state.visited3 = False
    st.session_state.visited4 = False
    st.session_state.visited5 = False


def click_button() -> None:
    st.session_state.clicked = True

    st.session_state.visited1 = False
    st.session_state.visited2 = False
    st.session_state.visited3 = False
    st.session_state.visited4 = False
    st.session_state.visited5 = False


def click_done_button1() -> None:
    st.session_state.visited1 = True


def click_done_button2() -> None:
    st.session_state.visited2 = True


def click_done_button3() -> None:
    st.session_state.visited3 = True


def click_done_button4() -> None:
    st.session_state.visited4 = True


def click_done_button5() -> None:
    st.session_state.visited5 = True


if "clicked" not in st.session_state:
    st.session_state.clicked = False

if "visited1" not in st.session_state:
    st.session_state.visited1 = False
if "visited2" not in st.session_state:
    st.session_state.visited2 = False
if "visited3" not in st.session_state:
    st.session_state.visited3 = False
if "visited4" not in st.session_state:
    st.session_state.visited4 = False
if "visited5" not in st.session_state:
    st.session_state.visited5 = False

if "completed" not in st.session_state:
    st.session_state.completed = False

st.set_page_config(page_title="Agoda Go", page_icon="🔴🟡🟢🟣🔵")

st.write("# Welcome to Agoda Go! 🔴🟡🟢🟣🔵")

city: str = st.text_input("Type in a city to continue")
st.button("Go", on_click=click_button)

if (
    st.session_state.visited1
    and st.session_state.visited2
    and st.session_state.visited3
    and st.session_state.visited4
    and st.session_state.visited5
):
    st.write("Congratulations! You just won $100 Agoda Cash! 🎉")
    st.image("images/complete.png")
    st.button("I want to explore another city", on_click=reset_button)
elif st.session_state.clicked:
    map, locations = generate_map(city.lower(), N_LOCATIONS)
    st_folium(map, width=725)

    st.markdown("# Your mission should you choose to accept it: \n")

    st.markdown(f"## 1. {list(locations.keys())[0]}")
    if not st.session_state.visited1:
        st.button("Done", key=1, on_click=click_done_button1)
    else:
        st.button("Completed", key=1)

    st.markdown(f"## 2. {list(locations.keys())[1]}")
    if not st.session_state.visited2:
        st.button("Done", key=2, on_click=click_done_button2)
    else:
        st.button("Completed", key=2)

    st.markdown(f"## 3. {list(locations.keys())[2]}")
    if not st.session_state.visited3:
        st.button("Done", key=3, on_click=click_done_button3)
    else:
        st.button("Completed", key=3)

    st.markdown(f"## 4. {list(locations.keys())[3]}")
    if not st.session_state.visited4:
        st.button("Done", key=4, on_click=click_done_button4)
    else:
        st.button("Completed", key=4)

    st.markdown(f"## 5. {list(locations.keys())[4]}")
    if not st.session_state.visited5:
        st.button("Done", key=5, on_click=click_done_button5)
    else:
        st.button("Completed", key=5)
else:
    st.image("images/homepage.png")

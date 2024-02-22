import folium
import streamlit as st
from streamlit_folium import st_folium

st.write("""Travel the world with Agoda""")

DESTINATION = {
    "Bangkok": {
        "The Grand Palace": {
            "location": [13.7500, 100.4913],
            "url": "https://gpt-vision-image-bucket.s3.ap-southeast-1.amazonaws.com/dall_e/d7fd6704-a333-4436-a8a4-7ca51d7d35c5",
            "agoda_url": "https://www.agoda.com/activities/detail?activityId=1126288&cityId=9395&ds=gLSAa1Rh0gYeAbBU&currency=THB&cid=1920321",
        },
        "Chatuchak Weekend Market": {
            "location": [13.7995, 100.5512],
            "url": "https://gpt-vision-image-bucket.s3.ap-southeast-1.amazonaws.com/dall_e/aba3bc44-5d47-4d9c-828a-1f6e78aed693",
        },
        "Jim Thompson House": {
            "location": [13.7492, 100.5290],
            "url": "https://gpt-vision-image-bucket.s3.ap-southeast-1.amazonaws.com/dall_e/8bcb9f10-3cc2-4918-ba7a-db6623c0e3cb",
        },
        "Wat Arun": {
            "location": [13.7437, 100.4886],
            "url": "https://gpt-vision-image-bucket.s3.ap-southeast-1.amazonaws.com/dall_e/9b9f2e60-c78f-424c-95ce-11ef4542c9f4",
            "agoda_url": "https://www.agoda.com/activities/detail?activityId=1126288&cityId=9395&ds=gLSAa1Rh0gYeAbBU&currency=THB&cid=1920321",
        },
        "Khao San Road": {
            "location": [13.7587, 100.4972],
            "url": "https://gpt-vision-image-bucket.s3.ap-southeast-1.amazonaws.com/dall_e/6b6b610c-6422-4a74-ab88-e6ae0b02f1d4",
        },
    }
}


def generate_map(dest_city, dest_coords):
    city_map = folium.Map(
        location=dest_coords[dest_city]["The Grand Palace"]["location"], zoom_start=13
    )

    for destination, coords in dest_coords[dest_city].items():
        button = (
            ""
            if "agoda_url" not in coords.keys()
            else f"""
                    <a href="{coords['agoda_url']}"
                    <button type="button">Buy at Agoda</button>
                    </a>
                """
        )
        folium.Marker(
            location=coords["location"],
            popup=f"""
                <div>
                <span>{destination}</span>
                <img src="{coords["url"]}" alt="Flowers in Chania" width="230" height="172">
                <br/>
                {button}
                </div>
            """,
            tooltip=destination,
            icon=folium.features.CustomIcon(
                "https://agoda.sharepoint.com/:i:/r/sites/Agoda/Office%20templates/04%20Agoji%20Library/Agojiusingbinocular.png?csf=1&web=1&e=iedfFB",
                icon_size=(50, 50),
            ),
        ).add_to(city_map)

    # Return the map object
    return city_map

    # if __name__ == "main":


map = generate_map("Bangkok", DESTINATION)
st_folium(map, width=725)

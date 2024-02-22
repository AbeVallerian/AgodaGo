import folium
from get_openai import get_location_dict_from_city


def generate_map(dest_city: str):
    dest_coords = get_location_dict_from_city(dest_city)

    city_map = folium.Map(
        location=dest_coords[list(dest_coords.keys())[0]]["location"], zoom_start=13
    )

    for destination, coords in dest_coords.items():
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
                <img src="{coords["image_url"]}" width="230" height="172">
                <br/>
                {button}
                </div>
            """,
            tooltip=destination,
            icon=folium.features.CustomIcon(
                "https://drive.google.com/file/d/13A46gjJnTRuZtccH5yf6zbCwa0mZP_e5/view?usp=drive_link",
                icon_size=(50, 50),
            ),
        ).add_to(city_map)

    return city_map


# def get_locations(dest_city: str, dest_coords=DESTINATION):
#     return dest_coords[dest_city]

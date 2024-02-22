from typing import Dict, Tuple

import folium
from get_openai import get_location_dict_from_city


def generate_map(dest_city: str, n_locations: int) -> Tuple[folium.Map, Dict]:
    dest_coords: Dict = get_location_dict_from_city(dest_city, n_locations)

    city_map: folium.Map = folium.Map(
        location=dest_coords[list(dest_coords.keys())[0]]["location"], zoom_start=15
    )

    for destination, coords in dest_coords.items():
        folium.Marker(
            location=coords["location"],
            popup=f"""
                <div>
                <span>{destination}</span>
                <img src="{coords['image_url']}" width="230" height="172">
                <br/>
                <a><button type="button">Buy at Agoda</button></a>
                </div>
            """,
            tooltip=destination,
            icon=folium.features.CustomIcon(
                "https://agoda.sharepoint.com/:i:/r/sites/Agoda/Office%20templates/04%20Agoji%20Library/Agojiusingbinocular.png?csf=1&web=1&e=iedfFB",
                icon_size=(50, 50),
            ),
        ).add_to(city_map)

    return city_map, dest_coords

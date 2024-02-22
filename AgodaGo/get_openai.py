import hashlib
import json
import os

import openai

client = openai.OpenAI(
    api_key="sk-ssot-ds-hackathon", base_url="https://openai-proxy.agoda.is/v1"
)
city_name = "Bangkok"
n_locations = 3

ld = [
    {
        f"location{i}_name": {
            "type": "string",
            "description": f"Name of location {i}",
        },
        f"location{i}_latitude": {
            "type": "number",
            "description": f"Latitude of location {i}",
        },
        f"location{i}_longitude": {
            "type": "number",
            "description": f"Longitude of location {i}",
        },
    }
    for i in range(1, n_locations + 1)
]

get_locations_spec = {
    "name": "get_locations",
    "description": "Get locations of top tourist destinations within a city",
    "parameters": {
        "type": "object",
        "properties": {k: v for d in ld for k, v in d.items()},
        "required": [k for d in ld for k in d.keys()],
    },
}


def get_image(location_name):
    prompt = f"Show me a representative picture of {location_name} in {city_name} that motivates tourists to visit the place."
    prompt_hash = hashlib.sha1(prompt.encode()).hexdigest()
    cache_path = f"openai_cache/{prompt_hash}.txt"
    if os.path.isfile(cache_path):
        with open(cache_path, "r") as f:
            image_url = f.read()
    else:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url
        with open(cache_path, "w") as f:
            f.write(image_url)
    return image_url


def get_location_dict_from_city(city_name="Bangkok", n_locations=3):
    # Get locations
    prompt = f"Give me {n_locations} tourist location in Bangkok that are in walking distance within each other"
    prompt_hash = hashlib.sha1(prompt.encode()).hexdigest()
    cache_path = f"openai_cache/{prompt_hash}.txt"
    if os.path.isfile(cache_path):
        with open(cache_path, "r") as f:
            locations = json.load(f)
    else:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": f"Give me {n_locations} tourist location in {city_name} that are in walking distance within each other",
                }
            ],
            tools=[{"type": "function", "function": get_locations_spec}],
            tool_choice={"type": "function", "function": {"name": "get_locations"}},
        )
        fp = json.loads(response.choices[0].message.tool_calls[0].function.arguments)
        locations = {
            fp[f"location{i}_name"]: {
                "location": [fp[f"location{i}_latitude"], fp[f"location{i}_longitude"]]
            }
            for i in range(1, n_locations + 1)
        }
        with open(cache_path, "w") as f:
            json.dump(locations, f)

    # Get image
    for location_name in locations.keys():
        image_url = get_image(location_name)
        locations[location_name]["image_url"] = image_url

    return locations

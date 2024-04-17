import requests

def get_color_name(hex_code):
    response = requests.get(f"https://www.thecolorapi.com/id?hex={hex_code.lstrip('#')}")
    if response.status_code == 200:
        return response.json().get('name', {'value': 'Unknown'})
    return {'value': 'Unknown'}
def adding_extra_data(data : dict) -> dict:
    data['address_google_maps'] = f"https://www.google.com/maps/search/{data['address'].replace(' ', '%')}"
    data['abbrev_name'] = data['name'][:3]
    return data

def adding_extra_data(data: dict) -> dict:
    address_url = data["address"].replace(" ", "%")
    data["address_google_maps"] = f"https://www.google.com/maps/search/{address_url}"
    data["abbrev_name"] = data["name"][:3]
    return data



def adding_extra_data(data : list[dict]):
    for institution_data in data:
        institution_data['address_google_maps'] = f"https://www.google.com/maps/search/{institution_data['address'].replace(' ', '%')}"
        institution_data['abbrev_name'] = institution_data['name'][:3]
    return data

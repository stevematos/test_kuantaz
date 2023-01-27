from utils.institution import adding_extra_data


def test_adding_extra_data():

    data = {
        "address": "address mz test",
        "description": "test description",
        "name": "test name"
    }

    result = adding_extra_data(data)

    expected = {
        "abbrev_name": "tes",
        "address": "address mz test",
        "address_google_maps": "https://www.google.com/maps/search/address%mz%test",
        "description": "test description",
        "name": "test name"
    }

    assert result == expected

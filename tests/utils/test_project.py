from utils.project import process_data_for_days_for_end


def test__count_days_for_end():

    data = {
        "end_date": "2023-01-21",
        "name": "Project 2"
    }

    result = process_data_for_days_for_end(data)

    expected = {
        "count_days_for_end": 0,
        "name": "Project 2"
    }

    assert result == expected

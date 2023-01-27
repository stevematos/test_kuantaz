from unittest.mock import patch
import pytest

from config.exceptions import InstitutionNotFound
from services.institution import read_institution
from sqlalchemy.exc import NoResultFound


@pytest.mark.parametrize(
    ("_id", "is_not_found"),
    (
        (1, False),
        (2, True),
    ),
)
@patch("services.institution.get_institution_by_id")
def test_read_institution(mock_get_institution_by_id, _id, is_not_found):

    institution_data = {
        "address": "Address 1",
        "description": "Description 1",
        "name": "Institution 1",
        "projects": [
            {
                "end_date": "2023-01-21",
                "name": "Project 2",
                "start_date": "2023-01-03"
            },
            {
                "end_date": "2023-01-28",
                "name": "Project 1",
                "start_date": "2023-01-13"
            }
        ]
    }

    def get_institution_by_id_side_effect(_id, is_dump=True, **kwargs):
        if _id == 1:
            return institution_data
        elif _id == 2:
            raise NoResultFound()

    mock_get_institution_by_id.side_effect = get_institution_by_id_side_effect

    if is_not_found:
        with pytest.raises(InstitutionNotFound):
            read_institution(_id)
    else:
        result = read_institution(_id)
        assert result == institution_data

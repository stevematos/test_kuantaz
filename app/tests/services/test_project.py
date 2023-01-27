from datetime import date
from unittest.mock import patch

from models import Project
from schemas.project import ProjectEndDateSchema
from services.project import read_projects_with_days_to_end


@patch("services.project.process_data_for_days_to_end")
@patch("services.project.get_all_projects")
def test_read_projects_with_days_for_end(
    mock_get_all_projects, mock_process_data_for_days_for_end
):

    project_1 = Project(
        id=1,
        name="Project 1",
        start_date=date(2023, 1, 13),
        end_date=date(2023, 1, 28),
    )

    project_2 = Project(
        id=2,
        name="Project 2",
        start_date=date(2023, 1, 13),
        end_date=date(2023, 1, 22),
    )

    mock_get_all_projects.return_value = [project_1, project_2]

    schema = ProjectEndDateSchema()

    project_1_data = schema.dump(project_1)
    project_2_data = schema.dump(project_2)

    def process_data_for_days_for_end_side_effect(data, **kwargs):
        if data == project_1_data:
            data["count_days_for_end"] = 0
        elif data == project_2_data:
            data["count_days_for_end"] = 2
        return data

    mock_process_data_for_days_for_end.side_effect = (
        process_data_for_days_for_end_side_effect
    )

    result = read_projects_with_days_to_end()

    expected = [
        {
            "end_date": "2023-01-28",
            "name": "Project 1",
            "count_days_for_end": 0,
        },
        {
            "end_date": "2023-01-22",
            "name": "Project 2",
            "count_days_for_end": 2,
        },
    ]

    assert result == expected

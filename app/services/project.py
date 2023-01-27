from queries.project import get_all_projects
from schemas.project import ProjectEndDateSchema, ProjectGetSchema
from utils.project import process_data_for_days_to_end


def read_all_projects() -> list[dict]:
    schema = ProjectGetSchema(many=True)
    return schema.dump(get_all_projects())


def read_projects_with_days_to_end() -> list[dict]:
    schema = ProjectEndDateSchema(many=True)

    projects = get_all_projects()
    data_projects = schema.dump(projects)
    data_projects = [
        process_data_for_days_to_end(data_project) for data_project in data_projects
    ]

    return data_projects

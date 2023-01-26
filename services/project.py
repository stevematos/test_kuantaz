from queries.project import get_all_projects
from schemas.project import ProjectGetSchema


def read_all_projects() -> list[dict]:
    schema = ProjectGetSchema(many=True)
    return schema.dump(get_all_projects())

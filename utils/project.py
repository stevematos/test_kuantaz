from datetime import datetime


def _count_days_for_end(end_date_str: str):
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
    date_now = datetime.now().date()

    difference_days = (end_date-date_now).days

    return difference_days if difference_days > 0 else 0


def process_data_for_days_for_end(data: list[dict]) -> list[dict]:
    for project_data in data:
        _count_days_for_end(project_data['end_date'])
        project_data['count_days_for_end'] = _count_days_for_end(project_data.pop('end_date'))
    return data

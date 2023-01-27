class InstitutionErrorValidation(Exception):
    def __init__(self, errors: dict[str: []]) -> None:
        self.errors = errors

    def __str__(self):
        message = ""
        for field, errors in self.errors.items():
            message += f"{field}: {','.join(errors)}"

        return message


class InstitutionNotFound(Exception):
    def __str__(self):
        return f"Institution not found"


class UserNotFound(Exception):
    def __str__(self):
        return f"User not found"
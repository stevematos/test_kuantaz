class InstitutionErrorValidation(Exception):
    def __init__(self, errors: dict[str:[]]) -> None:
        self.errors = errors

    def __str__(self):
        message = ""
        for field, errors in self.errors.items():
            message += f"{field}: {','.join(errors)}"

        return message


class InstitutionNotFound(Exception):
    def __str__(self):
        return "Institution not found"


class UserNotFound(Exception):
    def __str__(self):
        return "User not found"

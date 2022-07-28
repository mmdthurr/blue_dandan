class Flood(Exception):
    def __init__(self, retry_after: int):
        self.retry_after = retry_after

    def __str__(self):
        return "Too many requests."


class Unauthorized(Exception):
    def __str__(self):
        return "Bot has not enough rights to perform the requested action."


class Forbidden(Exception):
    def __str__(self):
        return "Privacy violation."


class BadRequest(Exception):
    def __str__(self):
        return "Could not process the request correctly."


class UnknownError(Exception):
    def __str__(self):
        return "Unknown error happened."

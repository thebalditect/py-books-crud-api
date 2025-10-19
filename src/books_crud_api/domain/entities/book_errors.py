from .common.error import Error


class BookErrors:

    @staticmethod
    def not_found(id: int) -> Error:
        return Error.not_found(
            code="Books", description=f"Book with id {id} was not found."
        )

from __future__ import annotations
from dataclasses import dataclass
from .error_type import ErrorType


@dataclass(frozen=True)
class Error:
    code: str
    description: str
    error_type: ErrorType

    @staticmethod
    def failure(code: str, description: str) -> Error:
        return Error(code=code, description=description, error_type=ErrorType.FAILURE)

    @staticmethod
    def conflict(code: str, description: str) -> Error:
        return Error(code=code, description=description, error_type=ErrorType.CONFLICT)

    @staticmethod
    def validation(code: str, description: str) -> Error:
        return Error(
            code=code, description=description, error_type=ErrorType.VALIDATION
        )

    @staticmethod
    def not_found(code: str, description: str) -> Error:
        return Error(code=code, description=description, error_type=ErrorType.NOT_FOUND)

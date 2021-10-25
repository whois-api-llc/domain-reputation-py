import copy
from datetime import datetime

from .base import BaseModel
import sys

if sys.version_info < (3, 9):
    import typing


def _datetime_from_int(values: dict, key: str) -> datetime or None:
    if key in values and values[key]:
        return datetime.utcfromtimestamp(values[key])
    return None


def _string_value(values: dict, key: str) -> str:
    if key in values and values[key]:
        return str(values[key])
    return ''


def _float_value(values: dict, key: str) -> float:
    if key in values and values[key]:
        return float(values[key])
    return 0.0


def _int_value(values: dict, key: str) -> int:
    if key in values and values[key]:
        return int(values[key])
    return 0


def _list_value(values: dict, key: str) -> list:
    if key in values and type(values[key]) is list:
        return copy.deepcopy(values[key])
    return []


def _list_of_objects(values: dict, key: str, classname: str) -> list:
    r = []
    if key in values and type(values[key]) is list:
        r = [globals()[classname](x) for x in values[key]]
    return r


def _bool_value(values: dict, key: str) -> bool:
    if key in values and values[key]:
        return bool(values[key])
    return False


class TestResult(BaseModel):
    test: str
    test_code: int
    warnings: [str]
    warning_codes: [int]

    def __init__(self, values):
        super().__init__()
        self.test = ''
        self.test_code = 0
        self.warnings = []
        self.warning_codes = []

        if values:
            self.test = _string_value(values, 'test')
            self.test_code = _int_value(values, 'testCode')
            self.warnings = _list_value(values, 'warnings')
            self.warning_codes = _list_value(values, 'warningCodes')


class Response(BaseModel):
    mode: str
    reputation_score: float
    if sys.version_info < (3, 9):
        test_results: typing.List[TestResult]
    else:
        test_results: [TestResult]

    def __init__(self, values):
        super().__init__()
        self.mode = ''
        self.reputation_score = 0.0
        self.test_results = []

        if values is not None:
            self.mode = _string_value(values, 'mode')
            self.reputation_score = _float_value(values, 'reputationScore')
            self.test_results = _list_of_objects(values, 'testResults', 'TestResult')


class ErrorMessage(BaseModel):
    code: int
    message: str

    def __init__(self, values):
        super().__init__()

        self.code = 0
        self.message = ''

        if values is not None:
            self.code = _int_value(values, 'code')
            self.message = _string_value(values, 'messages')

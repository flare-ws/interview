from datetime import datetime
from typing import List
from enum import Enum


class Tag:
    def __init__(self, major: int, minor: int, patch: int):
        self.major = major
        self.minor = minor
        self.patch = patch


class TestStatus(Enum):
    Passed = 0
    Failed = 1


class TestRun:
    def __init__(self, tag: Tag, status: TestStatus, date: datetime):
        self.tag = tag
        self.status = status
        self.date = date


class TestReport:
    def __init__(self, first_broken_version: str, break_time: datetime, fixed_version: str,
                 fix_time: datetime):
        self.first_broken_version = first_broken_version
        self.break_time = break_time
        self.fixed_version = fixed_version
        self.fix_time = fix_time


# GenerateTestReport
# We need to find:
# 1. moment in time when tests begin to FAIL and the first BROKEN version of the application
# 2. moment in time when tests begin to PASS and the first FIXED version of the application
#
# Example input:
# [
#	{"1.0.1", 1, "2023-09-14 10:30"},
#	{"1.1.0", 0, "2023-09-15 12:30"},
#	{"1.0.0", 0, "2023-09-13 10:36"}
# ]
def generate_test_report(test_runs: List[TestRun]) -> TestReport:
    return TestReport("", datetime.now(), "", datetime.now())

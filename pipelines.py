from typing import List


class Job:
    def __init__(self, name: str, duration: int, status: str, stage: str):
        self.name = name
        self.duration = duration
        # passed, failed
        self.status = status
        self.stage = stage


class Pipeline:
    def __init__(self, jobs: List[Job]):
        self.jobs = jobs


# calculate_pipeline_duration accepts Pipeline object and returns its duration
# Pipeline's - sum of all its jobs durations
def calculate_pipeline_duration(pipeline: Pipeline) -> int:
    return 0


# shortest_passed_job accepts list of Pipeline objects and returns the Job with the lowest Duration
# between Jobs which status is "passed"
def shortest_passed_job(pipelines: List[Pipeline]) -> Job:
    return Job("", 0, "", "")
